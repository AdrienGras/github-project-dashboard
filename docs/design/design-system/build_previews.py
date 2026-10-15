"""Génère les preview.html du design system Suivi Client : une source par composant, rendue en clair puis en sombre."""
import re, sys, pathlib

TABLER = pathlib.Path(sys.argv[1])
COMP = pathlib.Path(sys.argv[2])

def inner(name):
    svg = (TABLER / f"{name}.svg").read_text()
    paths = re.findall(r"<(?:path|circle|rect|line|polyline)[^>]*/>", svg)
    return "".join(p for p in paths if 'stroke="none"' not in p)

def ic(name, cls="sc-icon", style=""):
    st = f' style="{style}"' if style else ""
    return f'<svg class="{cls}" viewBox="0 0 24 24" aria-hidden="true"{st}>{inner(name)}</svg>'

SUJET, BUG, IDEE, ALERT = "stack-2", "bug", "bulb", "alert-triangle"
def tsujet(): return f'<span class="sc-type sc-type--sujet">{ic(SUJET)}Sujet</span>'
def tbug(): return f'<span class="sc-type sc-type--bug">{ic(BUG)}Bug</span>'
def tidee(): return f'<span class="sc-type sc-type--idee">{ic(IDEE)}Idée</span>'
def badge(kind, label, icon=None):
    return f'<span class="sc-badge sc-badge--{kind}">{ic(icon) if icon else ""}{label}</span>'

P = {}

P["Button"] = ("Actions", 470, "Tailles normale et compacte, boutons icône", lambda: f'''
<div class="sc-root" style="padding:20px 20px 24px;background:var(--bg);display:flex;flex-direction:column;gap:14px">
  <span class="sc-steps"><span>Normal · 38 px</span></span>
  <div style="display:flex;flex-wrap:wrap;gap:8px;align-items:center">
    <button class="sc-btn sc-btn--urgent" type="button">{ic(ALERT)}Signaler un bug / une urgence</button>
    <button class="sc-btn sc-btn--idea" type="button">{ic(IDEE)}Proposer une idée</button>
    <button class="sc-btn sc-btn--secondary" type="button">Étape précédente</button>
    <button class="sc-btn sc-btn--ghost" type="button">Annuler</button>
    <button class="sc-btn sc-btn--primary" type="button" disabled>Envoi…</button>
  </div>
  <span class="sc-steps"><span>Compact · 30 px (barres d'outils, en-têtes de carte)</span></span>
  <div style="display:flex;flex-wrap:wrap;gap:8px;align-items:center">
    <button class="sc-btn sc-btn--urgent sc-btn--sm" type="button">{ic(ALERT)}Signaler</button>
    <button class="sc-btn sc-btn--idea sc-btn--sm" type="button">{ic(IDEE)}Idée</button>
    <button class="sc-btn sc-btn--secondary sc-btn--sm" type="button">Aujourd'hui</button>
    <button class="sc-btn sc-btn--ghost sc-btn--sm" type="button">Réinitialiser</button>
  </div>
  <span class="sc-steps"><span>Bouton icône · carré, libellé en aria-label</span></span>
  <div style="display:flex;flex-wrap:wrap;gap:8px;align-items:center">
    <button class="sc-btn sc-btn--secondary sc-btn--icon" type="button" aria-label="Période précédente">{ic("chevron-left")}</button>
    <button class="sc-btn sc-btn--secondary sc-btn--icon" type="button" aria-label="Période suivante">{ic("chevron-right")}</button>
    <button class="sc-btn sc-btn--ghost sc-btn--icon" type="button" aria-label="Fermer">{ic("x")}</button>
    <button class="sc-btn sc-btn--secondary sc-btn--icon sc-btn--sm" type="button" aria-label="Période précédente">{ic("chevron-left")}</button>
    <button class="sc-btn sc-btn--secondary sc-btn--icon sc-btn--sm" type="button" aria-label="Période suivante">{ic("chevron-right")}</button>
    <button class="sc-btn sc-btn--ghost sc-btn--icon sc-btn--sm" type="button" aria-label="Fermer">{ic("x")}</button>
  </div>
</div>''')

