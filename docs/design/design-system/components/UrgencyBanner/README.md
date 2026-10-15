# UrgencyBanner

La zone `sc-urgent` liste les bugs urgents ouverts, ainsi que ceux corrigés ou rejetés depuis moins de 48 h. **Il n'y a pas de carte englobante** : un titre en rouge (`danger-ink`), puis une carte par urgence, empilées. On évite ainsi les cartes dans les cartes.

**Le consommateur fournit** : le nombre d'urgences, puis une ligne `sc-urgent__row` par urgence, avec le titre, l'auteur et la date de la déclaration, le badge d'état et la date du dernier changement d'état.

- **Place** : sous la rangée de tuiles, **en pleine largeur**, pour rester lisible même avec une dizaine d'urgences. Sans urgence, elle **disparaît**.
- **Chaque ligne** :
  - à gauche, le titre prend toute la largeur restante et passe sur plusieurs lignes si nécessaire. La déclaration est **toujours en dessous** du titre ;
  - à droite, les badges « Urgent » et l'état sont **toujours en haut**, à la même place, et ne se centrent jamais verticalement. La date du dernier changement d'état s'affiche sous les badges.
- **Ordre** : en qualification, puis confirmées, puis corrigées ou rejetées.
- **États** : *En qualification* (`--danger`), *Confirmée, en correction* (`--active`), *Corrigée* (`--done`), *Pas un dysfonctionnement* (`--planned`).
- On n'affiche que des faits, aucun délai promis. Une ligne s'ouvre au clic ou avec Entrée, sur le side panel de détail.
