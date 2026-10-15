# github-project-dashboard

Dashboard client branché sur GitHub Projects. Le client voit un Gantt de ses sujets et déclare des bugs, des urgences et des idées. L'équipe tech travaille uniquement dans GitHub. Il y a une instance Docker par client.

## Lire en premier

1. `docs/HANDOFF.md` : l'état du projet, ce qui a changé depuis la PRD, les points ouverts et la prochaine étape.
2. `docs/superpowers/specs/2026-10-15-dashboard-client-gh-projects-design.md` : la PRD validée, source de vérité fonctionnelle.
3. `docs/design/design-system/README.md` : la charte et les règles d'usage des tokens et des composants.

## Repères

- **Langue** : tout est en français, l'interface comme la documentation. Vouvoiement, aucun jargon GitHub dans l'interface client.
- **Stack retenue** : Rust + Loco (version figée), React + Vite + shadcn/ui, SQLite en WAL, volume `/data` unique, image GHCR.
- **Design system** : les tokens sont dans `docs/design/design-system/tokens.json` (clair et sombre, contrastes AA vérifiés), les classes des composants dans `components/bundle.css`, et les icônes viennent de Tabler (`@tabler/icons-react`).
- **Prototypes** : `docs/design/flux/*.dc.html` sont des copies des artboards du canvas. Le canvas en ligne fait foi : https://claude.ai/artifact/MVgRgVc4qRpbEReToXJ84y
- `.superpowers/` (brouillons de brainstorming) et `.playwright-mcp/` sont ignorés par git.
