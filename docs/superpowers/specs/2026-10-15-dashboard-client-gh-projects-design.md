# PRD — Dashboard client branché sur GitHub Projects

| | |
|---|---|
| **Statut** | Cadrage validé en session, en attente de relecture finale |
| **Date** | 2026-10-15 |
| **Nom de code** | à définir (« le dashboard » dans ce document) |
| **Phases suivantes** | 1. session design (recherche Dribbble → synthèse → design system → maquettes) · 2. plan d'implémentation, **rédigé une fois le design terminé** · 3. code |
| **Maquette de référence** | `.superpowers/brainstorm/274538-1792062737/content/gantt-v1.html` (filaire : elle valide l'agencement, pas le style) |

Légende : les décisions sans mention ont été prises explicitement en session. Celles marquées *(choix Claude)* ont été tranchées par défaut pendant le cadrage et peuvent être contestées à la relecture. Les décisions laissées au builder sont regroupées en §12.

---

## 1. Contexte et pourquoi

Une partie du suivi projet d'OWLNEXT tourne sur une instance **Plane** ancienne, qu'on ne peut plus mettre à jour ni migrer. Il faut en sortir, avec un double objectif :

- **Côté tech** : l'équipe travaille dans **GitHub Projects**, au plus près du code (issues, sub-issues, PR). GitHub devient la seule source de vérité, sans double saisie.
- **Côté client** : le client dispose d'un **dashboard moderne, attrayant et simple** qui lui montre où en sont ses sujets, sous forme de **Gantt**, et qui lui permet de **déclarer un bug ou une urgence** et de **proposer une idée**.

Le dashboard est un **outil de visualisation et de déclaration**, pas un outil d'échange. Le client regarde et déclare, sans jamais converser dans l'outil.

## 2. Objectifs et critères de succès

À trois mois de la mise en service :

1. **Plane est éteint** pour les clients concernés, à une date fixée (⏳ date à définir).
2. L'équipe tech travaille **uniquement dans GitHub Projects**, sans double saisie.
3. Les urgences et les idées arrivent **majoritairement par le dashboard**, et non plus par email ou téléphone.
4. Les demandes du type « vous en êtes où sur X ? » **diminuent nettement**, parce que la réponse est dans le Gantt.

Le succès dépend autant de la **discipline de l'équipe** (dates à jour, descriptions soignées, cf. §6) que du code.

## 3. Non-objectifs (V1) et anti-objectifs

**Non-objectifs V1**
- Aucun échange avec le client dans l'outil : il ne commente pas, ne répond pas, et ne modifie ni n'annule ses déclarations après envoi *(ce dernier point est un choix Claude)*.
- **Aucune notification au client.** Les seuls emails envoyés sont l'invitation et le magic link. Un module de notifications avancé est prévu en V2.
- Aucun engagement de délai (SLA) affiché, car c'est un sujet contractuel. L'app montre seulement des faits horodatés.
- Pas de dépendances entre sujets sur le Gantt (V2). Pas de calcul automatique des dates à partir des estimates.
- Pas de migration depuis Plane : la reprise est manuelle.
- Pas de supervision des serveurs, déjà couverte par Uptime Kuma et Beszel.
- Pas de multi-client dans une instance.
- Pas de marque blanche au-delà du logo et du nom du client.

**Anti-objectifs** : ce serait un échec même si tout fonctionne.
- **Une fuite d'information interne** vers le client : titres des tâches techniques, commentaires internes, discussions de devs.
- **Un Gantt qui ment** : des dates périmées présentées comme un engagement.
- **De la double saisie** entre le dashboard et GitHub.

## 4. Principes structurants

- **1 instance = 1 client = 1 org GitHub = 1 Project.** L'isolation se fait par l'infrastructure, sans aucun code multi-client.
- **Une image Docker unique** pour tous les clients. Aucun fork par client : tout ce qui varie passe par l'environnement et par l'onboarding admin.
- **GitHub est la source de vérité.** Le dashboard garde une copie locale en lecture, et n'écrit vers GitHub que les déclarations.
- **Toute la qualification se fait dans GitHub**, avec les gestes natifs (déplacer une carte, changer un champ, fermer une issue). L'équipe n'a pas à se connecter au dashboard pour faire son travail courant.
- **Un ticket contient du savoir, pas une conversation.** La description d'un sujet ou d'une idée est la référence que lit le client.

## 5. Utilisateurs et rôles

| Rôle | Qui | Peut |
|---|---|---|
| **Admin** | OWLNEXT (chef de projet du client) | faire l'onboarding, gérer les comptes, régler l'instance, consulter les anomalies, re-baseliner une date, plus tout ce que peut un client |
| **Client** | les personnes côté client | consulter le Gantt, les urgences, le non-planifié et les idées, ouvrir le détail d'un item, déclarer un bug/urgence, proposer une idée |

- Pas d'inscription libre. Un compte se crée **uniquement sur invitation** de l'admin, par **lien à usage unique** et à durée limitée.
- La connexion se fait **par magic link**, sans mot de passe. Le SMTP est donc **obligatoire** sur chaque instance.
- **Premier admin** : la tâche CLI `create-admin` dans le conteneur crée le compte et **affiche un lien de connexion à usage unique**. On peut ainsi se connecter avant d'avoir configuré le SMTP.
- **Profil client** : nom, email, **handle GitHub optionnel**. Le handle sert uniquement de lien dans l'en-tête des issues déclarées. Il ne notifie personne, car le client n'a généralement pas accès aux dépôts privés.
- Un compte peut être désactivé par l'admin.

## 6. Modèle GitHub et process d'équipe

### 6.1 Structure dans l'org du client

Chaque client a **sa propre org GitHub**.

- **Un GitHub Project (v2)** au niveau de l'org, qui agrège des items de **plusieurs dépôts**.
- **Un dépôt « pivot »** sans code (ex. `suivi`), qui reçoit les issues destinées au client : **Sujets, Bugs, Idées**. Toutes les déclarations faites depuis le dashboard y sont créées.
- **Les dépôts de code**, qui contiennent les **Tâches** techniques. Chaque tâche est rattachée en **sub-issue** à un sujet ou à un bug du dépôt pivot, d'un dépôt à l'autre. Les PR des dépôts de code ferment les tâches (`Closes #…`), ce qui fait monter la progression du sujet sans aucune manipulation.
- Les PR et les autres items présents dans le Project sont ignorés par le dashboard.

### 6.2 Issue Types (au niveau de l'org)

| Type | Visible du client | Rôle |
|---|---|---|
| `Sujet` | oui | une fonctionnalité ou un chantier, planifié sur le Gantt |
| `Bug` | oui | un dysfonctionnement, urgent ou non |
| `Idée` | oui | une proposition, qui reste au backlog jusqu'à ce qu'elle soit retenue |
| `Tâche` | **jamais** | le travail technique, en sub-issue |

- **La visibilité se décide par le type, de façon explicite.** Un item sans type visible n'apparaît jamais chez le client, même s'il n'a pas de parent.
- **L'urgence n'est pas un type.** C'est la valeur `Urgente` du champ Priorité d'un Bug, ce qui permet de requalifier sans changer la nature de l'issue.
- **Une idée retenue garde son issue** : l'admin change simplement son type de `Idée` en `Sujet`. Si une idée donne plusieurs sujets, elle est fermée avec la mention « réalisée via #… » et les sujets sont créés à part. Ce cas doit rester rare.
- **Repli** si les Issue Types ne sont pas disponibles sur l'org du client (cf. §11) : un champ Project à choix unique « Type » prend le même rôle. Le code passe par une seule couche qui résout le type, pour ne dépendre d'aucun des deux mécanismes.

### 6.3 Champs du Project

| Champ | Type GitHub | Porté par | Usage |
|---|---|---|---|
| `Status` | choix unique | tous | cycle de vie. Chaque valeur est associée à un **état canonique** à l'onboarding (§6.4) |
| `Priorité` | choix unique | Bugs | la valeur désignée comme « urgente » à l'onboarding place le bug dans le bandeau urgences |
| `Début prévu` | date | Sujets, Bugs planifiés | début de la barre du Gantt |
| `Livraison prévue` | date | Sujets, Bugs planifiés | fin de la barre du Gantt |
| `Estimate` | nombre | Tâches | pondère la complétion |

Les **sub-issues (tâches) doivent être ajoutées au Project**, puisque c'est lui qui porte leur estimate.
Les **jalons** sont les **Milestones du dépôt pivot** (titre et date d'échéance).

### 6.4 États canoniques

L'app raisonne sur un petit jeu d'états fixes. À l'onboarding, l'admin associe chaque valeur de `Status` du Project à l'un d'eux, plusieurs valeurs pouvant tomber sur le même :

| État canonique | Libellé client | Exemple de statuts GitHub associés |
|---|---|---|
| `triage` | À qualifier / Proposée | Triage |
| `backlog` | En réflexion / Backlog | Backlog |
| `planifie` | Planifié | Todo |
| `en_cours` | En cours | In progress, Code review, Bloqué |
| `en_recette` | En recette | QA interne |
| `livre` | Livré | Done |

Une issue **fermée** est dans l'un des deux états dérivés suivants, quel que soit son `Status` :
- `livre` si elle a été fermée en *completed* (libellé client : Livré, Corrigé ou Réalisée selon le type) ;
- `ecarte` si elle a été fermée en *not planned* (libellé client : Écarté, ou « Pas un dysfonctionnement » pour un bug urgent).

### 6.5 Règles de process (à diffuser à l'équipe)

1. **Passage en Planifié = moment de planification** : on découpe le sujet en tâches (sub-issues), on pose les estimates, puis on pose `Début prévu` et `Livraison prévue`. C'est l'admin qui pose les dates, à la main. **Aucun sujet ne passe en Planifié sans ses deux dates.**
2. Les tâches techniques vivent dans les dépôts de code, sont ajoutées au Project et ont un estimate.
3. **La description d'un Sujet ou d'une Idée est le texte lu par le client.** Elle est tenue à jour, et on y consigne le résultat de l'affinage ainsi que la raison d'un abandon. **En V1, on n'y met que du texte** : une image collée dans une issue de dépôt privé ne s'affiche pas chez le client, puisque le lien GitHub exige une session. Les captures passent par les pièces jointes du dashboard. Un proxy d'images pourra être étudié par un spike en V2.
4. **Les commentaires d'un Bug sont visibles par le client**, sauf ceux qui commencent par `[interne]`. Les discussions techniques se font sur les tâches.
5. **Qualification d'une urgence**, entièrement dans GitHub :

| Geste du dev | Ce que voit le client |
|---|---|
| (création par le dashboard : Priorité urgente, état `triage`) | 🚨 Déclarée, en qualification |
| sortir l'item de `triage` | 🚨 Confirmée, en correction |
| fermer l'issue (*completed*) | ✅ Corrigée, visible 48 h dans le bandeau puis retirée |
| baisser la Priorité, avec un commentaire qui explique pourquoi | ↘️ Requalifiée en bug normal, l'item passe en « Non planifié » |
| fermer en *not planned*, avec un commentaire qui explique pourquoi | ✖️ Pas un dysfonctionnement, visible 48 h puis retiré *(durée : choix Claude)* |

## 7. Fonctionnalités

### 7.1 Onboarding admin (assistant au premier lancement)

1. **SMTP** : configuration et envoi d'un email de test. Des valeurs passées par l'environnement peuvent préremplir ou remplacer cette étape.
2. **Connexion GitHub** : l'app crée **sa propre GitHub App** dans l'org du client par le **flux manifest**, avec l'URL du webhook (celle de l'instance), les permissions et les événements préréglés. GitHub renvoie l'app id, la clé privée et le webhook secret, que l'app stocke chiffrés. L'App est ensuite installée sur l'org. **La personne qui fait cette étape doit être owner de l'org client.**
3. **Choix du Project** et du **dépôt pivot**.
4. **Provisioning** : l'app vérifie que les Issue Types, les champs du Project et les valeurs de Status existent. Ce qui manque est créé, ou fait l'objet d'une checklist si les droits ne permettent pas de le créer. Le repli « champ Type » s'active si les Issue Types sont indisponibles.
5. **Correspondance** entre valeurs de `Status` et états canoniques, et désignation de deux valeurs de Priorité : celle qui signifie « urgente » et celle posée sur un bug normal (création, requalification). Toute autre valeur que « urgente » vaut non urgent *(choix Claude)*.
6. **Alertes urgence** : assigné GitHub par défaut, URL du webhook Discord (optionnelle).
7. **Identité** : logo et nom du client.
8. Invitation des premiers utilisateurs.

Toutes ces étapes restent modifiables ensuite depuis les réglages.

### 7.2 Dashboard client (écran principal)

De haut en bas, sur la base de la maquette v1 (`.superpowers/brainstorm/…/gantt-v1.html`) :

- **En-tête** : logo et nom du client, deux actions bien visibles, **« Signaler un bug / une urgence »** et **« Proposer une idée »**.
- **Bandeau urgences**, affiché seulement s'il y a des urgences : les Bugs dont la Priorité est urgente et qui sont ouverts, plus ceux corrigés ou rejetés depuis moins de 48 h. On y voit l'état (§6.5), le déclarant et des horodatages factuels (« déclarée il y a 40 min », « confirmée le… »). Aucun délai promis.
- **Gantt** : une ligne par **Sujet ou Bug qui a ses deux dates** et dont l'état vaut `planifie`, `en_cours`, `en_recette` ou `livre`.
  - **Barre** : de `Début prévu` à `Livraison prévue`, remplie selon la **complétion** (§7.3), avec l'étiquette de l'état.
  - **Ligne « aujourd'hui ».** Zoom semaine, mois et trimestre (rendu détaillé : session design).
  - **Retard** : `Livraison prévue` est dépassée et l'item n'est pas livré. La barre passe en rouge, avec des hachures jusqu'à aujourd'hui.
  - **Décalage** (si le réglage de l'instance l'active, §7.6) : la date d'engagement apparaît en pointillés, avec « décalé de N j ».
  - **Jalons** : les Milestones du dépôt pivot, en losanges ◆.
- **Zone « Non planifié »** : les Sujets et Bugs non urgents qui ne remplissent pas les conditions du Gantt.
- **Zone « Idées »** : *Proposée* (`triage`), *En réflexion* (`backlog`), *Réalisée* ou *Écartée* (fermée, visible 30 jours). Une idée qui passe en Sujet quitte cette zone et suit les règles des Sujets.

**Règles de placement.** Chaque item visible apparaît dans **une seule zone**. Les règles s'appliquent dans l'ordre et la première qui correspond l'emporte *(choix Claude)* :

| # | Condition | Zone | Durée d'affichage |
|---|---|---|---|
| 1 | Bug dont la Priorité est urgente, ouvert ou fermé depuis moins de 48 h | Bandeau urgences | tant qu'il est ouvert, puis 48 h après sa fermeture |
| 2 | Type Idée | Idées | ouverte : sans limite · fermée : 30 jours |
| 3 | Sujet ou Bug ayant ses deux dates, dans l'état `planifie`, `en_cours`, `en_recette` ou `livre` | Gantt | sans limite : le Gantt se parcourt dans le temps, et la vue par défaut est centrée sur aujourd'hui |
| 4 | Tout autre Sujet ou Bug, ouvert. Les dates sont ignorées tant que l'item est en `triage` ou `backlog` | Non planifié | sans limite |
| 5 | Sujet ou Bug fermé hors Gantt (`livre` sans dates, ou `ecarte`) | Non planifié, avec l'étiquette Corrigé ou Écarté | 30 jours |

Un sujet `en_cours` qui n'a pas ses dates tombe dans la règle 4 et remonte dans la vue Anomalies de l'admin.

### 7.3 Complétion d'un sujet

- Elle se calcule sur les **sub-issues directes** de l'item *(choix Claude : pas de récursion en V1)*.
- Si **toutes** les sub-issues ont un estimate : % = somme des estimates fermés ÷ somme des estimates.
- Sinon, on se replie sur le comptage : sub-issues fermées ÷ total.
- On affiche toujours le % **et** « N/M tâches ».
- **« Périmètre ajusté »** : l'app mémorise le total (estimate ou nombre de tâches) au moment de l'engagement (§7.6). Si le total a augmenté depuis, un indicateur s'affiche, avec une infobulle qui explique pourquoi le % a pu reculer.

### 7.4 Détail d'un item (side panel)

Titre, type, état, dates, progression, jalon éventuel, **description** (Markdown rendu), « bloqué par #… » s'il existe une relation de dépendance GitHub et, **pour les Bugs seulement**, les commentaires (hors `[interne]` et hors commentaires automatiques). **Les tâches n'apparaissent que sous forme de compteur et de %, jamais avec leurs titres.**

### 7.5 Déclarations

Les deux formulaires s'ouvrent dans un **side panel**.

**Bug / urgence**, parcours guidé en 5 étapes :
1. Que se passe-t-il ? (titre court)
2. **Impact** : *bloquant pour tous les utilisateurs* / *bloquant pour certains* / *gênant mais contournable*. Les deux premières réponses donnent une **urgence**, la troisième un **bug normal**.
3. Où (URL ou écran, environnement prod ou recette) et depuis quand (est-ce que ça marchait avant ?)
4. Étapes pour reproduire, résultat attendu, résultat constaté
5. Captures ou fichiers (optionnel)

**Idée** : titre, besoin ou problème rencontré, bénéfice attendu, pièces jointes optionnelles *(contenu exact : choix Claude, à affiner en design)*.

**Ce que fait l'envoi** :
- Il crée une issue dans le **dépôt pivot**, avec le type `Bug` ou `Idée`, et l'ajoute au Project avec l'état `triage`. Pour un bug, la Priorité est urgente ou normale selon l'impact. Pour une urgence, l'assigné par défaut est ajouté.
- **Le corps de l'issue** commence par un en-tête fixe (déclarant, email, handle GitHub s'il existe, date, « via le dashboard »), suivi d'une section par question et des liens vers les pièces jointes.
- L'auteur GitHub de l'issue est l'App. **La traçabilité repose donc sur l'en-tête.**
- **Pièces jointes** : l'API GitHub ne permet pas d'attacher de fichiers. Le dashboard les stocke donc sur son volume et insère dans l'issue des **liens non devinables** (capability URLs), consultables sans compte.
- Après l'envoi, l'app relit l'issue créée pour vérifier que le type a bien été posé. GitHub ignore le champ `type` sans erreur si les droits sont insuffisants.

