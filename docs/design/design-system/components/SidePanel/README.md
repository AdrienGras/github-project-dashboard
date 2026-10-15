# SidePanel

Le panneau latéral `sc-sheet` (le Sheet de shadcn) s'ouvre à droite. Il sert à trois usages : le **détail d'un item**, la **déclaration d'un bug ou d'une urgence**, et la **proposition d'une idée**.

**Le consommateur fournit** : l'icône en pastille de l'en-tête, le titre, la description courte, le contenu du corps, et les actions du pied de panneau. Pour un formulaire, il fournit aussi l'étape courante.

- **En-tête** : une icône en pastille (`sc-sheet__chip`, Bug en rouge, Idée en cyan, détail selon le type), le titre en style `title`, et le bouton Fermer en bouton icône `--ghost --icon --sm`.
- **Formulaire à étapes** : l'indicateur `sc-steps` place le libellé « Étape N sur 5 · Nom » **au-dessus** des barres (`sc-steps__bars`). Les barres se partagent la largeur, quel que soit le nombre d'étapes, et montrent les étapes faites (`is-done`) et l'étape courante (`is-current`). Le parcours bug suit les 4 étapes de la PRD : **Impact** d'abord, puis Le problème (titre, où, depuis quand), Reproduction et captures, Récapitulatif. Le titre n'est jamais seul dans une étape : un champ isolé pousse le client à tout y écrire.
- **Description** : elle reste fixe. Le texte saisi par le client ne vient jamais la remplacer.
- **Champs** : ceux du composant Field (`sc-input`, `sc-select`, `sc-check`), jamais les contrôles natifs du navigateur.
- **Choix d'impact** : les cartes radio `sc-choice` portent un titre et une explication. Le choix sélectionné prend `danger-soft`. Quand l'impact choisi est bloquant, le message `sc-hint` annonce que l'équipe sera alertée. Son texte va dans **un seul `<span>`**, pour former une phrase continue même avec des passages en gras.
- **Pied de panneau** : il reste fixe en bas. On y trouve « Étape précédente » en `--secondary` et l'action suivante en `--primary` (« Continuer », puis « Envoyer la déclaration »).
- **Fermeture** : par Échap, par le clic à l'extérieur, ou par le bouton Fermer. Un brouillon de formulaire est conservé jusqu'à l'envoi.
- **Mobile** : le panneau occupe toute la largeur, sans arrondi.
- **Détail d'un item** : description en Markdown rendu, dates, progression (compteur N/M seulement, jamais les titres des tâches) et, pour un Bug, ses commentaires.
