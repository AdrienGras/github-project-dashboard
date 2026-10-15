# ItemRow

Ligne de liste `sc-item`, utilisée dans les cartes **Non planifié** et **Idées** posées côte à côte sous le Gantt.

**Le consommateur fournit** : le titre, l'étiquette de type, une méta factuelle et le badge d'état. Les lignes vivent dans une `sc-card` avec un titre et un compteur.

- **Deux lignes** :
  1. le titre, sur deux lignes au maximum avant les points de suspension ;
  2. le type puis la méta (« Déclaré par Marc D. · 13 oct. »).

  Le badge d'état est en haut à droite, aligné sur la première ligne.
- **Marges** : padding de `space-3` / `space-4`. Pas plus, pour garder des listes denses mais aérées.
- Les items fermés (Corrigé, Écarté, Réalisée) restent 30 jours, en bas de la liste.
- **Liste vide** : « Aucune idée pour l'instant. Proposez la première avec le bouton en haut de page. »
- La ligne entière est cliquable et accessible au clavier. Elle ouvre le side panel de détail.
