#!/usr/bin/env python3
"""
Fetch all public GitHub repositories for Jidi1997 and update _data/repositories.yml automatically.
Excludes forks, private repos, and specified system/site repos.
Saves detailed metadata (stars, forks, description, language, language_color, html_url)
to enable native static rendering of repository cards on the website.
"""
import os
import json
import urllib.request

USERNAME = "Jidi1997"

# Repositories to exclude from the showcases page
EXCLUDE_REPOS = {
    f"{USERNAME}/{USERNAME}.github.io",
    f"{USERNAME}/.github",
}

# Standard color mapping for major programming languages
LANGUAGE_COLORS = {
    "Python": "#3572A5",
    "JavaScript": "#f1e05a",
    "TypeScript": "#3178c6",
    "HTML": "#e34c26",
    "CSS": "#563d7c",
    "Jupyter Notebook": "#DA5B0B",
    "Shell": "#89e051",
    "Ruby": "#701516",
    "Go": "#00ADD8",
    "Rust": "#dea584",
    "Java": "#b07219",
    "C++": "#f34b7d",
    "C": "#555555",
}

def fetch_repos():
    token = os.environ.get("GITHUB_TOKEN")
    url = f"https://api.github.com/users/{USERNAME}/repos?type=owner&per_page=100&sort=pushed"
    req = urllib.request.Request(url)
    req.add_header("User-Agent", "Jekyll-Repo-Fetcher")
    if token:
        req.add_header("Authorization", f"Bearer {token}")
    
    try:
        with urllib.request.urlopen(req) as response:
            if response.status == 200:
                data = json.loads(response.read().decode('utf-8'))
                repos = []
                for r in data:
                    full_name = r.get("full_name")
                    is_fork = r.get("fork", False)
                    is_private = r.get("private", False)
                    if not is_fork and not is_private and full_name not in EXCLUDE_REPOS:
                        repos.append({
                            "name": r.get("name"),
                            "full_name": full_name,
                            "description": r.get("description") or "",
                            "stargazers_count": r.get("stargazers_count", 0),
                            "forks_count": r.get("forks_count", 0),
                            "language": r.get("language") or "",
                            "html_url": r.get("html_url") or f"https://github.com/{full_name}"
                        })
                return repos
    except Exception as e:
        print(f"[ERROR] Failed to fetch repos from GitHub API: {e}")
        return None

def update_repositories_yml(repos):
    if not repos:
        print("[WARN] No repos retrieved or error occurred. Keeping existing repositories.yml.")
        return

    script_dir = os.path.dirname(os.path.abspath(__file__))
    filepath = os.path.normpath(os.path.join(script_dir, "..", "_data", "repositories.yml"))
    
    content = f"""# ============================================================
# GitHub 仓库配置（自动更新）
# 由 _scripts/fetch_repos.py 在构建时自动更新
# ============================================================

github_users:
  - {USERNAME}

repo_description_lines_max: 2

github_repos:
"""
    for repo in repos:
        lang = repo.get("language") or ""
        lang_color = LANGUAGE_COLORS.get(lang, "#858585")
        
        # Clean description for YAML string format
        desc = repo.get("description") or ""
        desc_escaped = desc.replace('\\', '\\\\').replace('"', '\\"')
        
        content += f"  - name: \"{repo.get('name')}\"\n"
        content += f"    full_name: \"{repo.get('full_name')}\"\n"
        content += f"    description: \"{desc_escaped}\"\n"
        content += f"    stargazers_count: {repo.get('stargazers_count')}\n"
        content += f"    forks_count: {repo.get('forks_count')}\n"
        content += f"    language: \"{lang}\"\n"
        content += f"    language_color: \"{lang_color}\"\n"
        content += f"    html_url: \"{repo.get('html_url')}\"\n"

    with open(filepath, "w", encoding="utf-8") as f:
        f.write(content)
    print(f"[SUCCESS] Updated {filepath} with {len(repos)} repos:")
    for r in repos:
        print(f"  - {r['full_name']}")

if __name__ == "__main__":
    repos = fetch_repos()
    if repos:
        update_repositories_yml(repos)
