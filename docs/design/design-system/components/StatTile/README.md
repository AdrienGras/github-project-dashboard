# StatTile

Tuile récapitulative **compacte**. Elle se lit sur une ligne : pastille d'icône, puis le libellé avec sa ligne de contexte en dessous, puis le chiffre à droite.

**Le consommateur fournit** : la variante de couleur, l'icône Tabler, le libellé, une ligne de contexte factuelle et le chiffre, calculé avec les mêmes règles de placement que les zones de l'écran.

- **Les quatre tuiles**, toujours dans cet ordre : **En cours** (`--active`), **Planifiés** (`--planned`), **Urgences** (`--danger`), **Livrés ce mois** (`--done`).
- **Disposition sur le dashboard** : les quatre tuiles sont **toujours en ligne** sur toute la largeur, en version compacte. Les urgences viennent dessous, en pleine largeur. Elles passent à 2 × 2 sous 760px, puis en colonne sur téléphone.
- La couleur ne porte que sur la pastille d'icône. Aucune tuile n'a de contour coloré, celle des urgences comprise.
- Le chiffre est en style `stat` (mono, chiffres tabulaires). Le contexte tient sur une ligne et se termine par des points de suspension s'il déborde.
- Un clic sur une tuile fait défiler jusqu'à la zone correspondante.
