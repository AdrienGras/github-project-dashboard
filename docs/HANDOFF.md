# Passation : état du projet au 2026-10-15

## Où on en est

| Phase | État |
|---|---|
| Cadrage (PRD) | ✅ validée : `docs/superpowers/specs/2026-10-15-dashboard-client-gh-projects-design.md` |
| Recherche visuelle | ✅ `docs/design/2026-10-15-references-dribbble.md` |
| Design system | ✅ v9, relu par l'UX (Elise) et par Adrien : https://claude.ai/artifact/13HKhxAcpMu96hgvz27VYx (sources : `docs/design/design-system/`) |
| Prototypes des flux | ✅ v13, retours client et backoffice intégrés : https://claude.ai/artifact/MVgRgVc4qRpbEReToXJ84y (sources : `docs/design/flux/`) |
| **Plan d'implémentation** | ⏭️ **prochaine étape** |
| Code | à venir |

Dépôt : https://github.com/AdrienGras/github-project-dashboard (public).

## Décisions d'interface prises après la PRD

Les prototypes font foi sur l'interface. La PRD reste la source pour le fonctionnel, le modèle GitHub et l'architecture.

**Couleurs et style**
- La couleur porte un sens : six familles d'état (planned, active, review, done, danger, idea) et une famille warning.
- **Idée en cyan**, pour ne jamais la confondre avec un avertissement. **L'ambre (warning) est réservé au décalage de date.**
- Le seul dégradé est celui du bouton « Signaler un bug / une urgence ». « Proposer une idée » a le rendu `primary`.
- Les **types** (Sujet, Bug, Idée) sont des étiquettes à contour gris, au rayon court. Les **états** sont des pastilles pleines.
- Thème clair et thème sombre, avec un bouton pour basculer. Tous les couples de couleurs sont conformes AA. Les icônes viennent de Tabler.
- Pas de carte dans une carte.

**Dashboard client** (`Main.dc.html`), de haut en bas :
1. **En-tête** : logo et nom du client, « Espace admin » pour les admins, bouton de thème (icône avec contour), profil dans une pastille.
2. **Accueil** « Bonjour Julie », avec les boutons Urgence et Idée.
3. **4 tuiles compactes en ligne** (icône · libellé et contexte · chiffre), puis les **urgences en pleine largeur dessous** : un titre rouge et une carte par urgence, badges fixés en haut à droite. La zone urgences disparaît s'il n'y en a pas.
4. **Gantt** :
   - colonne de gauche sur 3 niveaux (titre ; type, état et décalage ; avancement) ;
   - numéro et date sur chaque semaine ;
   - barres colorées par état, avec un liseré de progression ;
   - retard en hachures ;
   - décalage en pointillés ambre, avec une puce « +N j » ;
   - jalons ◆.
5. **Non planifié** et **Idées** : lignes sur 2 niveaux, état en haut à droite.

**Détail d'un item** (side panel) : badge de type avec son icône, état et décalage, informations, avancement (compteur seulement), description, captures en vignettes, et commentaires pour les bugs.

**Formulaire bug / urgence**, en 4 étapes :
1. **Impact**, choisi en premier.
2. **Le problème** : titre en une phrase, au-dessus du « Où », environnement, depuis quand, « ça fonctionnait avant ».
3. **Reproduction et captures** : ce qui devrait se passer (texte long), ce qui se passe à la place (texte long, obligatoire), étapes pour reproduire (facultatif), puis dépôt de captures avec vignettes et suppression.
4. **Récapitulatif** de toutes les informations saisies, captures en petites vignettes.

Le titre n'est jamais seul dans une étape. Le sous-titre du panneau reste fixe.

**Formulaire idée** : l'idée en une phrase, le besoin, ce que ça changerait.

**Connexion** : invitation à activer, magic link avec validation de l'adresse et écran « Vérifiez vos emails », lien expiré.

**Espace admin** : menu vertical à gauche, en pleine page.
- **Comptes** : invitation en side panel (nom, email, rôle, handle GitHub), confirmation avant désactivation.
- **Anomalies** : décalé (avec re-baseline), en retard, sans dates, sans estimate.
- **Synchronisation**.
- **Réglages** : afficher ou non les décalages.

**Onboarding**, en 8 étapes :
1. SMTP, avec un test d'envoi.
2. App GitHub par manifest.
3. Project et dépôt de suivi, **créables à la volée**.
4. Provisioning des types, champs et **valeurs de priorité**.
5. Correspondance des statuts et des priorités.
6. Alertes (assigné, Discord, email).
7. Identité.
8. Invitations.

**Champs** (composant Field) : liste avec un chevron qui ne touche pas la bordure, cases et radios dessinées par le design system. Dans le code, le menu déroulant natif est remplacé par le Select de shadcn (point jugé non bloquant par l'UX).

## Points ouverts, à trancher avant de coder

- ⏳ Date d'extinction de Plane.
- ⏳ Client pilote.
- ⏳ Org GitHub **Free** de test pour les spikes (Adrien peut la créer).
- Sur les deux artefacts, les fils de commentaires qui n'ont pas été envoyés à Claude restent ouverts. Ils ont tous été traités et sont à résoudre à la main dans la page.

## Prochaine étape : le plan d'implémentation

Rédiger le plan dans `docs/superpowers/plans/`, avec le skill `superpowers:writing-plans`, à partir de la PRD, du design system et des prototypes. Découpage pressenti :

| Phase | Contenu |
|---|---|
| 0 · Spike GitHub (org Free de test) | App par manifest, webhooks `projects_v2_item` et `sub_issues`, Issue Types en Free, droits de provisioning, `type` à la création, champs et `sub_issues_summary` en GraphQL. **Le résultat décide des branches suivantes** (webhooks ou réconciliation seule ; Issue Types ou champ « Type »). |
| 1 · Socle | Loco figé, SQLite WAL, Docker, auth par magic link en cookie httpOnly, invitations, CLI `create-admin` et `backup`. |
| 2 · Front | React + Vite + shadcn, tokens clair et sombre depuis `tokens.json`, composants du design system. |
| 3 · GitHub | Onboarding, provisioning, synchronisation (webhooks et réconciliation), copie locale en lecture, dates d'engagement. |
| 4 · Dashboard client | Règles de placement (PRD §7.2), Gantt, tuiles, urgences, détail. |
| 5 · Déclarations | Formulaires, pièces jointes (liens non devinables), création des issues, alertes email et Discord. |
| 6 · Admin | Comptes, anomalies, re-baseline, réglages. |
| 7 · Exploitation | CI vers GHCR, `compose` d'exemple, sauvegarde, procédure de mise à jour. |

## Modifier le design system ou les prototypes

- Les artefacts se modifient avec l'outil Artifact, sur leurs URL ci-dessus. Il faut lire `project/design-system.json` ou `project/canvas.json` juste avant de publier l'index.
- Les aperçus du design system se régénèrent avec : `python3 -I docs/design/design-system/build_previews.py docs/design/design-system/assets/Icons docs/design/design-system/components`
- Le canvas embarque une copie du design system (`project/ds/suiviclient/`). Après chaque changement du design system, il faut la recopier en entrées `{"artifact": <url du DS>, "path": ...}` et mettre à jour la version dans `designSystems`.