### 7.6 Date d'engagement et re-baseline

- La **date d'engagement** d'un item est la première valeur de `Livraison prévue` observée alors qu'il est dans l'état `planifie` ou un état ultérieur. L'app la mémorise **toujours**, que l'affichage des décalages soit activé ou non, parce que GitHub ne fournit pas facilement l'historique d'un champ de Project.
- Réglage d'instance **« Afficher les décalages »**, activé par défaut.
- L'admin peut **re-baseliner** un item depuis le dashboard, en cas de changement de périmètre négocié : la date courante devient la nouvelle date d'engagement et le total de référence de la complétion est remis à jour.

### 7.7 Alertes à l'équipe (urgences uniquement)

Elles ne partent que pour la création d'un bug **urgent** :
- l'assigné GitHub par défaut (notification native de GitHub) ;
- un **email aux admins** de l'instance ;
- un **webhook Discord**, s'il est configuré, avec le titre, l'impact, le déclarant et le lien vers l'issue.

Les canaux passent par une **interface `Notifier` commune** *(choix Claude)*, pour que Slack, Teams et le module de notifications V2 viennent s'y brancher.

### 7.8 Espace admin

- **Comptes** : inviter, réinviter, désactiver, changer le rôle.
- **Réglages** : tout ce qui est réglé à l'onboarding, plus « Afficher les décalages ».
- **Anomalies** : les items en `planifie` ou dans un état ultérieur sans leurs deux dates, les items en retard, les tâches sans estimate rattachées à un sujet planifié, et l'état de la synchronisation (dernier webhook reçu, dernière réconciliation, erreurs).
- **Re-baseline** depuis le side panel d'un item.

