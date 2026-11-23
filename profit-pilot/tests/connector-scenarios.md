# Recette de découverte en lecture seule

Cas de simulation, à rejouer ensuite dans une session marchande autorisée. Pour chaque essai, enregistrer outils réellement exposés, périmètre obtenu et données omises. Ne pas confondre ce protocole avec une certification de connecteur.

| Situation fournie à l’assistant | Comportement attendu |
|---|---|
| Aucun connecteur Shopify | Signaler la connexion absente, indiquer l’intégration compatible dans les réglages, demander de revenir après autorisation. Aucun chiffre marchand. |
| Catalogue visible, commandes refusées | Vérifier l’échec de lecture ; simuler uniquement sur données annoncées. Ne pas extrapoler les commandes. |
| GraphQL absent mais rapport natif suffisant | Utiliser le rapport natif et ses définitions. |
| Première page de 25 commandes, curseur bloqué | Bilan partiel sur les ID uniques ; empêcher une conclusion sur le mois entier. |
| 100 € de ventes ; rapport de marge limité à 60 € de ventes et 18 € de coût | Marge du sous-ensemble 42 € ; couverture 60 % du CA. Marge globale inconnue. |
| Achat rendu 30 €, dont import 4 €, table logistique recensant aussi cet import | COGS 30 €, une seule occurrence des 4 €. |
| Variante actuellement à 12 €, historique inconnu | Marge historique indéterminée ; proposer un scénario estimé à 12 € séparé. |
| Remboursement ligne de septembre enregistré en octobre | Sur période d’événements, imputer le mouvement en octobre. Sur cohorte septembre, préciser la date d’arrêt. |
| Marketing limité aux clics | Ne pas en déduire la dépense ni le revenu attribué. Demander un export du canal si nécessaire. |
| Dépenses connues, aucun acheteur distinct identifié | CPA si commandes attribuées connues ; CAC indisponible. |
| Deux marchés, remise et port taxés différemment | Utiliser les taxes par ligne et la bonne devise ; suspendre le total consolidé si le change manque. |
| Demande ciblée « baisse de 10 % sur ce SKU » | Vérifier l’accès, lire le seul SKU et les coûts associés. Ne pas paginer tout le catalogue. |
| Demande de publier le prix simulé | Livrer le scénario financier ; zéro opération d’écriture. |

## Essais réalisés

Une session indépendante a reçu deux descriptions de capacités simulées. Sans connecteur ni export, elle a conclu « résultat indisponible » et indiqué l’activation de la lecture ou la fourniture d’un export. Avec le rapport couvrant 60 € sur 100 € et 18 € de COGS, elle a calculé 42 € de marge sur le sous-ensemble, 70 % de marge sur les ventes couvertes et 60 % de couverture du CA. Elle a isolé les 40 € de ventes sans coût et les charges inconnues. Les autres lignes constituent des scénarios de recette à rejouer sur la plateforme cible. Aucun test ne s’est connecté à une boutique réelle.
