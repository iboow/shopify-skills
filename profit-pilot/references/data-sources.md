# Construire le périmètre de preuve

Inventorier les lectures autorisées : boutique et devise, catalogue, variantes/coûts, commandes, rapports financiers et marketing. Tester la capacité utile. Privilégier un rapport natif dont les définitions conviennent. N’utiliser ShopifyQL ou GraphQL que via une opération de lecture effectivement exposée. Un accès au catalogue ne prouve pas l’accès aux commandes, aux coûts ou aux campagnes.

| Source | Champs à rechercher | Contrôle |
|---|---|---|
| Catalogue | ID produit et variante, SKU, prix courant et comparatif, coût actuel, devise, catégorie, statut | Joindre par ID stable ; le prix comparatif ne mesure pas une remise réalisée. |
| Ventes | ID commande, ligne et événement, date et fuseau, quantités, prix, remises, annulations, retours, remboursements, livraison, taxes, devise | Choisir date d’événement pour un mois d’activité ou cohorte de commandes avec date d’arrêt pour suivre les retours ultérieurs. |
| Finance | Ventes nettes, coût historique, marge brute par période/variante | Rapprocher ventes couvertes et ventes totales. Un rapport de marge peut omettre des ventes sans coût enregistré à la vente. |
| Acquisition | Spend, revenu attribué, commandes et nouveaux clients, canal, fenêtre et modèle | Vérifier assiette et couverture. Les dépenses Meta ou Google peuvent nécessiter un export distinct. |

Paginer rapports, commandes et lignes imbriquées jusqu’à fin confirmée. Dédupliquer sur identifiants d’événement et de ligne. Sur erreur ou curseur répété, garder le sous-ensemble observé et annoncer la limite. Compter séparément commandes, lignes et événements. Agréger chaque source à son grain avant jointure pour éviter de multiplier le transport par le nombre de lignes. Conserver les filtres de statut, marchés, canaux, dates et devise pour la réconciliation.

Pour tout coût, consigner montant, unité, contenu, date de validité, source, destination/transporteur ou moyen de paiement pertinent. Un coût rendu entrepôt incluant achat, droits et transport amont remplace ces trois postes. Demander d’abord « Le coût unitaire inclut-il déjà le transport amont et les droits ? » seulement si le chevauchement est matériel. Ensuite cibler la décision : coût transport par destination pour une offre de livraison, taux et fixe par transaction pour un prix plancher, dépenses du canal pour un résultat après acquisition. Les abonnements et frais logistiques mensuels appartiennent aux charges fixes sauf part facturée à l’usage. Garder ce registre dans le contexte de travail ; annoncer une sauvegarde seulement si effectivement réalisée.

Sources métier : [rapports de ventes Shopify](https://help.shopify.com/en/manual/reports-and-analytics/shopify-reports/report-types/default-reports/sales-report) et [rapports de marge Shopify](https://help.shopify.com/en/manual/reports-and-analytics/shopify-reports/report-types/default-reports/profit-reports).
