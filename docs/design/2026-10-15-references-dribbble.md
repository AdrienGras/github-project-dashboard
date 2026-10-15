# Références visuelles : synthèse Dribbble

Recherche faite le 2026-10-15, pour la phase visuelle de la [PRD](../superpowers/specs/2026-10-15-dashboard-client-gh-projects-design.md). Les captures restent en local (`.superpowers/`, ignoré par git), parce que les visuels appartiennent à leurs auteurs. Ce document ne contient que des liens et notre analyse.

## Références retenues

| Référence | Ce qu'on prend | Ce qu'on évite |
|---|---|---|
| [Teamwork.com, Project Timeline View](https://dribbble.com/shots/25439137-Teamwork-com-Project-Timeline-View) (Ivo Ivanov) | Barres pastel saturées, avec le libellé et la durée lisibles dans la barre. Regroupement des lignes par section. | Une couleur par tâche sans signification : chez nous, la couleur porte le type ou l'état. |
| [Dashboard, Gantt Chart](https://dribbble.com/shots/23913594-Dashboard-Gantt-Chart) (Rama Zuldi / Odama) | Grille tableau + Gantt : colonne de gauche avec le % et une mini-barre de progression par ligne, semaines en en-tête. | La densité, le menu d'édition et l'arborescence des tâches, qui relèvent d'un outil de chef de projet. |
| [HR Management, My Absence](https://dribbble.com/shots/25318939-HR-Management-My-Absence) (Michal Muller / Afternow) | Rangée de tuiles récapitulatives pastel, une teinte par catégorie. Pastilles icône + texte pour le type et le statut. Toast de confirmation. | Le côté un peu sage : on ajoute de la profondeur (ombres douces, dégradé sur l'action principale). |

## Références d'appoint (détails précis)

| Référence | Détail repris |
|---|---|
| [Monograph Shareable Gantt](https://dribbble.com/shots/7115467-Monograph-Shareable-Gantt) | Une vue Gantt *faite pour le client* : peu de lignes, jalons posés sur les barres, infobulle de jalon, ligne « aujourd'hui ». |
| [Timeline View, Task Management](https://dribbble.com/shots/23919900-Timeline-View-Task-Management-Dashboard) (BTA Studio) | Sélecteur Jour / Semaine / Mois, navigation par période, marqueur sur la ligne « aujourd'hui ». |
| [Booking Timeline Calendar](https://dribbble.com/shots/11021862-Booking-Timeline-Calendar) | Zones hachurées, reprises pour le retard. Carte de détail flottante au survol. |
| [Stepper-driven intake](https://dribbble.com/shots/27486078-Stepper-driven-intake-with-a-live-updating-summary-sidebar) | Indicateur d'étapes en pastilles, pour le parcours bug/urgence en 5 étapes. |
| [Slideout menu, Untitled UI](https://dribbble.com/shots/27698497-Slideout-menu-Untitled-UI) | Le modèle de side panel : en-tête avec une icône en pastille, validation inline, pied de panneau fixe Annuler / Valider. |

Références écartées : ChronoTask (Outcrowd), Flow AI (Raj Singh) et Roadmap v2 (Val Pieŭnioŭ). Elles sont plus « effet verre et dégradés », et ce n'est pas la direction retenue. La grille « shadcn dashboard » est surtout monochrome, ce qui confirme que shadcn brut est trop froid pour l'effet recherché.

## Direction retenue

**Pratique et coloré, la couleur porte le sens.** On part de la base shadcn, modernisée ainsi :

- **Couleurs sémantiques en pastel saturé** : Sujet en bleu, Bug / urgence en rouge, Idée en ambre, plus les états (planifié, en cours, en recette, livré, en retard). Tous les couples texte / fond sont conformes AA.
- **Le dégradé de marque** est réservé à l'action principale et au remplissage des barres de progression.
- **La profondeur** passe par des ombres douces à plusieurs couches, et des hachures pour le retard.
- **Deux thèmes** : clair par défaut, sombre qui suit le système, plus un bouton pour basculer. Le sombre a ses propres teintes de barres (plus profondes, texte clair), ce n'est pas une inversion du clair.
- **Agencement de l'écran client** :
  1. accueil avec le nom de l'utilisateur et les deux boutons d'action ;
  2. 4 tuiles récapitulatives (En cours · Planifiés · Urgences · Livrés ce mois) ;
  3. bandeau urgences ;
  4. carte Gantt (tableau à gauche avec le %, barres pastel, jalons, contrôles de zoom et de période) ;
  5. deux colonnes, « Non planifié » et « Idées ».

  Les formulaires utilisent un Sheet shadcn à étapes.
