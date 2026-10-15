# Field

Les éléments de formulaire, utilisés dans les side panels, l'onboarding et l'espace admin : `sc-field` (libellé, contrôle, aide), `sc-input`, `sc-select`, `sc-check`, `sc-radio` et `sc-files` / `sc-file`.

**Le consommateur fournit** : un `<label for>` relié à chaque contrôle par son `id`, la valeur, et un texte d'aide ou d'erreur s'il y a lieu.

- **Champ** : `sc-input` sur un `<input>` ou un `<textarea>`, avec un contour `border-control` (3:1) et un anneau de focus `focus`. Le placeholder montre un exemple (« Ex. : ce matin vers 9 h »), jamais la consigne.
- **Liste déroulante** : le `<select class="sc-input">` est placé dans un `<span class="sc-select">` avec l'icône Tabler `chevron-down`. Il a 40px de padding à droite, pour que le chevron ne touche pas la bordure. Le menu déroulant natif ne se stylise pas : dans le produit, on utilise le Select de shadcn (Radix), qui reprend ces tokens.
- **Case et radio** : `sc-check` et `sc-radio`, dessinés par le design system et non plus par le navigateur. Cochés, ils prennent `primary`. Dans une carte de choix (`sc-choice`), le radio coché prend la couleur de la carte.
- **Erreur** : un texte `sc-help` en `danger-ink` sous le champ, qui dit comment corriger (« Saisissez une adresse email complète »).
- **Fichiers joints** : les `sc-file` se placent en ligne et passent à la ligne si besoin (`sc-files`). Chacun porte une vignette (`sc-thumb`), le nom et un bouton croix pour le retirer, avec un `aria-label` « Retirer … ». Dans le détail d'un ticket, les captures s'affichent en vignettes plus grandes (`sc-thumb--lg`).
