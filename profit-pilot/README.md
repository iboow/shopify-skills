# Profit Pilot — Shopify Profitability Analyst

Combien reste-t-il sur une commande, et combien pouvez-vous dépenser pour l’acquérir ? Profit Pilot rapproche ventes, coûts et publicité, puis montre le calcul, sa couverture et les informations manquantes. Le skill utilise uniquement les lectures déjà autorisées par votre assistant.

## Installation et premier diagnostic

1. Décompressez le ZIP. Dans votre projet Claude Code, placez le dossier entier dans `.claude/skills/profit-pilot/`. Pour Codex, utilisez `.agents/skills/profit-pilot/`. Conservez les sous-dossiers.
2. Activez l’intégration Shopify compatible dans les réglages de votre assistant. Sélectionnez la boutique et autorisez les lectures nécessaires dans le parcours officiel. Les opérations disponibles dépendent du connecteur et des droits du compte.
3. Ouvrez le projet. Dans Claude Code, invoquez `/profit-pilot` ; dans Codex, `$profit-pilot`. Essayez « Analyse ma rentabilité Shopify le mois dernier et montre combien il me reste par commande ». Si les coûts manquent, indiquez leur unité et leur contenu, par exemple « 6 € de préparation et transport par commande France, emballage compris ».
4. Pour une simulation ciblée : « Sur cette variante seulement, que devient ma contribution si je baisse le prix de 10 % ? ». Pour exporter : « Donne-moi le tableau par variante en CSV avec les hypothèses et la couverture ».

**ChatGPT ou autre assistant.** Si l’import de skills est indisponible, joindre SKILL.md et les références nécessaires comme fichiers de contexte, activer la lecture Shopify compatible dans cette conversation, puis écrire « Applique Profit Pilot aux données autorisées. Vérifie le périmètre avant de calculer ». Un export marchand peut servir de source identifiée. La disponibilité d’un connecteur ne garantit pas l’accès aux coûts ou aux campagnes. Pour un essai hors boutique, demander explicitement une simulation fictive.

## Calcul local facultatif

Depuis le dossier du skill, Python 3 sans dépendances :

```sh
python3 scripts/calculations.py
python3 -m unittest discover -s tests -p 'test_*.py' -v
```

La première commande reproduit le cas de référence. Pour vos données, passez le chemin d’un fichier JSON à la place de l’exemple intégré. Exemple d’une commande fictive, coûts en EUR, assiette HT :

```json
{"currency":"EUR","products":"100","shipping_income":"0","cogs":"30","logistics":"10","payment":"3","other_variable":"0","ads":"25","fixed":"12","acquired_orders":1,"attributed_sales":"100","cohort":true}
```

`--digits 2` fixe les décimales monétaires affichées ; les taux sont des fractions. Une entrée omise produit un résultat dépendant null. Les zéros de l’exemple sont confirmés. Consulter le [contrat de calcul](references/financial-formulas.md) et le [cas publicitaire](examples/ads-break-even.md) avant de fournir une cohorte attribuée.

## Contenu

- `SKILL.md` pilote l’analyse. Les sept fichiers de `references/` traitent sources, formules, acquisition, économie unitaire, scénarios, fiscalité/devises et restitution.
- `examples/` contient quatre rapports fictifs : [boutique](examples/store-profitability.md), [produits](examples/product-profitability.md), [publicité](examples/ads-break-even.md) et [prix](examples/pricing-simulation.md).
- `scripts/calculations.py` calcule localement. `tests/` contient les tests Python, les résultats financiers attendus et la recette connecteur. L’intégration sur compte marchand reste à valider.

Format de distribution : [spécification Agent Skills](https://agentskills.io/specification).
