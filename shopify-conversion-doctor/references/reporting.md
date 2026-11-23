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

## Confirmation des modifications

Construire la revue à partir de **tous les constats** sur **toutes les fiches analysées**, y compris les priorités secondaires. Avant affichage, rapprocher chaque constat soit d’une ou plusieurs corrections concrètes, soit d’une ligne « À vérifier » avec la donnée ou la capacité manquante. Un simple conseil de réécriture appelle un texte proposé complet lorsque les faits le permettent. La première action du plan ne limite jamais le contenu de la revue.

Une ligne sélectionnable = un produit (ou média/variante identifié), un champ, une valeur actuelle, une valeur proposée. Regrouper les constats qui aboutissent à la même écriture. Afficher priorité et raison. Présenter les alternatives incompatibles comme un choix exclusif ou les résoudre avant validation. Écarter les écritures identiques. Donner à chaque ligne un identifiant stable, unique dans cette revue. Distinguer les corrections éditoriales étayées des promesses à confirmer.

**Interaction.** Ouvrir une boîte de dialogue à sélection multiple, une case initialement vide par correction prête, regroupée par fiche. Afficher les lignes bloquées avec leur motif. Le bouton « Appliquer la sélection (N) » reste inactif à zéro. L’action « Annuler » ou la fermeture clôt la revue sans écriture. Préserver les choix entre pages si la liste est longue. Un simple Oui ou le choix d’un produit ne désigne pas les champs approuvés.

Si l’hôte expose un vrai contrôle multisélection relié à l’assistant, utiliser son résultat soumis. Sinon, générer le panneau à partir de [la boîte de sélection HTML](selection.html), l’intégrer au rapport ou le joindre à côté des scores et l’ouvrir si possible. Remplacer le titre de boutique, l’identifiant unique de revue et les lignes d’exemple. Dupliquer les lignes pour inclure tous les constats. Échapper toute donnée marchande insérée dans le HTML. Le bouton prépare un message à remettre dans le chat. En texte seul, afficher la liste numérotée complète et demander « Quels identifiants veux-tu appliquer ? ». Accepter uniquement les ID explicites et valides de la revue active. En lecture seule, afficher les corrections comme manuelles. Ne proposer aucune écriture si la sélection est vide.

**Application.** Conserver les cibles et valeurs affichées dans la revue. Sur soumission, utiliser seulement les ID sélectionnés et les écritures autorisées du connecteur officiel. Une modification de proposition nécessite une nouvelle validation. Avant chaque écriture, vérifier la boutique, la cible et la valeur actuelle. Ignorer les champs déjà conformes et suspendre les conflits. Préserver les champs non cochés y compris dans une mutation groupée. Utiliser une condition de version si disponible. Relire par ID et par champ ; rendre compte des réussites vérifiées, conflits, échecs et résultats incertains. À la reprise, vérifier les valeurs avant de réessayer.
