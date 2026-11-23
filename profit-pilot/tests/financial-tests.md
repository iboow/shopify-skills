# Vérification financière

Depuis la racine du skill, utiliser la commande de tests du README. Les entrées synthétiques sont définies dans test_calculations.py. Le cas de référence est aussi disponible en exécutant directement le moteur sans argument.

| Jeu de contrôle | Résultat attendu |
|---|---|
| Revenu produits 100 HT, COGS 30, logistique 10, paiement 3, publicité 25, fixe 12 ; une commande acquise, assiettes identiques | Marge brute 70, contribution avant/après 57/32, résultat 20, CPA maximal contributif 57, ROAS de seuil 1,754×, ROAS observé 4× |
| Publicité absente | Avant publicité 57, après publicité indisponible |
| Brut 120, remise 20, remboursement produit net 40 | Ventes nettes 60 |
| 3 unités à 9,50, une remboursée | COGS 19 si restockée intégralement, 28,50 si perdue ou conservée par le client |
| Deux variantes coûtant 10 et 18, ventes 55, port encaissé 4 et payé 7, paiement 2 | Marge brute 27, contribution 22 au niveau commande |
| Paiement 2,5 % de 120 + fixe 0,30 | Frais 3,30 |
| Conversion 20 USD à 0,90 EUR/USD + 10 EUR | 28 EUR ; sans taux, aucun total converti |
| Prix réduit à 90, commission 3 %, CPA 25 | Contribution après publicité 22,30 ; résultat 1 030 pour 100 commandes et 1 200 de fixes |
| Hausse du CPA de 25 à 35 | Contribution après publicité 22 |
| Coûts indépendants 67, frais 3 %, contribution cible 30 % | Prix HT 100 |
| Revenu attribué TTC 120 pour le même groupe, contribution HT 57 | Seuil sur base TTC 120/57 ; interdire le raccourci 100/57 sur cette base |

## Comparaison avec et sans skill

Deux sessions indépendantes ont traité le cas de référence et sa variante « dépense publicitaire inconnue ». La première a travaillé sans skill. La seconde a utilisé Profit Pilot et le moteur local. Toutes deux ont retrouvé 70 / 57 / 32 / 20 €, distingué le plafond contributif de 57 € du plafond après fixes de 45 €, et laissé les métriques observées dépendant de la dépense indéterminées quand celle-ci manquait. L’arrondi du seuil contributif était 1,75× sans skill et 1,754× avec le moteur.

La session sans skill a proposé un CPA de 25 € pour maintenir un résultat de 20 €. Avec le skill, la recommandation était un CPA inférieur à 45 € pour conserver un résultat positif. Les objectifs diffèrent et les deux recommandations sont cohérentes. La session avec skill a explicité le port facturé nul et l’absence d’autres coûts variables et fourni une méthode de reproduction. Ce seul cas ne démontre pas une supériorité statistique.
