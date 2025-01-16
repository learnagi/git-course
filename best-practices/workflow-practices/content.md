# 工作流最佳实践

本节将介绍 Git 工作流的最佳实践和建议，帮助你建立高效的开发流程。

## 分支管理

### 1. 分支策略

1. 分支类型
```bash
# 长期分支
- main/master：主分支
- develop：开发分支

# 临时分支
- feature/*：特性分支
- bugfix/*：修复分支
- release/*：发布分支
- hotfix/*：热修复分支
```

2. 分支命名
```bash
# 特性分支
feature/user-auth
feature/JIRA-123-payment-api

# 修复分支
bugfix/login-issue
bugfix/JIRA-456-memory-leak

# 发布分支
release/1.0.0
release/2023-Q4
```

### 2. 分支操作

1. 创建分支
```bash
# 创建特性分支
git checkout -b feature/new-feature develop

# 创建修复分支
git checkout -b bugfix/issue-123 main

# 创建发布分支
git checkout -b release/1.0.0 develop
```

2. 分支管理
```bash
# 列出分支
git branch -a

# 删除已合并分支
git branch --merged |
  grep -v "\*" |
  grep -v "main" |
  grep -v "develop" |
  xargs -n 1 git branch -d

# 清理远程分支
git remote prune origin
```

## 提交规范

### 1. 提交信息

1. 提交格式
```bash
# 创建提交模板
cat > .gitmessage << 'EOF'
<type>(<scope>): <subject>

<body>

<footer>
EOF

# 配置模板
git config --global commit.template .gitmessage
```

2. 提交类型
```markdown
## 提交类型
- feat: 新功能
- fix: 修复
- docs: 文档
- style: 格式
- refactor: 重构
- test: 测试
- chore: 其他
```

### 2. 提交操作

1. 提交准备
```bash
# 查看更改
git status
git diff

# 暂存文件
git add -p
git add <file>

# 提交更改
git commit
```

2. 提交管理
```bash
# 修改提交
git commit --amend

# 压缩提交
git rebase -i HEAD~3

# 拆分提交
git reset -p HEAD^
```

## 代码评审

### 1. 评审流程

1. 准备工作
```bash
# 更新代码
git fetch origin
git rebase origin/main

# 创建评审分支
git checkout -b review/feature-name

# 推送分支
git push -u origin review/feature-name
```

2. 评审标准
```markdown
## 评审清单
- [ ] 代码规范
- [ ] 测试覆盖
- [ ] 性能影响
- [ ] 安全考虑
- [ ] 文档更新
```

### 2. 评审工具

1. GitHub 流程
```bash
# 创建 PR
gh pr create

# 查看评审
gh pr list

# 合并 PR
gh pr merge
```

2. GitLab 流程
```bash
# 创建 MR
glab mr create

# 查看评审
glab mr list

# 合并 MR
glab mr merge
```

## 持续集成

### 1. CI 配置

1. GitHub Actions
```yaml
# .github/workflows/ci.yml
name: CI

on:
  push:
    branches: [ main, develop ]
  pull_request:
    branches: [ main, develop ]

jobs:
  test:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v2
      - name: Run tests
        run: npm test
```

2. GitLab CI
```yaml
# .gitlab-ci.yml
stages:
  - test
  - build
  - deploy

test:
  stage: test
  script:
    - npm test
```

### 2. 自动化检查

1. 预提交检查
```bash
# 安装 husky
npm install husky --save-dev

# 配置钩子
npx husky add .husky/pre-commit "npm test"
npx husky add .husky/pre-push "npm run build"
```

2. 代码检查
```json
{
  "scripts": {
    "lint": "eslint .",
    "test": "jest",
    "build": "webpack"
  }
}
```

## 发布管理

### 1. 版本控制

1. 版本规范
```bash
# 主版本
v1.0.0

# 次版本
v1.1.0

# 补丁版本
v1.1.1
```

2. 版本管理
```bash
# 创建标签
git tag -a v1.0.0 -m "Version 1.0.0"

# 推送标签
git push origin v1.0.0

# 删除标签
git tag -d v1.0.0
```

### 2. 发布流程

1. 发布准备
```bash
# 创建发布分支
git checkout -b release/1.0.0 develop

# 版本更新
npm version patch
git add package.json
git commit -m "chore: bump version to 1.0.0"
```

2. 发布完成
```bash
# 合并到主分支
git checkout main
git merge --no-ff release/1.0.0

# 创建标签
git tag -a v1.0.0 -m "Version 1.0.0"

# 清理分支
git branch -d release/1.0.0
```

## 文档管理

### 1. 文档规范

1. 基本文档
```markdown
## 必备文档
- README.md
- CONTRIBUTING.md
- CHANGELOG.md
- LICENSE
```

2. 文档内容
```markdown
## README.md 结构
1. 项目简介
2. 安装说明
3. 使用方法
4. 贡献指南
5. 许可说明
```

### 2. 文档维护

1. 更新流程
```bash
# 更新文档
git checkout -b docs/update-readme
echo "New content" >> README.md
git commit -am "docs: update readme"

# 评审文档
gh pr create
```

2. 版本文档
```markdown
## CHANGELOG.md
### [1.0.0] - 2025-01-16
#### Added
- 新功能 A
- 新功能 B

#### Fixed
- 修复问题 X
- 修复问题 Y
```

## 工具集成

### 1. IDE 配置

1. VS Code 设置
```json
{
  "git.enableSmartCommit": true,
  "git.confirmSync": false,
  "git.autofetch": true,
  "git.pruneOnFetch": true
}
```

2. 插件配置
```bash
# 安装插件
code --install-extension eamodio.gitlens
code --install-extension mhutchie.git-graph

# Git 工具配置
git config --global core.editor "code --wait"
git config --global diff.tool vscode
```

### 2. 命令行工具

1. 别名配置
```bash
# 配置别名
git config --global alias.st status
git config --global alias.co checkout
git config --global alias.br branch
git config --global alias.ci commit
```

2. 工具增强
```bash
# 安装工具
npm install -g commitizen
npm install -g conventional-changelog-cli

# 配置工具
commitizen init cz-conventional-changelog
```

## 安全实践

### 1. 凭证管理

1. SSH 配置
```bash
# 生成密钥
ssh-keygen -t ed25519 -C "email@example.com"

# 添加密钥
ssh-add ~/.ssh/id_ed25519

# 测试连接
ssh -T git@github.com
```

2. 凭证存储
```bash
# 配置凭证
git config --global credential.helper store

# 清理凭证
git credential-cache exit
```

### 2. 敏感信息

1. 忽略文件
```bash
# .gitignore
*.env
*.key
*.pem
config/secrets.yml
```

2. 安全检查
```bash
# 安装工具
npm install -g git-secrets

# 配置检查
git secrets --install
git secrets --register-aws
```

## 最佳实践

### 1. 日常工作

1. 工作流程
- 及时提交
- 定期同步
- 分支管理
- 代码评审

2. 质量控制
- 编写测试
- 代码检查
- 性能优化
- 安全审查

### 2. 团队协作

1. 沟通规范
- 清晰提交
- 完整文档
- 及时反馈
- 知识共享

2. 流程优化
- 自动化工具
- 持续集成
- 定期回顾
- 持续改进

## 学习要点
1. 掌握分支策略
2. 规范提交信息
3. 实施代码评审
4. 管理发布流程

## 小结
通过本节的学习，你应该掌握了 Git 工作流的最佳实践。这些实践将帮助你建立高效的开发流程。

## 练习题
1. 实施分支策略
2. 规范提交信息
3. 配置持续集成
4. 管理版本发布
