# 完整的 Git Flow + Semantic Release 整合流程

### 🎯 所有流程驗證成功

| 測試階段           | 分支         | Commit 類型              | Semantic Release 模式 | 建立 Tag | 結果               |
| ------------------ | ------------ | ------------------------ | --------------------- | -------- | ------------------ |
| **開發 1**         | develop      | `ci(gitlab):`            | `--dry-run`           | ❌        | ✅ Beta 版本預覽    |
| **開發 2**         | develop      | `fix(ci):` × 2           | `--dry-run`           | ❌        | ✅ Beta 版本預覽    |
| **Release**        | release/auto | (合併commits)            | `--dry-run`           | ❌        | ✅ RC 版本預覽      |
| **Release → Main** | main         | Merge commit             | **正式發布**          | ✅        | ✅ 正式版本 + Tag   |
| **清理配置**       | develop      | `refactor(ci):`          | `--dry-run`           | ❌        | ✅ Beta 版本預覽    |
| **Hotfix**         | hotfix/auto  | `fix(ci):` + `docs:` × 2 | `--dry-run`           | ❌        | ✅ 版本預覽         |
| **Hotfix → Main**  | main         | Merge commit             | **正式發布**          | ✅        | ✅ PATCH 版本 + Tag |

### 🔑 關鍵成就

1. ✅ **版本號自動化**
   - Semantic-release 完全控制版本號
   - 不需要手動指定版本
   - Git flow 使用 `auto` 作為臨時名稱
2. ✅ **避免版本重複**
   - Hotfix/Release 分支使用 `--dry-run`（只預覽）
   - Main 分支使用正式發布模式（建立 tag）
   - 相同版本號，但只有 main 建立 tag
3. ✅ **CI/CD 觸發優化**
   - Main 分支：所有 commit 都觸發（包含 merge）
   - Develop 分支：僅語義化 commit 觸發
   - Release/Hotfix 分支：所有 commit 觸發
   - Back-merge 不會重複觸發
4. ✅ **完整的版本管理**
   - 自動建立 Git tag
   - 自動更新 CHANGELOG.md
   - 自動建立 GitLab Release
   - Docker image 自動標記版本

### 📝 最終配置

#### `.releaserc` - Semantic Release 配置

```json
{
  "branches": [
    "main",                    // 正式版本
    {
      "name": "develop",
      "channel": "beta",
      "prerelease": "beta"     // beta 版本
    },
    {
      "name": "release/*",
      "channel": "rc",
      "prerelease": "rc"       // RC 版本
    },
    {
      "name": "hotfix/*"       // 直接產生正式版本
    }
  ]
}
```

#### `.gitlab-ci.yml` - CI/CD 配置重點

**觸發規則**：



- Main: 所有 commit
- Develop: 語義化 commit
- Release/Hotfix: 所有 commit

**Semantic Release 執行模式**：



- Main: `npx semantic-release`（正式發布）
- 其他: `npx semantic-release --dry-run`（預覽）

### 🚀 標準工作流程

#### Feature 開發

```bash
git flow feature start my-feature
git commit -m "feat: add new feature"
git flow feature finish my-feature
# develop 產生 beta 版本（預覽）
```

#### Release 發布

```bash
git flow release start auto
git flow release finish -n auto
git push origin main develop
# release/* 產生 rc 版本（預覽）
# main 產生正式版本 + tag
```

#### Hotfix 修復

```bash
git flow hotfix start auto
git commit -m "fix: critical bug"
git flow hotfix finish -n auto
git push origin main develop
# hotfix/* 預覽 patch 版本
# main 產生正式 patch 版本 + tag
```

### 📚 完整文件

所有配置和流程說明都已記錄在：



- ✅ [`.doc/CI-CD/GitFlow_SemanticRelease_工作流程.md`](vscode-webview://14rv7nefq8c5i58a0qj2bvo85gq74ruaqu5n0b8rukdjvkquuhot/index.html?id=3dc6504c-a30f-4a93-97e0-c69002ee2678&parentId=2&origin=d983d1a5-f5d2-4e69-9c0a-7d1568b6ebed&swVersion=4&extensionId=Anthropic.claude-code&platform=electron&vscode-resource-base-authority=vscode-resource.vscode-cdn.net&parentOrigin=vscode-file%3A%2F%2Fvscode-app&session=610f8b3a-7a09-408e-a1ad-a51c03a2df42) - 完整工作流程文件
- ✅ [`CLAUDE.md`](vscode-webview://14rv7nefq8c5i58a0qj2bvo85gq74ruaqu5n0b8rukdjvkquuhot/index.html?id=3dc6504c-a30f-4a93-97e0-c69002ee2678&parentId=2&origin=d983d1a5-f5d2-4e69-9c0a-7d1568b6ebed&swVersion=4&extensionId=Anthropic.claude-code&platform=electron&vscode-resource-base-authority=vscode-resource.vscode-cdn.net&parentOrigin=vscode-file%3A%2F%2Fvscode-app&session=610f8b3a-7a09-408e-a1ad-a51c03a2df42) - AI 提示詞文件（Git Flow 章節）
- ✅ [`README.md`](vscode-webview://14rv7nefq8c5i58a0qj2bvo85gq74ruaqu5n0b8rukdjvkquuhot/index.html?id=3dc6504c-a30f-4a93-97e0-c69002ee2678&parentId=2&origin=d983d1a5-f5d2-4e69-9c0a-7d1568b6ebed&swVersion=4&extensionId=Anthropic.claude-code&platform=electron&vscode-resource-base-authority=vscode-resource.vscode-cdn.net&parentOrigin=vscode-file%3A%2F%2Fvscode-app&session=610f8b3a-7a09-408e-a1ad-a51c03a2df42) - 版本管理說明

### 🎓 重要經驗

1. **Semantic Release 有兩種模式**：
   - `--dry-run`: 只分析和預覽，不建立 tag
   - 正常模式: 真正發布版本，建立 tag
2. **版本號不會重複**：
   - 因為只有 main 分支會真正建立 tag
   - 其他分支只是預覽版本號
3. **語義化 Commit 的重要性**：
   - `feat:` → MINOR 版本
   - `fix:` → PATCH 版本
   - `BREAKING CHANGE` → MAJOR 版本
   - 其他類型（`docs:`, `chore:` 等）不觸發版本更新
4. **Git Flow 配置**：
   - 使用 `-n` 參數或全域設定避免自動建立 tag
   - 使用 `auto` 等臨時名稱而非版本號