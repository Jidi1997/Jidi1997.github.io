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