"""Profit Pilot. Entrées normalisées HT, une devise et un périmètre par calcul."""
import argparse
import json
import re
from decimal import Decimal, InvalidOperation, ROUND_HALF_UP


def number(value):
    if isinstance(value, bool) or not isinstance(value, (str, int, Decimal)):
        raise ValueError("Utiliser un entier ou un décimal en chaîne.")
    try:
        result = Decimal(value)
    except InvalidOperation as exc:
        raise ValueError("Nombre décimal invalide") from exc
    if not result.is_finite():
        raise ValueError("Nombre non fini")
    return result


def difference(revenue, *costs):
    if revenue is None or None in costs:
        return None
    return revenue - sum(costs)


def ratio(numerator, denominator):
    if numerator is None or denominator is None or denominator <= 0:
        return None
    return numerator / denominator


def count(value):
    if value is None:
        return None
    n = number(value)
    if n < 0 or n != n.to_integral_value():
        raise ValueError("Effectif entier positif ou nul attendu")
    return n


def unit_cost(units, restocked, historic):
    shipped, recovered = count(units), count(restocked)
    if shipped is None or recovered is None or historic is None:
        return None
    cost = number(historic)
    if cost < 0:
        raise ValueError("Coût unitaire négatif")
    # Les reprises peuvent provenir de ventes d’une période antérieure.
    return (shipped - recovered) * cost


def payment(base, rate, fixed, transactions):
    if None in (base, rate, fixed, transactions):
        return None
    base, rate, fixed = map(number, (base, rate, fixed))
    if min(base, rate, fixed) < 0 or rate > 1:
        raise ValueError("Vérifier le barème et son assiette")
    return base * rate + fixed * count(transactions)


def currency(code):
    if not isinstance(code, str) or not re.fullmatch("[A-Z]{3}", code):
        raise ValueError("Code devise à trois lettres attendu")
    return code


def convert(amount, source, target, rate=None):
    if currency(source) == currency(target):
        return number(amount)
    if rate is None:
        return None
    fx = number(rate)
    if fx <= 0:
        raise ValueError("Taux de change non positif")
    return number(amount) * fx


def net_products(gross_ht, discounts_ht, reversals_ht):
    """Les reprises sont nettes de remise et saisies en déductions positives."""
    if None in (gross_ht, discounts_ht, reversals_ht):
        return None
    amounts = list(map(number, (gross_ht, discounts_ht, reversals_ht)))
    if min(amounts) < 0:
        raise ValueError("Brut et déductions positives attendus")
    return difference(*amounts)


def ex_tax(charged, included_tax):
    if None in (charged, included_tax):
        return None
    return number(charged) - number(included_tax)


def price_target(independent_costs, fee_rate, contribution_rate):
    """Modèle linéaire HT unitaire documenté dans scenario-modeling.md."""
    costs, fee, target = map(number, (independent_costs, fee_rate, contribution_rate))
    if min(costs, fee, target) < 0 or max(fee, target) > 1:
        raise ValueError("Vérifier les coûts et les taux fractionnaires")
    return ratio(costs, 1 - fee - target)


def analyze(data):
    fields = ("products", "shipping_income", "cogs", "logistics", "payment",
              "other_variable", "ads", "fixed", "attributed_sales")
    allowed = set(fields) | {"currency", "acquired_orders", "new_customers", "cohort"}
    if set(data) - allowed:
        raise ValueError("Champs inconnus : " + str(set(data) - allowed))
    code = currency(data.get("currency"))
    v = {k: None if data.get(k) is None else number(data[k]) for k in fields}
    if v["ads"] is not None and v["ads"] < 0:
        raise ValueError("Dépense publicitaire négative")
    cohort = data.get("cohort", False)
    if type(cohort) is not bool:
        raise ValueError("cohort doit être un booléen")
    orders = count(data.get("acquired_orders"))
    customers = count(data.get("new_customers"))
    product, ship = v["products"], v["shipping_income"]
    rev = product + ship if None not in (product, ship) else None
    gross = difference(product, v["cogs"])
    pre = difference(rev, v["cogs"], v["logistics"], v["payment"], v["other_variable"])
    post = difference(pre, v["ads"])
    # cohort confirme que montants ET dépenses portent sur les commandes attribuées.
    budget = max(Decimal(0), pre) if cohort and pre is not None else None
    return dict(currency=code, revenue=rev, gross=gross, gross_rate=ratio(gross, product),
                pre_ads=pre, post_ads=post, pre_rate=ratio(pre, rev), post_rate=ratio(post, rev),
                operating=difference(post, v["fixed"]), budget=budget,
                roas=ratio(v["attributed_sales"], v["ads"]),
                roas_break_even=ratio(v["attributed_sales"], pre) if cohort and
                v["attributed_sales"] is not None and v["attributed_sales"] > 0 else None,
                cpa=ratio(v["ads"], orders), max_cpa=ratio(budget, orders),
                media_cac=ratio(v["ads"], customers), acquired_post=ratio(post, orders) if cohort else None)


def display(value, places):
    if value is None:
        return None
    return str(value.quantize(Decimal(1).scaleb(-places), rounding=ROUND_HALF_UP))


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("file", nargs="?", help="JSON normalisé, sinon exemple de référence")
    parser.add_argument("--digits", type=int, choices=range(0, 7), default=2,
                        help="Décimales monétaires de restitution")
    args = parser.parse_args()
    try:
        if args.file:
            with open(args.file, encoding="utf-8") as stream:
                data = json.load(stream, parse_float=Decimal)
        else:
            data = dict(currency="EUR", products=100, shipping_income=0, cogs=30,
                        logistics=10, payment=3, other_variable=0, ads=25, fixed=12,
                        acquired_orders=1, attributed_sales=100, cohort=True)
        if not isinstance(data, dict):
            raise ValueError("Objet JSON attendu")
        output = analyze(data)
        for key in output.keys() - {"currency"}:
            places = 4 if key.endswith("rate") else 3 if key.startswith("roas") else args.digits
            output[key] = display(output[key], places)
        print(json.dumps(output, ensure_ascii=False, indent=2))
    except (ValueError, OSError, InvalidOperation) as exc:
        parser.error(str(exc))


if __name__ == "__main__":
    main()
