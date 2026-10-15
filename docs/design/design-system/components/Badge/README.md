# Badge

Deux marqueurs **visuellement distincts** : l'étiquette de **type** (`sc-type`) dit *ce qu'est* l'item, la pastille d'**état** (`sc-badge`) dit *où il en est*.

**Le consommateur fournit** : le libellé, l'icône Tabler associée et la classe de variante.

- **Type** : un contour gris `border-strong`, un rayon court (`radius-sm`), aucun fond. Seule l'icône est colorée : `--sujet` (stack-2, `active-strong`), `--bug` (bug, `danger-strong`), `--idee` (bulb, `idea-strong`).
- **État** : une pastille pleine et arrondie (`radius-pill`), une famille de couleur par état canonique :
  - `--planned` : Planifié, En réflexion, Écarté ;
  - `--active` : En cours, Confirmée ;
  - `--review` : En recette ;
  - `--done` : Livré, Corrigé, Réalisée ;
  - `--danger` : En retard, En qualification ;
  - `--idea` : Proposée, en cyan, pour ne pas évoquer un avertissement.
- `--solid-danger` (« Urgent ») est le seul badge plein, réservé au bandeau urgences. Son fond est `cta-urgent-from`, avec du texte blanc à 4.5:1 dans les deux thèmes.
- Un décalage de date s'affiche en `warning-soft` / `warning-ink` (« Décalé de 7 j »). L'ambre est réservé aux avertissements.
- **Une couleur n'est jamais seule** : un badge porte toujours un libellé, et une icône pour les états qu'il faut lire vite.
- Le vocabulaire est celui du client défini par la PRD, sans aucun terme GitHub.
