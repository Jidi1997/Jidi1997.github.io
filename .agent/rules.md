# 学术主页构建规则 (Academic Site Rules)

## 1. 核心目标
- 基于 Jekyll 框架构建一个极简、响应式的学术个人主页。
- 整合 `letgetql` 的结构建议（侧重内容布局）与 `taniarascia` 的技术实现（侧重代码逻辑）。

## 2. Agent 行为准则 (Agent Behaviors)
- **浏览调研：** 在开始编码前，必须调用浏览器工具完整解析提供的两个 URL，提取 `Gemfile` 配置参数、目录层级和 CSS 核心样式。
- **环境安全：** 在终端执行 `bundle` 或 `jekyll` 命令前，先检查 macOS 环境依赖（如 Ruby 版本）。
- **学术规范：** 优先建立 `_data/publications.yml` 用于结构化存储论文，而非手动在 HTML 中硬编码。
- **原子化提交：** 每完成一个核心功能（如导航栏、论文列表渲染），立即在内置浏览器预览并截图。

## 3. 技术偏好 (Tech Preferences)
- **CSS:** 优先使用纯 CSS 或极简框架，保持学术严肃感。
- **布局:** 必须包含：Bio (Home), Publications, Research, Teaching, 和 Blog。
- **自动化:** 自动将 `_posts` 中的最新 3 篇文章同步到首页。


## 4. 分支架构与部署规则 (Branch Architecture & Deployment Rules)
- **分支双轨制：** `main` 分支存储 Jekyll 源代码（Markdown / Liquid / BibTeX）；`gh-pages` 分支存储预渲染静态文件（HTML / CSS / JS / PDF），供 GitHub Pages 直接托管。
- **部署验证：** 推送至 `main` 后若自动化 Actions 失败或环境不兼容，不得假设线上已生效。应直接同步静态构建产物至 `gh-pages` 并推送，随后访问生产 URL 验证生效。
- **Token 权限边界：** 本地 Git 配置的 Personal Access Token 缺少 `workflow` 作用域，严禁通过该凭证推送修改 `.github/workflows/` 下的工作流文件。
- **论文与简历对齐：** `_bibliography/papers.bib` 与 Publications 页面必须与最新官方简历 PDF (`assets/pdf/2-CV-CAO.pdf`) 严格保持一致，不得保留未列入 CV 的其他文章。
