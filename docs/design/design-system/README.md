Système visuel du dashboard client branché sur GitHub Projects. On y lit, en un coup d'œil, où en sont ses sujets (Gantt), et on y déclare un bug, une urgence ou une idée. La base est shadcn/ui, rendue chaleureuse et lisible par trois leviers : **la couleur porte le sens**, **un seul dégradé**, et **de la profondeur douce**. Il existe deux thèmes, clair (par défaut) et sombre, tous deux conformes WCAG AA.

## Contenu et ton

- Écrire en **français**, au **vouvoiement**, du côté du client : « Signaler un bug », « Proposer une idée », « Livraison prévue le 30 oct. ».
- **Aucun jargon GitHub** à l'écran : pas d'issue, de sub-issue, de Triage, de PR ou de Closed. On utilise le vocabulaire de la PRD : Sujet, Bug, Idée ; Planifié, En cours, En recette, Livré, En retard ; En qualification, Confirmée, Corrigée.
- **Des faits, pas de promesses** : « Déclarée il y a 40 min », jamais « Traitée sous 4 h ».
- Les **libellés de boutons** disent ce qui se passe : « Envoyer la déclaration », jamais « OK ».
- Les dates sont courtes et en français : « 30 oct. », « 2 nov. ». Les pourcentages s'écrivent avec une espace insécable : « 62 % ».
- **Pas d'emoji** dans l'interface. Les icônes font ce travail.

## Couleur

- Le fond de page est `bg`. Cartes, Gantt et side panel sont sur `surface`. Les en-têtes de tableau et les zones calmes sont sur `surface-muted`.
- Le texte est en `ink`, le secondaire en `ink-muted`. Les deux atteignent 4.5:1 sur `bg`, `surface` et `surface-muted`, dans les deux thèmes.
- **La couleur ne décore jamais, elle signifie.** Six familles, chacune déclinée en `-soft` (fond de pastille), `-ink` (texte sur `-soft` et `-bar`), `-bar` (barre de Gantt) et `-strong` (liseré, icône) :
  - `planned` : Planifié, En réflexion, Écarté
  - `active` : En cours, Confirmée, icône Sujet, ligne « aujourd'hui »
  - `review` : En recette
  - `done` : Livré, Corrigé, Réalisée
  - `danger` : Bug, Urgent, En retard, En qualification
  - `idea` (cyan) : Idée, Proposée. Une idée n'est jamais présentée comme un avertissement.
  - `warning` (ambre) : décalage de date, et rien d'autre
- **Le dégradé** `cta-urgent-from` → `cta-urgent-to` (du rouge au cramoisi) n'existe que sur le bouton « Signaler un bug / une urgence ». Aucun autre dégradé. « Proposer une idée » prend le rendu de `primary`.
- Pas de carte dans une carte : une zone qui regroupe des cartes (urgences, listes) n'a qu'un titre, pas de fond ni de contour.
- Les boutons principaux neutres sont en `primary` avec `on-primary`. Ils inversent en sombre : clair sur fond sombre.
- **Une couleur n'est jamais seule** : un état a toujours un libellé, et une icône dès qu'il faut le lire vite. C'est ce qui rend l'interface lisible pour les daltoniens.
- Les contours de champs utilisent `border-control` (3:1). `border` et `border-strong` sont décoratifs.
- **Focus** : anneau plein `focus` de 2px, décalé de 2px, sur tout élément interactif.

## Typographie

- `display` (Bricolage Grotesque) sert **une seule fois par écran**, pour l'accueil « Bonjour Julie ». Les titres de cartes et de panneaux sont en `title`, dans la même famille.
- Tout le reste est en Figtree : `heading` pour les titres d'items, `body` pour le texte courant, `small` pour les méta, `caption` pour les pastilles et les barres, `label` pour les en-têtes en capitales.
- Les chiffres (pourcentages, compteurs, numéros, dates compactes) sont en `data` et `stat` (Geist Mono, chiffres tabulaires), pour que les colonnes restent alignées.

## Espacement, rayons, ombres

- Échelle de 4px : `space-1` à `space-8`. Les cartes ont un padding de `space-6`, les tuiles de `space-4`. Les grandes zones du dashboard sont espacées de `space-8`.
- Rayons : `radius-sm` pour les barres de Gantt, `radius-md` pour les boutons, champs et lignes, `radius-lg` pour les cartes, tuiles et panneaux, `radius-pill` pour les pastilles et segmentés.
- Ombres : `shadow-sm` pour les boutons et les barres, `shadow-md` pour les cartes au repos, `shadow-lg` pour le side panel et les cartes flottantes. Pas d'effet verre, pas de lueur colorée.

## Motifs propres au Gantt

- **Retard** : la barre passe en `danger-bar`, et des hachures `danger-bar` sous un contour en pointillés `danger-strong` vont de la fin prévue jusqu'à aujourd'hui.
- **Décalage** : un contour en pointillés `warning-strong` marque la date d'engagement, avec la puce « +N j » (`warning-soft` / `warning-ink`) après la barre.
- **Aujourd'hui** : une ligne de 2px en `active-strong`, et la semaine en cours surlignée en `active-soft`.
- **Jalon** : un losange en `ink`, avec un contour `surface`.

## Agencement de l'écran client

Du haut vers le bas :
1. **En-tête** : logo et nom du client à gauche. À droite, « Espace admin » (admins seulement), le bouton de thème en bouton icône `--secondary` (avec contour) et le profil dans sa propre pastille.
2. **Accueil** : « Bonjour Julie », puis les boutons Urgence et Idée.
3. **Synthèse** : les 4 StatTile compactes en ligne, puis l'UrgencyBanner en pleine largeur juste dessous (absente s'il n'y a pas d'urgence).
4. **Carte Gantt** : chaque semaine en tête de colonne porte son numéro et sa date.
5. **Deux colonnes** : Non planifié et Idées, en ItemRow.

Un clic sur un item ouvre le SidePanel. La largeur utile est de 1280px au maximum, avec une gouttière de 16px sur mobile.

## Iconographie

- **Tabler Icons**, en version outline : grille de 24px, trait de 2px, extrémités arrondies, couleur `currentColor`. Dans le code, on utilise `@tabler/icons-react` ; les aperçus reprennent les tracés Tabler en ligne.
- **Tailles** : 16px par défaut, 14px dans un bouton compact, 12 à 13px dans une pastille, 20px dans la pastille d'en-tête du side panel.
- **Une icône par concept**, sans variante : Sujet `stack-2`, Bug `bug`, Idée `bulb`, Urgence `alert-triangle`, Planifié `calendar`, En cours `progress`, En recette `eye`, Livré `check`, En retard `clock`, Jalon `flag`, Fermer `x`, Navigation `chevron-left` / `chevron-right`, Ajouter `plus`, Aide `info-circle`, Liste déroulante `chevron-down`, Capture `photo`. Le groupe d'assets « Icons » les contient toutes.
- **Logo** : aucun pour l'instant. Chaque instance affiche le logo et le nom du client, fournis à l'onboarding, à gauche de l'en-tête.
