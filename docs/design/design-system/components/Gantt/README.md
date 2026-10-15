# Gantt

La carte Gantt est l'écran principal du client. À gauche, un tableau avec le titre, le type et l'avancement, à la manière d'Odama. À droite, des barres **colorées selon l'état**, à la manière de Teamwork, avec la couleur qui porte un sens.

**Le consommateur fournit** : la période affichée et son nombre de colonnes (`--cols`), la position de la ligne « aujourd'hui » en %, et pour chaque item visible du Gantt (règle 3 de la PRD) :
- le titre et le type ;
- l'état canonique ;
- le début et la fin, convertis en `left` et `width` (%) ;
- la complétion (`--p`) et le compteur N/M ;
- la date de livraison ;
- en option : la date d'engagement (pour le décalage), le dépassement (pour le retard) et les jalons.

## Règles visuelles

- **Ligne de la colonne de gauche, sur trois niveaux** (hauteur 76px) :
  1. le titre, sur une seule ligne, avec points de suspension et le titre complet en infobulle ;
  2. les étiquettes : type, état, puis « En retard » ou « Décalé de N j » s'il y a lieu ;
  3. l'avancement : mini-barre, %, N/M, date courte.

  Aucun texte ne passe à la ligne de façon imprévue.
- **Barre** : `sc-bar--planned | --active | --review | --done | --late`, suivant l'état. Le libellé dans la barre reprend l'état, avec le % pour les états en cours. Un liseré de 3px en bas, à la couleur `*-strong`, montre la complétion.
- **Retard** : `sc-bar--late`, plus une zone `sc-overdue` hachurée, de la fin prévue jusqu'à aujourd'hui. Dans la colonne de gauche, l'étiquette « En retard » répète l'information en toutes lettres.
- **Décalage** (si le réglage de l'instance l'active) : un contour `sc-ghost` en pointillés `warning-strong`, aux dates d'engagement, sur lequel la barre courante se superpose (c'est la « baseline » des Gantt classiques). Une puce `sc-slipchip` « +N j » se place juste après la fin de la barre, et l'étiquette « Décalé de N j » apparaît dans la colonne de gauche.
- **Aujourd'hui** : une ligne `sc-today` de 2px en `active-strong`, et la colonne de la semaine en cours surlignée (`is-now`).
- **Jalon** : un losange `sc-milestone` en `ink`, avec son nom et sa date en infobulle, et répétés dans la colonne de gauche.
- **Tâches techniques** : jamais affichées. Seuls le compteur N/M et le % apparaissent.
- **Ordre des lignes** : par date de livraison croissante. Les livrés restent en tête de leur période.

## Comportement

- **Échelle** : segmenté Semaine / Mois / Trimestre (`sc-seg`). Navigation : boutons icône compacts ‹ ›, et « Aujourd'hui » en `sc-btn--sm`. La vue par défaut est Mois, centrée sur aujourd'hui.
- Cliquer une barre ou une ligne (ou appuyer sur Entrée) ouvre le side panel de détail.
- Sur mobile, sous 720px, la colonne de gauche passe au-dessus de chaque barre. La piste défile horizontalement dans la carte, jamais la page.
