# 工作流基础

本节将介绍 Git 工作流的基本概念和原则，帮助你理解和选择合适的工作流程。

## 工作流概念

### 1. 基本定义

1. 工作流特点
- 分支策略
- 协作模式
- 发布流程
- 质量控制

2. 核心要素
- 主分支管理
- 特性开发
- 代码审查
- 版本发布

### 2. 工作流类型

1. 集中式工作流
```bash
# 克隆仓库
git clone repository-url

# 直接在主分支工作
git pull origin main
git commit -m "feat: add feature"
git push origin main
```

2. 特性分支工作流
```bash
# 创建特性分支
git checkout -b feature/new-feature

# 完成后合并
git checkout main
git merge feature/new-feature
```

## 分支策略

### 1. 分支类型

1. 长期分支
```bash
# 主分支
git checkout main

# 开发分支
git checkout develop
```

2. 临时分支
```bash
# 特性分支
git checkout -b feature/user-auth

# 修复分支
git checkout -b hotfix/bug-fix
```

### 2. 分支命名

1. 命名规范
```bash
# 特性分支
feature/feature-name
feature/JIRA-123

# 修复分支
bugfix/issue-description
hotfix/critical-bug
```

2. 版本分支
```bash
# 发布分支
release/1.0.0
release/2021-Q1

# 标签
git tag -a v1.0.0 -m "Version 1.0.0"
```

## 提交规范

### 1. 提交信息

1. 基本格式
```bash
# 提交格式
<type>(<scope>): <subject>

# 示例
feat(auth): add user authentication
fix(api): resolve data parsing issue
```

2. 类型定义
- feat: 新功能
- fix: 修复
- docs: 文档
- style: 格式
- refactor: 重构
- test: 测试
- chore: 维护

### 2. 提交策略

1. 原子提交
```bash
# 单一功能
git add auth.js
git commit -m "feat(auth): implement login function"

# 单一修复
git add api.js
git commit -m "fix(api): handle null response"
```

2. 提交模板
```bash
# 创建模板
git config --global commit.template .gitmessage

# 模板内容
feat(scope): subject

body

BREAKING CHANGE:
Closes #
```

## 代码评审

### 1. 评审流程

1. 创建请求
```bash
# 推送分支
git push origin feature/new-feature

# 创建 Pull Request
gh pr create
```

2. 评审操作
```bash
# 查看变更
git diff main...feature/new-feature

# 添加评论
gh pr review
```

### 2. 评审标准

1. 代码质量
- 代码风格
- 测试覆盖
- 性能影响
- 安全考虑

2. 评审清单
```markdown
## 评审要点
- [ ] 代码规范
- [ ] 测试用例
- [ ] 文档更新
- [ ] 性能检查
```

## 发布流程

### 1. 版本管理

1. 语义化版本
```bash
# 主版本
git tag -a v1.0.0 -m "Major release"

# 次版本
git tag -a v1.1.0 -m "Minor release"

# 补丁版本
git tag -a v1.1.1 -m "Patch release"
```

2. 发布说明
```markdown
# Release Notes v1.0.0

## Features
- User authentication
- API integration

## Bug Fixes
- Fixed data parsing
- Resolved UI issues
```

### 2. 发布策略

1. 常规发布
```bash
# 创建发布分支
git checkout -b release/1.0.0

# 版本修复
git commit -m "chore: prepare for 1.0.0"

# 合并发布
git checkout main
git merge release/1.0.0
```

2. 紧急修复
```bash
# 创建热修复分支
git checkout -b hotfix/critical-bug main

# 修复问题
git commit -m "fix: resolve critical issue"

# 合并修复
git checkout main
git merge hotfix/critical-bug
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

### 2. 自动化流程

1. 测试自动化
```bash
# 提交前测试
npm test

# 推送前检查
git push --dry-run
```

2. 部署自动化
```yaml
deploy:
  stage: deploy
  script:
    - deploy.sh
  only:
    - main
```

## 最佳实践

### 1. 工作建议

1. 分支管理
- 保持主分支稳定
- 及时清理过期分支
- 避免长期分支
- 定期同步上游

2. 提交管理
- 清晰的提交信息
- 适当的提交粒度
- 及时的代码评审
- 完整的测试覆盖

### 2. 团队协作

1. 沟通规范
```markdown
## 团队规范
1. 每日同步进度
2. 及时反馈问题
3. 共享技术文档
4. 定期代码评审
```

2. 文档维护
```markdown
## 项目文档
1. README.md
2. CONTRIBUTING.md
3. CHANGELOG.md
4. SECURITY.md
```

## 工具支持

### 1. 开发工具

1. IDE 集成
```json
{
  "git.enableSmartCommit": true,
  "git.confirmSync": false,
  "git.autofetch": true
}
```

2. 命令行工具
```bash
# Git 别名
git config --global alias.st status
git config --global alias.co checkout
git config --global alias.br branch
```

### 2. 辅助工具

1. 代码检查
```bash
# ESLint
npm run lint

# Prettier
npm run format
```

2. 提交检查
```bash
# Husky
npm install husky
npx husky add .husky/pre-commit "npm test"
```

## 学习要点
1. 理解工作流概念
2. 掌握分支策略
3. 规范提交流程
4. 实践代码评审

## 小结
工作流是团队协作的基础。通过本节的学习，你应该能够理解工作流的基本概念和原则，为选择合适的工作流程打下基础。

## 练习题
1. 创建分支策略
2. 实践提交规范
3. 模拟代码评审
4. 配置持续集成
