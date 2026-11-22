# Shopify Conversion Doctor

Connectez votre boutique Shopify à une IA compatible disposant de la lecture des produits. Ce dossier fournit ensuite la méthode pour auditer vos fiches, choisir lesquelles retravailler et préparer de nouveaux textes. Il fonctionne entièrement en Markdown. Chaque audit se termine par les modifications proposées. Si votre connecteur permet l’écriture, le choix Oui lance leur application et Non clôt l’audit. Une interface sans dialogue recueille votre réponse dans le chat.

## Démarrer

1. Activez le connecteur Shopify officiel dans le répertoire d’apps ou d’intégrations de votre assistant, lorsqu’il est proposé pour votre compte. Sélectionnez la boutique et accordez la lecture des produits dans le parcours officiel. Si votre organisation gère les accès, demandez cette autorisation à son administrateur.
2. Chargez le dossier selon votre assistant. Conservez les sous-dossiers avec le fichier principal.
3. Demandez « Utilise Shopify Conversion Doctor pour auditer mes 20 premières fiches. » L’assistant vérifie la lecture et indique le tri, le nombre de fiches examinées et les limites de l’audit.

| Environnement | Installation ou adaptation |
|---|---|
| Claude Code | Décompressez le dossier dans `.claude/skills/` à la racine du projet. Ouvrez le projet et invoquez `/shopify-conversion-doctor`. Pour une interface Claude proposant l’import de skills, utilisez le ZIP dans cette interface. Vérifiez que le connecteur est disponible dans la même session. |
| Codex | Décompressez le dossier sous `.agents/skills/` dans votre projet. Ouvrez le projet et invoquez `$shopify-conversion-doctor`. Vérifiez que les outils Shopify y ont accès aux produits du marchand. |
| ChatGPT | Si votre espace propose l’app Shopify officielle et la lecture du catalogue marchand, activez-la dans la conversation. Joignez SKILL.md et les cinq fichiers de references/ comme documents, puis collez l’instruction ci-dessous. Cette méthode utilise les fichiers comme contexte. |

**Instruction à copier pour ChatGPT**

> Applique le fichier Shopify Conversion Doctor joint et consulte les cinq références par leur nom de fichier. Vérifie d’abord que l’app Shopify officielle de cette conversation peut lire les produits de ma boutique. Applique la procédure de blocage du skill si nécessaire. Présente la liste finale et demande mon accord avant toute écriture. Ma demande est la suivante : « Quels produits dois-je optimiser ? »

## Choisir sa demande

- « Analyse toute ma boutique Shopify. » Pour un bilan et un plan d’action.
- « Quels produits dois-je optimiser ? » Pour une liste de priorités justifiées.
- « Audite mes 20 premières fiches. » Pour commencer par un lot borné.
- « Identifie les problèmes SEO. » Pour examiner les métadonnées et les doublons.
- « Réécris mes descriptions produits. » Pour obtenir des propositions par ID.
- « Classe mes fiches de la moins bonne à la meilleure. » Pour comparer les scores à couverture équivalente.

Le score mesure la qualité éditoriale observable. La couverture indique combien de critères ont pu être vérifiés. Une fiche avec peu de données peut donc obtenir un score élevé et une confiance faible. Les performances commerciales nécessitent des mesures distinctes.

Consultez les [deux exemples de rapports](examples/catalog-audit.md), le [protocole de validation](tests/test-cases.md) et le [point d’entrée du skill](SKILL.md).

Documentation de référence : [Agent Skills](https://agentskills.io/specification), [Claude Code](https://code.claude.com/docs/en/skills), [Codex](https://developers.openai.com/codex/skills/).