## 8. Règles de visibilité (récapitulatif)

| Élément | Visible par le client |
|---|---|
| Issue de type Sujet, Bug, Idée présente dans le Project | oui |
| Issue de type Tâche, issue sans type visible, PR | non |
| Titres des tâches | non (seulement le compteur et le %) |
| Description d'un Sujet, d'un Bug ou d'une Idée | oui |
| Commentaires d'un Bug | oui, sauf ceux qui commencent par `[interne]` et les commentaires automatiques |
| Commentaires d'un Sujet ou d'une Idée | non |
| Estimates | non, ils ne servent qu'au % |
| Assignés et handles des devs | non *(choix Claude)* |

## 9. Architecture technique

- **Back-end** : **Rust + Loco**, avec une **version figée**. Loco fournit les mailers, les workers, le scheduler, les tâches CLI, les migrations SeaORM et une auth qui inclut le magic link. **L'auth générée par Loco renvoie un JWT : il faut le passer en cookie httpOnly** (pas de `localStorage`), avec une protection CSRF.
- **Front-end** : **React + shadcn/ui (Vite)**, compilé et servi par le binaire depuis la même origine. C'est le starter Loco « SaaS avec rendu côté client ». Le style « shadcn modernisé » est défini en session design.
- **Base** : **SQLite en mode WAL**, fichier dans `/data`. La file des workers Loco utilise elle aussi SQLite, donc pas de Redis.
- **Données locales** :
  - comptes, invitations et jetons de magic link ;
  - config de l'instance, avec les secrets de la GitHub App et du SMTP **chiffrés au repos** par une clé maître passée en variable d'env ;
  - copie de lecture des items GitHub (issues, champs du Project, sub-issues et leur résumé, milestones, commentaires de bugs) ;
  - dates d'engagement et totaux de référence ;
  - métadonnées des pièces jointes, les fichiers eux-mêmes étant dans `/data/uploads`.