P["Badge"] = ("Statut", 420, "Types (contour, rayon court) et états (pastille pleine)", lambda: f'''
<div class="sc-root" style="padding:20px;background:var(--bg);display:flex;flex-direction:column;gap:12px">
  <span class="sc-steps"><span>Type · ce qu'est l'item</span></span>
  <div style="display:flex;flex-wrap:wrap;gap:8px">{tsujet()}{tbug()}{tidee()}</div>
  <span class="sc-steps"><span>État · où il en est</span></span>
  <div style="display:flex;flex-wrap:wrap;gap:8px">
    {badge("planned","Planifié","calendar")}{badge("active","En cours","progress")}{badge("review","En recette","eye")}{badge("done","Livré","check")}{badge("danger","En retard","clock")}
  </div>
  <div style="display:flex;flex-wrap:wrap;gap:8px">
    <span class="sc-badge sc-badge--solid-danger">Urgent</span>{badge("danger","En qualification")}{badge("active","Confirmée, en correction")}{badge("done","Corrigée")}{badge("idea","Proposée")}{badge("planned","En réflexion")}{badge("planned","Écartée")}
  </div>
</div>''')

def tile(kind, label, icon, value, foot):
    return f'<div class="sc-tile sc-tile--{kind}"><span class="sc-tile__chip">{ic(icon)}</span><div class="sc-tile__text"><span class="sc-tile__head">{label}</span><span class="sc-tile__foot">{foot}</span></div><span class="sc-tile__value">{value}</span></div>'
P["StatTile"] = ("Synthèse", 520, "Tuiles compactes : icône, libellé et contexte, chiffre", lambda: f'''
<div class="sc-root" style="padding:20px;background:var(--bg)">
  <div class="sc-tiles">
    {tile("active","En cours","progress","4","dont 1 en recette")}
    {tile("planned","Planifiés","calendar","2","prochain départ le 2 nov.")}
    {tile("danger","Urgences",ALERT,"1","en qualification")}
    {tile("done","Livrés ce mois","check","3","dernier : Tableau de bord v2")}
  </div>
</div>''')

def urow(title, meta, state_kind, state_label, state_date):
    return f'''<div class="sc-urgent__row" tabindex="0">
      <div class="sc-urgent__main"><span class="sc-urgent__name">{title}</span><span class="sc-urgent__meta">{meta}</span></div>
      <div class="sc-urgent__side"><div class="sc-urgent__badges"><span class="sc-badge sc-badge--solid-danger">Urgent</span>{badge(state_kind, state_label)}</div>{f'<span class="sc-urgent__meta">{state_date}</span>' if state_date else ''}</div>
    </div>'''
P["UrgencyBanner"] = ("Statut", 560, "Titre sur toute la largeur, badges fixes en haut à droite", lambda: f'''
<div class="sc-root" style="padding:20px;background:var(--bg)">
  <section class="sc-urgent" aria-label="Urgences">
    <div class="sc-urgent__title">{ic(ALERT)}3 urgences</div>
    {urow("Paiement par carte refusé en production", "Déclarée par Julie M. · il y a 40 min", "danger", "En qualification", "")}
    {urow("Connexion impossible pour les comptes invités depuis la mise à jour de lundi, sur tous les navigateurs", "Déclarée par Marc D. · hier à 15 h 40", "active", "Confirmée, en correction", "confirmée hier à 17 h 12")}
    {urow("Export des factures vide", "Déclarée par Julie M. · 13 oct.", "done", "Corrigée", "corrigée ce matin à 9 h 05")}
  </section>
</div>''')

TODAY = 20.2
def grow(title, typ, tags, sub, bar, extra=""):
    t = {"sujet": tsujet, "bug": tbug}[typ]()
    return (f'<div class="sc-gantt__cell"><div class="sc-gantt__name" title="{title}">{title}</div><div class="sc-gantt__tags">{t}{tags}</div><div class="sc-gantt__sub">{sub}</div></div>'
            f'<div class="sc-gantt__track"><div class="sc-today" style="left:{TODAY}%"></div>{extra}{bar}</div>')
