import json
import subprocess
import sys
import unittest
from decimal import Decimal as D
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
import calculations as calc

BASE = dict(currency="EUR", products="100", shipping_income=0, cogs=30, logistics=10,
            payment=3, other_variable=0, ads=25, fixed=12, attributed_sales=100,
            acquired_orders=1, cohort=True)


def run(**changes):
    return calc.analyze(dict(BASE, **changes))


class FinancialTests(unittest.TestCase):
    def test_reference(self):
        r = run()
        for k, v in dict(gross=70, pre_ads=57, post_ads=32, operating=20, max_cpa=57,
                         roas=4, acquired_post=32, budget=57, cpa=25).items():
            self.assertEqual(r[k], v, k)
        self.assertEqual(calc.display(r["roas_break_even"], 3), "1.754")

    def test_missing_cost(self):
        r = run(cogs=None)
        self.assertEqual(r["revenue"], 100)
        self.assertIsNone(r["gross"])
        self.assertIsNone(r["operating"])

    def test_no_ad_report(self):
        r = run(ads=None)
        self.assertEqual(r["pre_ads"], 57)
        self.assertIsNone(r["post_ads"])
        self.assertIsNone(r["roas"])

    def test_attribution_unknown(self):
        r = run(attributed_sales=None, cohort=False, acquired_orders=None)
        for k in ("roas", "roas_break_even", "max_cpa", "budget", "cpa"):
            self.assertIsNone(r[k])

    def test_partial_costs(self):
        self.assertIsNone(run(logistics=None)["pre_ads"])
        self.assertEqual(run(logistics=None)["gross"], 70)

    def test_discount_and_refund(self):
        self.assertEqual(calc.net_products(120, 20, 40), 60)
        self.assertEqual(calc.net_products(0, 0, 15), -15)

    def test_returned_to_stock(self):
        self.assertEqual(calc.unit_cost(3, 1, '9.50'), 19)
        self.assertEqual(calc.unit_cost(0, 1, '9.50'), D('-9.50'))

    def test_refunded_without_stock(self):
        self.assertEqual(calc.unit_cost(3, 0, '9.50'), D('28.50'))

    def test_two_variants_shared_order(self):
        cogs = calc.unit_cost(1, 0, 10) + calc.unit_cost(1, 0, 18)
        r = run(products=55, cogs=cogs, shipping_income=4, logistics=7, payment=2, ads=0)
        self.assertEqual((r["gross"], r["pre_ads"]), (27, 22))
        self.assertIsNone(calc.unit_cost(1, 0, None))

    def test_free_shipping(self):
        self.assertEqual(run(shipping_income=0)["pre_ads"], 57)
        self.assertEqual(run(shipping_income=5)["pre_ads"], 62)

    def test_transaction_fee(self):
        self.assertEqual(calc.payment(120, '0.025', '0.30', 1), D('3.30'))

    def test_tax_regimes(self):
        self.assertEqual(calc.ex_tax(120, 20), 100)
        self.assertEqual(calc.ex_tax(120, 0), 120)
        self.assertIsNone(calc.ex_tax(120, None))

    def test_fx(self):
        self.assertEqual(calc.convert(20, 'USD', 'EUR', '0.9') + 10, 28)
        self.assertIsNone(calc.convert(20, 'GBP', 'EUR'))
        self.assertEqual(calc.convert(20, 'EUR', 'EUR'), 20)

    def test_zero_divisors(self):
        r = run(ads=0, acquired_orders=0, products=0)
        for k in ('gross_rate', 'cpa', 'roas', 'roas_break_even', 'max_cpa'):
            self.assertIsNone(r[k])

    def test_nonpositive_contribution(self):
        r = run(cogs=140)
        self.assertIsNone(r["roas_break_even"])
        self.assertEqual(r["budget"], 0)

    def test_different_attributed_basis(self):
        self.assertEqual(run(attributed_sales=120)["roas_break_even"], D(120)/57)

    def test_cac_and_repeat(self):
        r = run(new_customers=1, acquired_orders=2)
        self.assertEqual(r["cpa"], D("12.5"))
        self.assertEqual(r["media_cac"], 25)

    def test_price_change(self):
        fee = calc.payment(90, '0.03', 0, 1)
        r = run(products=90, payment=fee)
        self.assertEqual(r["post_ads"], D("22.30"))
        self.assertEqual(100*r["post_ads"]-1200, 1030)

    def test_cpa_increase(self):
        self.assertEqual(run(ads=35)["post_ads"], 22)

    def test_price_target(self):
        self.assertEqual(calc.price_target(67, '.03', '.30'), 100)
        self.assertIsNone(calc.price_target(67, '.70', '.30'))

    def test_input_validation(self):
        for bad in ('NaN', 'Infinity', True, 3.14):
            with self.assertRaises(ValueError):
                calc.number(bad)
        for bad in (dict(currency="eu"), dict(acquired_orders='0.5'), dict(ads=-1),
                    dict(cohort="false"), dict(producs=1)):
            with self.assertRaises(ValueError):
                run(**bad)

    def test_rounding(self):
        self.assertEqual(calc.display(D('1.005'), 2), '1.01')

    def test_cli(self):
        command = [sys.executable, str(ROOT/'scripts'/'calculations.py')]
        output = json.loads(subprocess.check_output(command))
        self.assertEqual(output['operating'], '20.00')
        self.assertEqual(output['roas_break_even'], '1.754')


if __name__ == '__main__':
    unittest.main()
