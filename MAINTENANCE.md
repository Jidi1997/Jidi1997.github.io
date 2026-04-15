# 学术主页维护与更新手册 (Maintenance Guide

这份文档旨在帮助您快速掌握如何管理和更新您的个人主页。针对 Jekyll `al-folio` 主题的结构，我们将文件归纳为以下几类。

---

## 1. 核心内容更新指南 (最常修改的地方)

这些文件采用 YAML 填空或 Markdown 格式，修改后网页会自动渲染。

### 1.1 个人资料与首页 (Index / About Me)
- **文件路径**: `index.md`
- **操作**: 
  - **自我介绍**: 直接修改文件底部的文字内容。
  - **板块划分**: 使用 `<div class="glass-card"> ... </div>` 包裹内容，可实现美观的毛玻璃效果板块。
  - **头像**: 将图片放入 `assets/img/`，并在文件顶部 `profile.image` 修改文件名。

### 1.2 社交图标与联系方式 (Social Icons)
- **数据文件**: `_data/socials.yml`
- **布局位置**: 社交图标显示在右侧头像区域下方（由 `_layouts/about.liquid` 中的 `.profile-social` 渲染，样式定义在 `_sass/_base.scss` 的 `.header-profile .profile-social` 部分）。
- **操作**: 
  - **显示/隐藏**: 在 `_data/socials.yml` 行首添加或删除 `#`（注释符）即可。
  - **修改链接**: 编辑 `email` 或 `scholar_userid` 等字段。
  - **自定义图标**: 参考文件底部的 `custom_social` 模板。

### 1.3 论文与出版物 (Publications)
- **文件路径**: `_bibliography/papers.bib`
- **操作**: 
  - 使用标准 BibTeX 格式添加条目。
  - 支持 `pdf`, `code`, `abstract` 等字段，添加后会自动生成对应的按钮。

### 1.4 GitHub 仓库展示 (Repositories)
- **文件路径**: `_data/repositories.yml`
- **操作**: 
  - 在 `github_repos` 列表中按 `用户名/项目名` 格式添加你想展示的项目，网页会自动抓取统计数据。

---

## 2. 页面与导航维护 (Navigation)

### 2.1 导航栏显隐与排序
- **文件路径**: `_pages/` 目录下的 `.md` 文件（如 `publications.md`, `repositories.md`, `cv.md`）。
- **操作**: 
  - `nav: true / false`: 决定该页面是否出现在顶部菜单。
  - `nav_order: 数字`: 数字越小，菜单位置越靠左。

### 2.2 简历板块 (CV)
- **文件路径**: `_pages/cv.md` 及 `_data/cv.yml`
- **操作**: 
  - **PDF 链接**: 在 `_pages/cv.md` 的 `cv_pdf` 字段指定。
  - **内容更新**: 编辑 `_data/cv.yml` 或 `assets/json/resume.json`（取决于你选用的格式）。

---

## 3. 全局设置 (进阶自定义)

- **`_config.yml`**: 网站的大脑。在这里修改网站标题 (`title`)、你的名字 (`first_name`)、是否开启黑夜模式 (`enable_darkmode`) 等。**注意：修改此文件后，建议重启本地预览。**
- **`assets/` 目录**: 存放所有的静态文件。
  - `assets/img/`: 头像、项目配图。
  - `assets/pdf/`: 论文原文、简历 PDF。

---

## 4. 维护与发布 (最佳实践)

对于 `al-folio` 主题，**最推荐、最简单且完全免费**的发布方式是使用 **GitHub Pages** 配合 **GitHub Actions**。当你把代码推送到 GitHub 时，服务器会自动在后台编译并更新你的网站。

### 🌟 日常维护“黄金三步” (The Golden Loop)

在以后每一次你想更新网页内容（比如加了一篇论文、改了自我介绍）时，只需要重复以下三个步骤：

#### 第一步：本地修改内容
按照本文档第 1、2 部分的说明，在 VS Code 中修改对应的 `.md` 或 `.yml` 文件并保存。

#### 第二步：本地预览效果 (可选但强烈建议)
在终端运行以下命令开启本地服务器，检查修改是否正确、网页是否报错：
```bash
export PATH="/opt/homebrew/opt/ruby/bin:$PATH"
bundle exec jekyll serve
```
浏览器打开: [http://localhost:4000](http://localhost:4000) 确认无误后，可以在终端按 `Ctrl + C` 关闭预览。

#### 第三步：一键推送到 GitHub (自动发布)
确认本地预览完美后，在终端按顺序运行以下三条指令，将改动同步到线上：
```bash
git add .
git commit -m "Personal website updated"  # 引号内可以改成你本次修改的备忘
git push origin main
```

**✅ 就这么简单！** 
推送完成后，稍等 1-3 分钟，GitHub 会自动完成编译，你就可以在浏览器中刷新你的个人网址看到最新内容了。

> **💡 故障排查小贴士**:
> 如果推送后几分钟网页还没有变化，你可以登录你的 GitHub 仓库页面，点击顶部的 **`Actions`** 标签夹。在这里你可以看到网站部署的进度状态。如果出现红色的 ❌，点击进去通常能看到具体的报错信息（比如 YAML 格式缩进不对等）。

---

## 5. 项目结构索引

- `_data/`: 存放“填空式”的数据文件（最重要）。
- `_pages/`: 存放网页的各个独立页面。
- `_includes/`: 网页组件（如页眉、页脚、GitHub 统计卡代码）。
- `_layouts/`: 网页模板（决定页面长什么样）。
- `_sass/`: 存放颜色、间距等样式代码。