def mini(p, tok="active-strong"): return f'<span class="sc-mini"><i style="width:{p}%;background:var(--{tok})"></i></span>'
def bar(kind, left, width, p, label): return f'<div class="sc-bar sc-bar--{kind}" style="left:{left}%;width:{width}%;--p:{p}%" tabindex="0">{label}</div>'
P["Gantt"] = ("Planning", 1640, "Lignes sur trois niveaux : titre, étiquettes, avancement", lambda: f'''
<div class="sc-root" style="padding:20px;background:var(--bg)">
  <section class="sc-card">
    <header class="sc-card__head">
      <h2 class="sc-card__title">Planning des sujets</h2>
      <div style="display:flex;flex-wrap:wrap;gap:8px;align-items:center">
        <div class="sc-seg" role="group" aria-label="Échelle"><button type="button" aria-pressed="false">Semaine</button><button type="button" aria-pressed="true">Mois</button><button type="button" aria-pressed="false">Trimestre</button></div>
        <button class="sc-btn sc-btn--secondary sc-btn--icon sc-btn--sm" type="button" aria-label="Période précédente">{ic("chevron-left")}</button>
        <button class="sc-btn sc-btn--secondary sc-btn--sm" type="button">Aujourd'hui</button>
        <button class="sc-btn sc-btn--secondary sc-btn--icon sc-btn--sm" type="button" aria-label="Période suivante">{ic("chevron-right")}</button>
      </div>
    </header>
    <div class="sc-gantt" style="--cols:12">
      <div class="sc-gantt__th sc-gantt__th--left">Sujet · avancement</div>
      <div class="sc-gantt__th sc-gantt__weeks"><span><b>S40</b>28 sep</span><span><b>S41</b>5 oct</span><span class="is-now"><b>S42</b>12 oct</span><span><b>S43</b>19 oct</span><span><b>S44</b>26 oct</span><span><b>S45</b>2 nov</span><span><b>S46</b>9 nov</span><span><b>S47</b>16 nov</span><span><b>S48</b>23 nov</span><span><b>S49</b>30 nov</span><span><b>S50</b>7 déc</span><span><b>S51</b>14 déc</span></div>
      {grow("Tableau de bord v2","sujet",badge("done","Livré","check"),mini(100,"done-strong")+"100 % · 6/6 · 2 oct.",bar("done",0,6,100,"Livré"))}
      {grow("Import CSV clients","sujet",badge("danger","En retard","clock"),mini(80,"danger-strong")+"80 % · 4/5 · 10 oct.",bar("late",1.2,13.1,80,"80 %"),'<div class="sc-overdue" style="left:14.3%;width:5.9%"></div>')}
      {grow("Recherche globale","sujet",badge("review","En recette","eye"),mini(100,"review-strong")+"100 % · 6/6 · 18 oct.",bar("review",2.4,21.4,100,"En recette"))}
      {grow("Espace documents et partage sécurisé avec les clients","sujet",badge("active","En cours","progress")+'<span class="sc-badge" style="background:var(--warning-soft);color:var(--warning-ink)">Décalé de 7 j</span>',mini(62)+"62 % · 5/8 · 30 oct.",bar("active",8.3,29.8,62,"En cours · 62 %"),'<div class="sc-ghost" style="left:8.3%;width:21.4%"></div><span class="sc-slipchip" style="left:38.1%">+7 j</span>')}
      {grow("Export comptable en double","bug",badge("active","En cours","progress"),mini(50)+"50 % · 1/2 · 22 oct.",bar("active",15.5,10.7,50,"50 %"))}
      {grow("SSO Microsoft","sujet",badge("active","En cours","progress"),mini(25)+"25 % · 1/4 · 20 nov.",bar("active",16.7,46.4,25,"En cours · 25 %"))}
      {grow("Notifications email","sujet",badge("planned","Planifié","calendar"),mini(0)+"0 % · 0/3 · 2 nov.",bar("planned",41.7,11.9,0,"Planifié"))}
      {grow("Refonte de l'onboarding","sujet",badge("planned","Planifié","calendar"),mini(0)+"0 % · 0/5 · ◆ 18 déc.",bar("planned",58.3,36,0,"Planifié"),'<div class="sc-milestone" style="left:96.4%" title="Mise en prod v3 · 18 déc."></div>')}
    </div>
  </section>
</div>''')

