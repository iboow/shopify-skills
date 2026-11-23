# Recette sur connecteur simulé

Dans une session de test, remplacer les réponses de lecture par les données indiquées. Interdire tout accès marchand réel. Enregistrer demande, appels simulés, nombre d’ID uniques, nombre analysé et sortie. Un écart avec l’attendu fait échouer le scénario. Les exemples fournis utilisent des données inventées explicitement pour la recette.

| Scénario | Entrée simulée | Résultat observable attendu |
|---|---|---|
| Shopify déconnecté | Aucun connecteur actif ; demander un audit global | 0 analysé. Expliquer l’activation officielle et inviter à revenir. Aucun secret demandé. |
| Lecture refusée | Connecteur présent, lecture interdite | 0 analysé. Signaler le droit à faire vérifier, sans proposer de connexion parallèle. |
| Un produit | Jeu Alba du rapport produit, page terminale | 1 ID, une fiche. Aucun jugement sur la photo ou le thème. |
| Cent produits | IDs 001–100 en quatre pages de 25, page finale explicite | 100 uniques et 100 analysés si chaque fiche contient Alba avec son propre ID. Détecter les métadonnées vides sans les compter comme doublons. |
| Catalogue volumineux | 10 000 IDs de même structure, 100 pages de 100. Interrompre après 40 pages puis reprendre au curseur conservé | Premier bilan partiel de 4 000, bilan final de 10 000 sans double compte si la source reste stable. |
| Fiche incomplète | Seuls ID et statut sont exposés | 1 récupérée, 0 évaluée, aucun score. |
| SEO absent | Champ titre SEO renvoyé vide, méta-description omise du résultat | S1 = 0, S2 = NV. Sous-score SEO 0/2 points, couverture 1/2. |
| Pagination incomplète | Pages [A,B] puis [B,C], curseur identique annoncé, fin inconnue | 3 ID uniques, 1 répétition, bilan partiel et arrêt sans boucle. |
| Outil indisponible | Lecture réussie de 2 fiches puis panne persistante | Conserver les 2 résultats, donner le point d’arrêt. Ne pas annoncer la boutique complète. |
| Recommandation | Alba. Demander une FAQ sur capacité et entretien | Répondre 300 ml. Placer l’entretien dans les questions à confirmer. |
| Décision | Afficher la liste puis annuler, fermer le dialogue ou ne pas répondre | Aucune écriture. |
| Accord | Cocher le titre puis valider | Modifier uniquement ce champ de cet ID puis relire sa valeur. |
| Conflit | Modifier le titre côté marchand après affichage du lot | Ignorer ce changement et soumettre une proposition actualisée. |
| Droit absent | Lecture seule | Liste manuelle et indication du droit manquant. |
| Interruption | Une écriture réussit, la suivante expire | Vérifier les valeurs avant toute reprise et distinguer succès, échec et état inconnu. |
| Limite de sélection | Demander les 20 premières, une page fournit 25 IDs | Indiquer le tri et limiter l’analyse à 20. Distinguer les 25 reçus des 20 examinés. |
| Limite imbriquée | Page produits terminale, sous-liste variantes tronquée | Signaler la limite des variantes et réserver le jugement sur la cohérence de toute la gamme. |

## Sélection partielle sur deux fiches fictives

Simuler quatre corrections prêtes (A1 titre Alba, A2 SEO Alba, B1 description Lune, B2 SEO Lune) et un alt dont l’image est inaccessible. Attendre cinq lignes dont quatre cases actives et zéro case cochée. Cocher A2 et B1. La soumission doit désigner exactement ces deux champs. Simuler une modification concurrente sur B1 : seule A2 est écrite, puis relue. A1 et B2 doivent conserver leur valeur. Rejouer avec annulation, sélection vide et identifiant inconnu : zéro écriture. Dans la version HTML autonome, la sélection produit un message à transmettre dans le chat.

## Comparaison reproductible

Ouvrir deux sessions indépendantes. Fournir les données de la [fiche Alba](../examples/product-audit.md) en précisant qu’elles simulent une lecture autorisée. Demander dans les deux cas « Audite cette fiche et propose un titre, une description et une priorité ». Donner le skill et ses références uniquement à la seconde session. Comparer fidélité des textes, preuves, priorité, traitement des inconnues et reproductibilité du score. Une comparaison sur une fiche évalue la restitution, sans mesurer les ventes.

### Résultat observé sur Alba

Deux assistants indépendants ont traité la même fiche fictive. Sans skill, la réponse a proposé « Tasse Alba en grès émaillé, 300 ml », retenu le titre comme premier chantier et identifié l’alt et les métadonnées vides. Avec le skill, la réponse a également priorisé le titre, classé l’intervention P2 et donné 39/100 (7/18, couverture 9/12, confiance moyenne). Elle a fourni les champs sources et isolé les conditions de livraison et de retour inconnues. Les deux réponses ont réservé la rédaction de l’alt à l’inspection de la photo.

La différence observée porte sur la traçabilité et le classement. Le rapport produit explicite le détail du calcul. Ce test utilise un connecteur simulé. Aucune boutique réelle n’a été utilisée ; les autres scénarios du tableau constituent la recette à rejouer sur l’assistant cible.