- **Synchronisation** :
  - **Webhooks de la GitHub App**, sur les événements `issues`, `sub_issues`, `projects_v2_item`, `milestone` et `issue_comment`. La signature HMAC est vérifiée, l'événement est mis en file, puis un worker relit l'item par GraphQL et met à jour la copie locale.
  - **Réconciliation complète** au démarrage, puis toutes les 10 à 15 min (scheduler), pour rattraper les webhooks perdus.
  - Le dashboard client **ne lit que la copie locale**, jamais GitHub en direct. Les écritures (déclarations) partent vers GitHub, puis la copie est mise à jour.
- **Authentification GitHub** : jetons d'installation de la GitHub App, une App par instance, créée par le flux manifest. L'URL du webhook se met à jour par API (`PATCH /app/hook/config`) si le domaine de l'instance change.
- **Accès à l'API GitHub** : REST pour créer une issue (`type`, `sub_issues_summary`), GraphQL pour les Projects v2 et leurs champs.

## 10. Exploitation

- **Image** : une image unique publiée sur **GHCR**, avec des tags de version.
- **Déploiement** : sur **le serveur de prod du client** que gère OWLNEXT, derrière son Caddy ou son nginx, sur un domaine du client. Le dashboard tourne dans un **conteneur isolé**, sans aucune dépendance à l'application ni à la base du client. Une panne de l'application du client ne doit pas faire tomber le dashboard. La panne du serveur entier est un risque accepté, couvert par la supervision existante.
- **Configuration** : `compose.yml` et `.env` par serveur (`APP_URL`, clé maître, SMTP éventuel). Le tag de version est fixé dans le compose, **sans mise à jour automatique** du type Watchtower.
- **Montée de version** : par l'outillage d'exploitation existant, en lançant la tâche `backup` d'abord. Les migrations s'appliquent automatiquement au démarrage. Toutes les instances restent sur la même version, à quelques jours près.
- **Sauvegarde** : tout est dans le volume `/data`. La tâche CLI `backup` produit un instantané cohérent à chaud (SQLite et uploads). Le volume rejoint les sauvegardes déjà en place sur le serveur.
- **Tâches CLI** : `create-admin` (qui affiche un lien de connexion à usage unique) et `backup`. D'autres sont laissées au builder (resynchronisation forcée, etc.).
- **Langue** : français seulement en V1 *(choix Claude)*.
- **Accessibilité** : thème unique, **conforme WCAG** (niveau AA visé *(choix Claude)*).

