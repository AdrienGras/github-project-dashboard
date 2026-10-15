# Button

Bouton d'action en cinq variantes (`sc-btn--primary`, `--secondary`, `--ghost`, `--urgent`, `--idea`). Chacune existe en taille **normale (38px)** et **compacte (30px, `sc-btn--sm`)**, et en **bouton icône carré** (`sc-btn--icon`).

**Le consommateur fournit** : un `<button type="button">` (ou un `<a>`), son libellé et, en option, une icône Tabler `svg.sc-icon` placée avant le texte. Un bouton icône n'a pas de texte visible, il porte donc obligatoirement un `aria-label`.

- `--urgent` est réservé à **« Signaler un bug / une urgence »**, une seule fois par écran. Son dégradé va du rouge (`cta-urgent-from`) au cramoisi profond (`cta-urgent-to`), avec un léger reflet en haut. C'est le seul dégradé de l'interface.
- `--idea` est réservé à **« Proposer une idée »**. Il prend le rendu de `primary` (encre), parce que proposer une idée est une action principale et non un avertissement : il ne faut jamais utiliser de jaune ou d'ambre ici.
- `--primary` sert à valider un formulaire, une seule fois par side panel. `--secondary` sert à la navigation, `--ghost` à annuler ou fermer.
- **Taille compacte** : pour les barres d'outils et les en-têtes de carte. « Aujourd'hui » et les flèches de période du Gantt sont en `--sm`. Dans un même groupe, on ne mélange jamais les deux tailles.
- **Bouton icône** : précédent et suivant (chevrons), fermer (croix). Il est carré, en 38px ou en 30px avec `--sm`.
- Le libellé dit ce qui se passe (« Envoyer la déclaration »). Pendant l'envoi, le bouton passe en `disabled` avec le libellé « Envoi… ».
- Le focus clavier affiche l'anneau `focus` de 2px, à ne jamais retirer.