def item(typ, title, meta, state):
    t = {"sujet": tsujet, "bug": tbug, "idee": tidee}[typ]()
    return f'<div class="sc-item" tabindex="0"><div class="sc-item__body"><span class="sc-item__title">{title}</span><div class="sc-item__line">{t}<span class="sc-item__meta">{meta}</span></div></div>{state}</div>'
P["ItemRow"] = ("Listes", 820, "Deux lignes : titre, puis type et méta ; état en haut à droite", lambda: f'''
<div class="sc-root" style="padding:20px;background:var(--bg);display:grid;grid-template-columns:repeat(auto-fit,minmax(300px,1fr));gap:16px;align-items:start">
  <section class="sc-card">
    <header class="sc-card__head"><h2 class="sc-card__title">Non planifié</h2><span class="sc-num" style="color:var(--ink-muted)">3</span></header>
    <div class="sc-list">
      {item("bug","Affichage cassé sur Safari mobile quand on ouvre une facture depuis la liste","Déclaré par Marc D. · 13 oct.",badge("planned","Backlog"))}
      {item("sujet","Tableau de bord des ventes","En attente de planification",badge("planned","Backlog"))}
      {item("bug","Faute de frappe sur la page de contact","Corrigé le 11 oct.",badge("done","Corrigé"))}
    </div>
  </section>
  <section class="sc-card">
    <header class="sc-card__head"><h2 class="sc-card__title">Idées</h2><span class="sc-num" style="color:var(--ink-muted)">3</span></header>
    <div class="sc-list">
      {item("idee","Export PDF des factures","Proposée par Marc D. · hier",badge("idea","Proposée"))}
      {item("idee","Mode sombre pour l'espace client","Affinée en réunion le 8 oct.",badge("planned","En réflexion"))}
      {item("idee","Application mobile native","Écartée le 1er oct. · raison dans le détail",badge("planned","Écartée"))}
    </div>
  </section>
</div>''')

P["SidePanel"] = ("Formulaires", 1360, "Déclaration d'un bug : étape 1 sur 4, l'impact", lambda: f'''
<div class="sc-root" style="padding:20px;background:var(--bg);display:flex;justify-content:flex-end">
  <aside class="sc-sheet" role="dialog" aria-labelledby="sp-title">
    <div class="sc-sheet__head">
      <div class="sc-sheet__top">
        <span class="sc-sheet__chip">{ic(BUG)}</span>
        <button class="sc-btn sc-btn--ghost sc-btn--icon sc-btn--sm" type="button" aria-label="Fermer">{ic("x")}</button>
      </div>
      <h2 class="sc-sheet__title" id="sp-title">Signaler un bug</h2>
      <p class="sc-sheet__desc">Paiement par carte refusé en production</p>
      <div class="sc-steps" aria-label="Étape 1 sur 4"><span>Étape 1 sur 4 · Impact</span><div class="sc-steps__bars"><i class="is-current"></i><i></i><i></i><i></i></div></div>
    </div>
    <form class="sc-sheet__body" onsubmit="event.preventDefault()">
      <span class="sc-field-label" id="impact-q">Quel est l'impact pour vos utilisateurs ?</span>
      <label class="sc-choice"><input class="sc-radio" type="radio" name="impact" id="impact-all" checked><b>Bloquant pour tous</b><span>Plus personne ne peut utiliser la fonctionnalité.</span></label>
      <label class="sc-choice"><input class="sc-radio" type="radio" name="impact" id="impact-some"><b>Bloquant pour certains</b><span>Une partie des utilisateurs ou des cas est bloquée.</span></label>
      <label class="sc-choice"><input class="sc-radio" type="radio" name="impact" id="impact-workaround"><b>Gênant mais contournable</b><span>On peut continuer à travailler autrement.</span></label>
      <div class="sc-hint">{ic(ALERT, style="color:var(--danger-strong)")}<span>Ce choix déclare une <b style="color:var(--ink)">urgence</b> : l'équipe est alertée dès l'envoi.</span></div>
    </form>
    <div class="sc-sheet__foot"><button class="sc-btn sc-btn--ghost" type="button">Annuler</button><button class="sc-btn sc-btn--primary" type="button">Continuer</button></div>
  </aside>
</div>''')

