# Du chiffre d’affaires au résultat de gestion

Normaliser les montants dans une devise commune. Dans les formules ci-dessous, une remise et une restitution sont des déductions positives. Dans un export signé, additionner les mouvements avec leur signe. Les ajustements de période peuvent produire des ventes ou un COGS nets négatifs.

| Étape | Calcul | Point de contrôle |
|---|---|---|
| Ventes produits nettes HT P | Brut produits HT − remises HT − reprises de revenu produits HT, après remise | Si le rapport fournit déjà P, le reprendre directement. Un même retour suivi d’un remboursement ne doit réduire le revenu qu’une fois. |
| Livraison nette HT L | Livraison facturée moins remises et remboursements de port, hors taxe | Isoler les frais de port payés au transporteur dans les coûts. |
| Revenu économique R | P + L dans le périmètre standard | Réconcilier séparément autres revenus, droits collectés pour tiers et taxes. Un encaissement, un versement bancaire ou la vente d’une carte cadeau ne constitue pas à lui seul une vente produit. |
| COGS C | Somme des unités sorties × coût historique du lot, moins coût historique récupéré en stock revendable | Une annulation avant expédition ne crée pas de sortie. Une restitution sans retour physique ne reprend aucun coût. Suivre un retour déprécié à sa valeur récupérable documentée. |
| Marge brute produit G | P − C ; taux G/P | Dénominateur strictement positif. Restreindre P et C aux mêmes lignes pour une marge partielle. |
| Contribution avant publicité B | R − C − logistique − paiement − autres variables | Logistique : préparation, emballage, distribution et retour. Autres variables : commissions et applications à l’usage. Éviter de compter à nouveau un produit perdu déjà inclus dans C. |
| Contribution après publicité A | B − dépenses publicitaires du périmètre | Taux avant/après = B/R et A/R lorsque R > 0. |
| Résultat d’exploitation estimé | A − charges fixes pertinentes de la période | Montrer abonnements, logistique fixe et autres charges couvertes. Isoler toute omission. Ce résultat de gestion ne certifie aucun bénéfice comptable ou fiscal. |

Pour un barème de paiement, calculer transaction par transaction : assiette réellement débitée × taux + fixe. Vérifier taxes/port inclus dans l’assiette, traitement des frais conservés sur remboursement et frais de litige. Utiliser les frais réels si disponibles. Rapprocher revenus et coûts avec les rapports agrégés et expliquer tout résidu.

**Contrat du moteur.** Un objet JSON représente une commande, un produit alloué, une période ou une cohorte déjà normalisés. Utiliser les clés du [fichier de calcul](../scripts/calculations.py) : products=P, shipping_income=L, cogs=C, logistics, payment, other_variable, ads, fixed en devise commune. Valeurs numériques en chaînes décimales de préférence. Champ absent ou null = inconnu ; zéro exige une justification. Les entrées sont des totaux de périmètre, pas des prix unitaires. Les taux rendus sont des fractions. Les frais annexes et autres types de revenu hors modèle requièrent un rapprochement séparé. Ne pas injecter un revenu annexe dans les ventes produits pour faire cadrer le total.
