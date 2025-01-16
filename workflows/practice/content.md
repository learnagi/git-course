# 实践练习

本节提供一系列实践练习，帮助你巩固 Git 工作流的知识。

## 基础工作流

### 练习 1：集中式工作流

1. 任务描述
- 创建中央仓库
- 克隆本地仓库
- 进行基本操作
- 处理冲突

2. 步骤指导
```bash
# 创建仓库
git init --bare central-repo.git

# 克隆仓库
git clone central-repo.git local-repo
cd local-repo

# 基本操作
echo "# Project" > README.md
git add README.md
git commit -m "docs: initial commit"
git push origin main
```

### 练习 2：特性分支工作流

1. 场景设置
- 创建特性分支
- 开发新功能
- 提交代码
- 合并特性

2. 解决步骤
```bash
# 创建特性分支
git checkout -b feature/user-profile

# 开发功能
echo "function userProfile() {}" > profile.js
git add profile.js
git commit -m "feat: add user profile"

# 合并特性
git checkout main
git merge feature/user-profile
```

## GitFlow 实践

### 练习 1：项目初始化

1. 基本设置
```bash
# 初始化 GitFlow
git flow init

# 创建开发分支
git checkout develop
echo "# Development" > DEVELOPMENT.md
git add DEVELOPMENT.md
git commit -m "docs: add development guide"
```

2. 特性开发
```bash
# 开始特性
git flow feature start auth

# 开发功能
echo "function auth() {}" > auth.js
git add auth.js
git commit -m "feat: implement authentication"

# 完成特性
git flow feature finish auth
```

### 练习 2：版本发布

1. 发布流程
```bash
# 创建发布
git flow release start 1.0.0

# 版本准备
echo "Version 1.0.0" > VERSION
git add VERSION
git commit -m "chore: prepare for 1.0.0"

# 完成发布
git flow release finish 1.0.0
```

2. 热修复
```bash
# 开始修复
git flow hotfix start 1.0.1

# 修复问题
echo "Bug fix" > fix.js
git add fix.js
git commit -m "fix: critical issue"

# 完成修复
git flow hotfix finish 1.0.1
```

## 主干开发实践

### 练习 1：持续集成

1. 配置 CI
```yaml
# .github/workflows/ci.yml
name: CI

on:
  push:
    branches: [ main ]
  pull_request:
    branches: [ main ]

jobs:
  test:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v2
      - name: Test
        run: npm test
```

2. 自动化测试
```bash
# 创建测试
echo "test('example', () => {})" > test.js
git add test.js
git commit -m "test: add example test"

# 运行测试
npm test
```

### 练习 2：特性开关

1. 实现特性
```javascript
// features.js
const features = {
  newUI: process.env.ENABLE_NEW_UI === 'true'
};

// app.js
if (features.newUI) {
  // 新 UI 代码
} else {
  // 旧 UI 代码
}
```

2. 配置管理
```bash
# 开发环境
echo "ENABLE_NEW_UI=true" > .env.development

# 生产环境
echo "ENABLE_NEW_UI=false" > .env.production
```

## 团队协作

### 练习 1：代码评审

1. 评审流程
```bash
# 创建分支
git checkout -b feature/new-feature

# 提交代码
git commit -m "feat: new feature"

# 创建 PR
gh pr create

# 评审代码
gh pr review
```

2. 评审标准
```markdown
## 评审清单
- [ ] 代码规范
- [ ] 测试覆盖
- [ ] 文档更新
- [ ] 性能考虑
```

### 练习 2：冲突解决

1. 模拟冲突
```bash
# 分支 1
git checkout -b feature1
echo "Version 1" > file.txt
git commit -am "feat: version 1"

# 分支 2
git checkout -b feature2 main
echo "Version 2" > file.txt
git commit -am "feat: version 2"
```

2. 解决冲突
```bash
# 合并分支
git checkout main
git merge feature1
git merge feature2

# 解决冲突
git mergetool
git commit -m "merge: resolve conflicts"
```

## 版本管理

### 练习 1：发布管理

1. 版本控制
```bash
# 创建标签
git tag -a v1.0.0 -m "Version 1.0.0"

# 推送标签
git push origin v1.0.0

# 创建发布说明
gh release create v1.0.0
```

2. 发布流程
```bash
# 创建发布分支
git checkout -b release/1.0.0

# 版本更新
echo "1.0.0" > VERSION
git commit -am "chore: bump version"

# 合并发布
git checkout main
git merge release/1.0.0
```

### 练习 2：变更管理

1. 更新日志
```markdown
# CHANGELOG.md
## [1.0.0] - 2025-01-16
### Added
- User authentication
- Profile management

### Fixed
- Data validation
- UI responsiveness
```

2. 版本回滚
```bash
# 创建回滚分支
git checkout -b rollback-1.0.0

# 回滚操作
git revert HEAD

# 合并回滚
git checkout main
git merge rollback-1.0.0
```

## 工作流优化

### 练习 1：自动化配置

1. Git 钩子
```bash
# pre-commit 钩子
cat > .git/hooks/pre-commit << 'EOF'
#!/bin/sh
npm test
npm run lint
EOF
chmod +x .git/hooks/pre-commit
```

2. 提交模板
```bash
# 创建模板
cat > .gitmessage << 'EOF'
type(scope): subject

body

BREAKING CHANGE:
Closes #
EOF

# 配置模板
git config commit.template .gitmessage
```

### 练习 2：工具集成

1. IDE 配置
```json
{
  "git.enableSmartCommit": true,
  "git.confirmSync": false,
  "git.autofetch": true
}
```

2. 命令别名
```bash
# 配置别名
git config --global alias.st status
git config --global alias.co checkout
git config --global alias.br branch
git config --global alias.ci commit
```

## 问题排查

### 场景 1：提交问题

1. 提交回滚
```bash
# 查看历史
git log --oneline

# 回滚提交
git revert HEAD

# 修改提交
git commit --amend
```

2. 历史清理
```bash
# 交互式变基
git rebase -i HEAD~3

# 压缩提交
git reset --soft HEAD~3
git commit -m "feat: combined changes"
```

### 场景 2：分支问题

1. 分支同步
```bash
# 更新分支
git fetch origin
git rebase origin/main

# 强制更新
git reset --hard origin/main
```

2. 分支清理
```bash
# 删除已合并分支
git branch --merged | grep -v "\*" | xargs -n 1 git branch -d

# 删除远程分支
git push origin --delete branch-name
```

## 最佳实践总结

### 1. 工作流程

1. 日常工作
```bash
# 同步代码
git pull --rebase

# 创建分支
git checkout -b feature/new-feature

# 提交代码
git commit -m "feat: add feature"

# 推送更改
git push origin feature/new-feature
```

2. 代码评审
```bash
# 创建 PR
gh pr create

# 评审代码
gh pr review

# 合并 PR
gh pr merge
```

### 2. 质量控制

1. 测试流程
```bash
# 运行测试
npm test

# 代码检查
npm run lint

# 构建检查
npm run build
```

2. 发布流程
```bash
# 版本更新
npm version patch

# 生成日志
npm run changelog

# 创建发布
gh release create
```

## 学习要点
1. 实践不同工作流
2. 掌握团队协作
3. 处理常见问题
4. 优化工作流程

## 小结
通过这些练习，你应该能够熟练运用不同的 Git 工作流，并在实际项目中选择和优化适合的工作流程。

## 下一步
1. 尝试更多场景
2. 优化工作流程
3. 自动化工具
4. 分享经验