X = '<svg class="sc-icon" viewBox="0 0 24 24" aria-hidden="true" style="width:14px;height:14px">' + inner("x") + '</svg>'
CHEV = ic("chevron-down") if (TABLER / "chevron-down.svg").exists() else ic("chevron-right", style="transform:translateY(-50%) rotate(90deg)")
def fchip(name):
    return f'<span class="sc-file"><span class="sc-thumb" aria-hidden="true"></span><span>{name}</span><button type="button" aria-label="Retirer {name}">{X}</button></span>'
P["Field"] = ("Formulaires", 900, "Champ, liste, cases et fichiers joints", lambda: f'''
<div class="sc-root" style="padding:20px;background:var(--bg);display:grid;grid-template-columns:repeat(auto-fit,minmax(280px,1fr));gap:20px;align-items:start">
  <div style="display:flex;flex-direction:column;gap:14px">
    <div class="sc-field"><label class="sc-field-label" for="f-title">Que se passe-t-il ?</label><input class="sc-input" id="f-title" value="Le paiement par carte est refusé"><p class="sc-help">Une phrase courte, elle sert de titre au ticket.</p></div>
    <div class="sc-field"><label class="sc-field-label" for="f-empty">Depuis quand ?</label><input class="sc-input" id="f-empty" placeholder="Ex. : ce matin vers 9 h"></div>
    <div class="sc-field"><label class="sc-field-label" for="f-env">Environnement</label><span class="sc-select"><select class="sc-input" id="f-env"><option>Production</option><option>Recette</option></select>{CHEV}</span><p class="sc-help">Même padding à droite qu'à gauche : le chevron ne touche jamais la bordure.</p></div>
    <div class="sc-field"><label class="sc-field-label" for="f-steps">Étapes pour reproduire</label><textarea class="sc-input" id="f-steps">1. Je vais sur la page de paiement
2. Je saisis une carte valide</textarea></div>
  </div>
  <div style="display:flex;flex-direction:column;gap:14px">
    <label class="sc-checkline"><input class="sc-check" type="checkbox" id="f-c1" checked>Ça fonctionnait avant</label>
    <label class="sc-checkline"><input class="sc-check" type="checkbox" id="f-c2">Prévenir aussi les admins par email</label>
    <label class="sc-checkline"><input class="sc-radio" type="radio" name="f-r" id="f-r1" checked>Client</label>
    <label class="sc-checkline"><input class="sc-radio" type="radio" name="f-r" id="f-r2">Admin</label>
    <span class="sc-field-label">Captures jointes</span>
    <div class="sc-files">{fchip("erreur-paiement.png")}{fchip("console-navigateur.png")}{fchip("capture-3.png")}</div>
  </div>
</div>''')

def dark_copy(body):
    body = re.sub(r'id="([^"]+)"', r'id="\1-d"', body)
    body = re.sub(r'aria-labelledby="([^"]+)"', r'aria-labelledby="\1-d"', body)
    return body.replace('name="impact"', 'name="impact-d"').replace('name="f-r"', 'name="f-r-d"')

for comp, (group, height, subtitle, render) in P.items():
    body = render().strip()
    html = (f'<!-- @dsCard group="{group}" height={height} subtitle="Clair et sombre · {subtitle}" -->\n'
            '<div class="sc-duo">\n'
            f'<div class="sc-pane" data-theme="light"><span class="sc-pane__tag">Clair</span>\n{body}\n</div>\n'
            f'<div class="sc-pane" data-theme="dark"><span class="sc-pane__tag">Sombre</span>\n{dark_copy(body)}\n</div>\n</div>\n')
    (COMP / comp / "preview.html").write_text(html)
    print(comp, len(html))
