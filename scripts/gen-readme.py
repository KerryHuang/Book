"""產生根目錄 README.md 與各分類目錄 README.md。

用法：python scripts/gen-readme.py
文章標題取檔名（front matter 有 title 則優先）；front matter 的 kind/source/author 會標在標題後。
"""
import os
import re
import sys

sys.stdout.reconfigure(encoding="utf-8")
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# 頂層目錄 → 說明（順序即 README 順序）
TOP = {
    "dotnet": ".NET 開發：C#、ASP.NET Core、Web API、EF Core、測試、LINE Bot",
    "architecture": "架構與設計：設計模式、認證授權、微服務、DDD/CQRS",
    "database": "資料庫：SQL Server 維運與移轉、DBeaver、SAP 資料表",
    "infra": "基礎建設：Docker、IIS/Windows Server、Azure、CI/CD、工具安裝",
    "devtools": "開發工具：Git、Visual Studio、GitHub Copilot、Markdown/HackMD、Mac 裝機",
    "ai": "AI 工具：Claude Code、Graphify、.NET AI Agent 與 MCP",
    "management": "專案與流程管理：Redmine、MES 導入、SSDLC、外包規範、SOP/BPMN、系統評估",
}

# 子目錄 → 說明
SUB = {
    "dotnet/csharp": "C# 語言與常用套件",
    "dotnet/csharp/菜雞與物件導向": "物件導向與 SOLID 入門系列",
    "dotnet/aspnet-core": "ASP.NET Core 教育訓練文件",
    "dotnet/aspnet-core/net6-samples": ".NET 6 各套件範例",
    "dotnet/aspnet-core/wdmis": "WDMIS 專案技術筆記",
    "dotnet/web-api": "Web API 設計、JWT、Swagger",
    "dotnet/entity-framework": "EF Core Migrations",
    "dotnet/testing": "單元測試",
    "dotnet/line-bot": "LINE Bot SDK Hands-On Labs",
    "dotnet/line-bot/basic": "基本訊息推送",
    "dotnet/line-bot/webhook": "Webhook",
    "dotnet/line-bot/liff": "LIFF",
    "dotnet/line-bot/CLI": "CLI 工具",
    "dotnet/菜雞新訓記": ".NET 新人培訓系列（Git、Web API、Dapper、Swagger、三層式、DI、Validation）",
    "architecture/design-patterns": "設計模式",
    "architecture/auth": "OAuth、SSO、CAS",
    "architecture/microservices": "微服務架構（Andrew Wu 系列）",
    "architecture/microservices/API First Workshop 設計概念與實做案例": "API First",
    "architecture/microservices/基礎建設 - 建立微服務的執行環境": "微服務基礎建設",
    "architecture/microservices/實做基礎技術 API & SDK Design": "API 與 SDK 設計",
    "architecture/microservices/建構微服務開發團隊": "架構面試題",
    "architecture/microservices/架構師觀點 - 轉移到微服務架構的經驗分享": "轉移經驗",
    "architecture/microservices/案例實作 - IP 查詢服務的開發與設計": "案例實作",
    "architecture/ddd-cqrs": "DDD、CQRS、MediatR",
    "database/sql-server": "SQL Server",
    "database/dbeaver": "DBeaver",
    "database/sap": "SAP 資料表清單",
    "infra/docker": "Docker 安裝各種服務",
    "infra/iis-windows": "IIS 與 Windows Server",
    "infra/azure": "Azure",
    "infra/ci-cd": "CI/CD 與程式碼品質",
    "infra/tools": "工具安裝",
    "devtools/git": "Git 語法、Git Flow、SSH",
    "devtools/git/30-days-git": "30 天精通 Git 版本控管（Will 保哥）",
    "devtools/visual-studio": "Visual Studio 與 .NET CLI",
    "devtools/github-copilot": "GitHub Copilot",
    "devtools/markdown": "Markdown 與 HackMD",
    "management/redmine-mis": "MIS 及專案管理：使用 Redmine（iThome 鐵人賽系列）",
    "management/mes-導入": "MES 導入方法論",
    "management/軟體專案任務挑戰賽": "真人與 AI 從需求到交付協作體驗",
    "management/軟體專案任務挑戰賽/工具使用指南": "Jira / Confluence / Rovo 工具指南",
    "management/軟體專案任務挑戰賽/關卡任務說明": "關卡任務",
    "management/sop-bpmn": "SOP 製作與 BPMN 流程圖",
    "management/系統評估": "系統評估與數位轉型",
}

SKIP_DIRS = {"images", "figures", "Images"}
# 不放進 MkDocs 網站的目錄：README 內改連 GitHub，避免網站 build 時出現斷連結
GITHUB_ONLY = set()
GITHUB = "https://github.com/KerryHuang/Book/blob/main/"


def front_matter(txt):
    if not txt.startswith("---"):
        return {}, txt
    end = txt.find("\n---", 3)
    if end < 0:
        return {}, txt
    fm = {}
    for line in txt[3:end].strip().splitlines():
        if ":" in line:
            k, v = line.split(":", 1)
            fm[k.strip()] = v.strip().strip('"')
    return fm, txt[end + 4:]


def title_of(path):
    txt = open(path, encoding="utf-8", errors="ignore").read()
    fm, body = front_matter(txt)
    t = (fm.get("title") or os.path.splitext(os.path.basename(path))[0]).strip()
    return t, fm


