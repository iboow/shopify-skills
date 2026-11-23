# Simuler un changement

Geler une référence datée avec prix réalisé HT, panier, mix, volume, coûts, attribution et charges fixes. Dupliquer les entrées pour chaque scénario. Étiqueter les variables modifiées, les coûts dépendants et les invariants. Pour chaque colonne afficher avant, après, écart unitaire et total, seuil et hypothèses. Un modèle prudent/central/optimiste emploie des volumes fournis ou explicitement illustratifs.

| Demande | Recalcul |
|---|---|
| Hausse de prix ou remise | Recalculer prix net et taxes ligne à ligne, commissions et paiement sur la nouvelle assiette. Recalculer les frais à tranches et la livraison si le panier franchit un seuil. |
| Livraison offerte dès 60 | Rejouer chaque panier admissible selon la règle réelle (devise, remises, taxes). Supprimer son port facturé, conserver le coût transporteur, recalculer taxe et paiement. Si seule une moyenne est connue, demander la part des paniers admissibles. |
| CPA à 18 | Dépense = 18 × commandes acquises à mix constant ; ne pas réutiliser simultanément la dépense historique. |
| Bundle de 2 | Additionner les COGS réels des composants ; appliquer une fois le port du nouveau colis, l’emballage et le fixe par paiement. Recalculer prix du lot, retours et éventuelle remise. |
| Logistique +20 % | Multiplier uniquement le poste concerné par 1,20. Un forfait mensuel reste fixe sauf changement de contrat. |
| 100 ventes | Préciser unités ou commandes. Multiplier les variables unitaires par le volume, les taux par leurs assiettes et intégrer les charges fixes une fois pour la période simulée. |

**Prix cible.** Pour une unité par commande, port facturé nul, prix HT P, coûts fixes par commande K (COGS et coûts unitaires indépendants du prix), prélèvement proportionnel f × P et contribution cible t × P, P = K/(1−f−t). Inclure le CPA dans K si la cible est après publicité. Un dénominateur nul ou négatif rend la cible inaccessible pour K positif. Pour plusieurs paliers, résoudre par tranche, vérifier la tranche obtenue puis recalculer au prix arrondi commercial, en remontant au centime si nécessaire. Pour une commission sur TTC, convertir son assiette avant de résoudre.

Pour conserver une contribution totale de référence Q₀ × B₀ avec une nouvelle contribution unitaire B₁ positive, volume requis = plafond(Q₀ × B₀ / B₁). Si B₁ ≤ 0, augmenter le volume ne restaure pas une contribution totale positive. Distinguer ce seuil du volume couvrant les fixes : plafond(F / contribution unitaire après publicité). Ne déduire aucune élasticité du seul changement de prix.
