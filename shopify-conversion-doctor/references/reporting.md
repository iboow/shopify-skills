# Livrer un audit exploitable

Ouvrir par le périmètre, la boutique ou le jeu fictif, les filtres, le tri, les statuts, les pages parcourues, les ID uniques récupérés et le nombre effectivement analysé. Compter comme analysé un ID pour lequel au moins un critère demandé a été examiné. Séparer les échecs et les doublons. Comparer au total annoncé uniquement s’il utilise les mêmes filtres. Sans total, une fin de pagination explicite suffit pour déclarer le périmètre accessible parcouru. Sinon écrire « partiel, total inconnu » ou préciser le total connu.

Pour un audit global, présenter les problèmes récurrents avec leur dénominateur observable, puis une ligne par fiche. Distinguer points forts, faiblesses, problèmes critiques, priorité, confiance et recommandation. Ajouter les textes demandés et un plan d’action avec ordre, responsable suggéré et contrôle d’acceptation. Sur un grand catalogue, fournir le détail en lots ou en fichier et préciser la plage livrée.

Pour « Quels produits optimiser ? », commencer par la file des priorités. Pour « de la moins bonne à la meilleure », suivre les règles de comparabilité du barème. Pour « problèmes SEO », détailler les champs SEO, leurs doublons et leur couverture. Pour « réécris mes descriptions », livrer les suggestions par ID et isoler les faits à confirmer.

Le tableau Markdown convient aux comparaisons courtes. Pour un CSV, utiliser UTF-8, une ligne par ID, des guillemets doubles autour des champs contenant virgule, guillemet ou saut de ligne et doubler tout guillemet interne. Neutraliser les cellules textuelles susceptibles d’être interprétées comme formules à l’ouverture dans un tableur. Si la création de fichier est indisponible, livrer le CSV en bloc de texte.

En-tête proposé :

```csv
id,statut,titre,points,maximum_observable,criteres_evalues,score,priorite,confiance,force,faiblesse,critique,action,texte_propose
```

Modèles remplis : [audit produit](../examples/product-audit.md) et [audit catalogue](../examples/catalog-audit.md).

## Vue visuelle par défaut

Dès qu’un résultat présente des scores, créer et afficher un panneau visuel interactif si l’hôte le permet. Sinon générer un rapport HTML autonome et fournir un lien ouvrable. En environnement texte seul, utiliser un tableau avec barres horizontales. Respecter une demande explicite de CSV ou de texte.

Placer en tête la décision prioritaire et sa justification observée. Présenter chaque produit dans une carte avec score en grand, barre sur une échelle commune de 0 à 100, couverture et confiance libellées. Dans un volet dépliable, inclure points bruts, critères observés et raisons d’incertitude. Afficher « non évaluable » en l’absence de score. Regrouper les limites communes sous les cartes. Une couleur ne doit jamais être le seul porteur de sens. Pour un grand catalogue, utiliser un tableau filtrable et des détails par ligne. Préserver les règles de comparabilité du barème. Échapper les données marchandes insérées dans le HTML. Fournir un rendu responsive, sans dépendance réseau.