def link(path_rel):
    p = path_rel.replace(os.sep, "/").replace("%", "%25").replace("#", "%23").replace("?", "%3F")
    return "<" + p + ">"


def natural_key(s):
    return [int(x) if x.isdigit() else x.lower() for x in re.split(r"(\d+)", s)]


def render_dir(abs_dir, rel_dir, depth, out):
    """列出 rel_dir 底下的文章與子目錄（遞迴）。"""
    entries = sorted(os.listdir(abs_dir), key=natural_key)
    files = [e for e in entries if e.endswith(".md") and e != "README.md"]
    dirs = [e for e in entries if os.path.isdir(os.path.join(abs_dir, e)) and e not in SKIP_DIRS and not e.startswith(".")]
    for f in files:
        p = os.path.join(abs_dir, f)
        t, fm = title_of(p)
        tag = ""
        if fm.get("kind") == "reprint":
            who = fm.get("author") or ""
            src = fm.get("source") or ""
            if src.startswith("http"):
                tag = f" — [轉貼{'：' + who if who else ''}]({src})"
            elif who:
                tag = f" — 轉貼：{who}"
            else:
                tag = " — 轉貼"
        out.append(f"{'  ' * depth}- [{t}]({link(os.path.join(rel_dir, f))}){tag}")
    for d in dirs:
        key = os.path.join(rel_dir, d).replace(os.sep, "/")
        desc = SUB.get(key, "")
        out.append(f"{'  ' * depth}- **{d}/**{'：' + desc if desc else ''}")
        render_dir(os.path.join(abs_dir, d), os.path.join(rel_dir, d), depth + 1, out)


def count_md(abs_dir):
    n = 0
    for r, ds, fs in os.walk(abs_dir):
        ds[:] = [d for d in ds if d not in SKIP_DIRS]
        n += sum(1 for f in fs if f.endswith(".md") and f != "README.md")
    return n


def href(top, name):
    if top in GITHUB_ONLY:
        return GITHUB + top + "/" + name.replace("#", "%23").replace(" ", "%20")
    return link(f"{top}/{name}")


def sub_outline(abs_top, top):
    """頂層目錄底下第一層子目錄與散檔的一覽（名稱、說明、篇數）。"""
    lines = []
    entries = sorted(os.listdir(abs_top), key=natural_key)
    for d in entries:
        ad = os.path.join(abs_top, d)
        if not os.path.isdir(ad) or d in SKIP_DIRS or d.startswith("."):
            continue
        desc = SUB.get(f"{top}/{d}", "")
        lines.append(f"  - [{d}/]({href(top, d)}){'：' + desc if desc else ''}（{count_md(ad)} 篇）")
    for f in entries:
        if f.endswith(".md") and f != "README.md":
            lines.append(f"  - [{os.path.splitext(f)[0]}]({href(top, f)})")
    return lines


def write(path, lines):
    with open(path, "w", encoding="utf-8", newline="\n") as fh:
        fh.write("\n".join(lines) + "\n")


def main():
    table = ["| 目錄 | 內容 | 篇數 |", "|---|---|---:|"]
    outline = []
    for top, desc in TOP.items():
        abs_top = os.path.join(ROOT, top)
        if not os.path.isdir(abs_top):
            continue
        n = count_md(abs_top)
        top_href = f"{GITHUB}{top}/README.md" if top in GITHUB_ONLY else f"<{top}/README.md>"
        table.append(f"| [{top}/]({top_href}) | {desc} | {n} |")
        outline.append(f"- **[{top}/]({top_href})** {desc}")
        outline += sub_outline(abs_top, top)
        body = [f"# {top}", "", desc, "", "[← 回總目錄](../README.md)", ""]
        render_dir(abs_top, "", 0, body)
        write(os.path.join(abs_top, "README.md"), body)
        print(f"{top}: {n} 篇")

    root = [
        "# Kerry Huang 的開發筆記",
        "",
        "個人技術文件庫，收錄自己撰寫的教學、安裝手冊與專案筆記，以及值得反覆查閱的他人文章存檔。",
        "依知識領域分七個目錄，每個目錄的 README 是該領域的完整文章清單。",
        "",
        "## 目錄",
        "",
        *table,
        "",
        "## 各領域內容",
        "",
        *outline,
        "",
        "## 慣例",
        "",
        "- **原創與轉貼**：每篇文章檔頭有 front matter，`kind: original` 為自己撰寫，`kind: reprint` 為他人文章存檔，"
        "`source` 與 `author` 記錄出處。目錄清單中標「轉貼」者連結指向原文。",
        "- **圖片**：放在文章所在目錄的 `images/`，以相對路徑引用。影片（mp4）走 Git LFS。",
        "- **新增文章**：放進對應領域目錄、加上 front matter，然後執行 `python scripts/gen-readme.py` 重新產生所有 README。",
        "- **文件網站**：push 到 main 後由 GitHub Actions 以 MkDocs Material 建置並發布到 https://kerryhuang.github.io/Book/ 。"
        "本機預覽：建虛擬環境後 `pip install -r requirements.txt`，再執行 `bash scripts/build-site.sh serve`。",
        "- **來源標記的限制**：轉貼文章的出處以檔內證據判定，少數只標到網域或 `kind: unknown`，歡迎修正。",
    ]
    write(os.path.join(ROOT, "README.md"), root)


if __name__ == "__main__":
    main()
