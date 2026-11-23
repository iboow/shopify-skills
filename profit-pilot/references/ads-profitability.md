# Seuils d’acquisition

Décrire période, canal, fenêtre et modèle d’attribution, dépense D, revenu attribué V (HT ou TTC, brut ou net, port), commandes acquises Q et nouveaux clients distincts N. Fixer une date d’arrêt pour retours et conversions tardives. Éviter les doublons entre plateformes attribuant la même commande. Si seule la vente boutique est connue, ventes totales / dépenses est un ratio global distinct du ROAS attribué.

| Indicateur | Formule et condition |
|---|---|
| ROAS observé | V / D, si D > 0, V connu et même campagne. |
| CPA observé | D / Q pour des achats attribués sur le même périmètre. |
| CAC média | D / N. Un CAC complet inclut tous les coûts d’acquisition pertinents ; préciser leur composition. Un client peut acheter plusieurs fois. |
| CPA maximal contributif | B / Q pour la cohorte acquise. Si B ≤ 0, aucun budget positif soutenable. |
| ROAS d’équilibre | V / B si V et B positifs, même cohorte. Si V = R, cela donne 1 / (B/R). Si V est TTC ou sur une assiette différente, réconcilier explicitement les deux bases avant utilisation. |
| Budget théorique | B pour la cohorte à mix et volume fixes, plancher zéro. Pour couvrir F de charges et un objectif T, plafond max(0, B − F − T). Indiquer lorsque l’objectif reste impossible même sans publicité. |
| Contribution par commande acquise | (B − D) / Q. Après fixes alloués, (B − D − F) / Q est un résultat distinct. |

Dans le moteur, renseigner attributed_sales, acquired_orders et new_customers seulement si leur définition et leur période correspondent à ads. cohort=true certifie en outre que les coûts et les revenus économiques sont ceux des commandes attribuées ; sinon laisser false. Les seuils sont des plafonds à volume et panier donnés. Présenter séparément tout scénario de réachat/LTV avec horizon, contribution par réachat et taux de rétention fourni.