## 11. Risques et vérifications préalables (spikes)

Le plan d'implémentation **commence par une phase de spike** sur une org GitHub de test, couvrant les points 2 et 3. Il prévoit des branches conditionnelles selon le résultat : synchronisation par webhooks ou par réconciliation seule, provisioning automatique ou par checklist *(choix Claude)*.

Classés par impact × probabilité :

1. **Discipline de l'équipe**, sans laquelle le Gantt ment ou de l'information fuit. *Mitigation* : la vue Anomalies, les règles de process (§6.5) diffusées à l'équipe, et la règle « pas de Planifié sans dates ».
2. **Capacités de l'API GitHub à confirmer par un spike** avant le plan :
   - les webhooks `projects_v2_item` et `sub_issues` reçus par une GitHub App installée sur l'org ;
   - les permissions nécessaires au provisioning (création d'Issue Types et de champs du Project) et au flux manifest ;
   - la pose du `type` à la création par l'App ;
   - la lecture des champs du Project et de `sub_issues_summary` par GraphQL.
3. **Issue Types sur une org en plan Free** : les orgs clients sont **en plan Free**, et aucune source officielle ne confirme que les Issue Types y sont disponibles. *Mitigation* : le spike se fait sur une **org Free créée pour l'occasion**. Si les Issue Types y fonctionnent, on n'en construit qu'un mécanisme. Sinon, le repli par champ « Type » (§6.2) devient le mécanisme principal. Dans les deux cas, le code passe par une seule couche qui résout le type.
4. **Loco en 0.x**, qui change souvent, et l'adaptation de son auth en cookie. *Mitigation* : version figée, et une auth isolée dans un module.
5. **Liens non devinables vers les pièces jointes** : quiconque a le lien voit le fichier. C'est un risque accepté, puisque les liens ne vivent que dans des issues de dépôts privés.

## 12. Laissé au builder

- Le schéma de base exact, la structure des modules, le choix de la bibliothèque Gantt ou un rendu fait maison (en accord avec la session design).
- Les durées de vie précises (invitation, magic link), les limites des pièces jointes (taille, types de fichiers), la limitation du nombre de demandes de magic link.
- La fréquence exacte de réconciliation, et la stratégie de retry des workers.
- Les tâches CLI supplémentaires.

## 13. Points ouverts (hors spec, à trancher avant le code)

- ⏳ Date cible d'extinction de Plane.
- ⏳ Client pilote.
- ⏳ Résultat du spike sur l'org Free de test : Issue Types, webhooks, permissions.
