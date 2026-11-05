# Personal Academic Website Development & Deployment Rules

## 1. Branch Architecture & Deployment Mechanism
- **`main` Branch (Source)**: Contains Jekyll markdown source files, layouts, and bibliography (`_bibliography/papers.bib`, `_pages/`, `_layouts/`, `_config.yml`).
- **`gh-pages` Branch (Live Site)**: Contains the rendered static HTML, CSS, JS, and PDF assets served directly by GitHub Pages.
- **Live Deployment Constraint**: Pushing to `main` does NOT guarantee immediate live site updates if GitHub Actions fails or runner versions change. To ensure live updates take effect:
  - If source changes in `main` are made, verify whether the live site at `https://jidi1997.github.io` updates.
  - If live updates do not reflect, synchronize the pre-rendered HTML/assets to the `gh-pages` branch directly and push to `origin/gh-pages`.

## 2. GitHub Token & Workflow Scope Boundaries
- **PAT Scope Limitation**: The configured Git credentials (Personal Access Token) lack the `workflow` scope.
- **Constraint**: Do NOT commit or push modifications to `.github/workflows/` using the default git credentials, as GitHub will reject the push with an authorization error.
- All live site emergency fixes and asset updates should be made directly on `gh-pages` or through standard content files on `main`.

## 3. Publication & CV Consistency
- The `publications` page (`_pages/publications.md` and `_bibliography/papers.bib`) must strictly align with the publications listed in the current CV PDF (`assets/pdf/2-CV-CAO.pdf`).
- Do not keep extraneous papers on the publications page that are excluded from the official CV.
- Always verify live deployment by checking the live URL after pushing.
