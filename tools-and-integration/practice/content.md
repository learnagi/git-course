# 实践练习

本节提供一系列实践练习，帮助你巩固对 Git 工具和集成的理解。

## 图形界面工具练习

### 练习 1：基本操作

1. 任务描述
- 使用 SourceTree 克隆仓库
- 创建新分支
- 提交更改
- 合并分支

2. 步骤指导
```bash
# 克隆仓库
git clone https://github.com/example/repo.git

# 创建分支
git checkout -b feature/new-feature

# 提交更改
git add .
git commit -m "feat: add new feature"

# 合并分支
git checkout main
git merge feature/new-feature
```

### 练习 2：冲突解决

1. 场景设置
- 在两个分支修改同一文件
- 使用图形工具解决冲突
- 完成合并操作

2. 解决步骤
```bash
# 创建冲突
git checkout -b feature1
# 修改文件
git commit -am "change in feature1"

git checkout -b feature2 main
# 修改同一文件
git commit -am "change in feature2"

# 合并并解决冲突
git checkout main
git merge feature1
git merge feature2
```

## IDE 集成练习

### 练习 1：VS Code Git

1. 基本设置
```json
{
  "git.enabled": true,
  "git.autofetch": true,
  "git.confirmSync": false
}
```

2. 操作步骤
- 安装 GitLens 扩展
- 配置 Git 设置
- 使用 Git 面板
- 查看文件历史

### 练习 2：IDEA Git

1. 配置任务
- 设置 Git 可执行文件
- 配置提交模板
- 设置变更列表
- 配置代码审查

2. 实践步骤
```properties
# 配置 Git
Settings > Version Control > Git

# 设置提交模板
Settings > Version Control > Commit
```

## 持续集成练习

### 练习 1：GitHub Actions

1. 配置文件
```yaml
name: CI

on:
  push:
    branches: [ main ]
  pull_request:
    branches: [ main ]

jobs:
  build:
    runs-on: ubuntu-latest
    steps:
    - uses: actions/checkout@v2
    - name: Set up Node.js
      uses: actions/setup-node@v2
      with:
        node-version: '16'
    - name: Install dependencies
      run: npm install
    - name: Run tests
      run: npm test
```

2. 实现任务
- 创建工作流文件
- 配置构建步骤
- 添加测试任务
- 设置部署流程

### 练习 2：GitLab CI

1. 配置文件
```yaml
stages:
  - build
  - test
  - deploy

build:
  stage: build
  script:
    - npm install
    - npm run build

test:
  stage: test
  script:
    - npm test

deploy:
  stage: deploy
  script:
    - echo "Deploying..."
  only:
    - main
```

2. 实现步骤
- 创建 .gitlab-ci.yml
- 配置构建阶段
- 添加测试阶段
- 设置部署阶段

## 综合实践

### 练习 1：项目工作流

1. 需求描述
- 创建新项目
- 设置 Git 工作流
- 配置 CI/CD
- 实现自动部署

2. 实现步骤
```bash
# 初始化项目
git init
npm init

# 配置工作流
git flow init

# 设置 CI/CD
# 创建 .github/workflows/ci.yml
```

### 练习 2：团队协作

1. 场景设置
- 多人协作项目
- 分支管理策略
- 代码评审流程
- 自动化测试

2. 工作流程
```bash
# 创建功能分支
git checkout -b feature/user-auth

# 提交代码
git add .
git commit -m "feat: implement user authentication"

# 创建 Pull Request
gh pr create

# 代码评审
gh pr review
```

## 进阶挑战

### 挑战 1：自定义工具

1. 任务目标
- 创建 Git 别名
- 编写自定义脚本
- 集成到工作流
- 优化工作效率

2. 示例实现
```bash
# 创建别名
git config --global alias.st status
git config --global alias.co checkout
git config --global alias.br branch
git config --global alias.ci commit

# 自定义脚本
#!/bin/bash
# git-cleanup
git branch --merged | grep -v "\*" | xargs -n 1 git branch -d
```

### 挑战 2：工作流优化

1. 优化目标
- 提高构建速度
- 优化测试流程
- 自动化部署
- 监控和报告

2. 实现方案
```yaml
# GitHub Actions
jobs:
  build:
    steps:
      - uses: actions/cache@v2
        with:
          path: ~/.npm
          key: ${{ runner.os }}-node-${{ hashFiles('**/package-lock.json') }}
      
      - name: Test
        run: npm test -- --coverage
      
      - name: Upload coverage
        uses: codecov/codecov-action@v2
```

## 问题解决

### 场景 1：合并冲突

1. 问题描述
- 多人同时修改
- 冲突文件处理
- 保持代码质量

2. 解决方案
```bash
# 查看冲突
git status

# 解决冲突
# 使用图形工具或编辑器

# 完成合并
git add .
git commit -m "resolve conflicts"
```

### 场景 2：CI 失败

1. 问题分析
- 查看错误日志
- 定位问题原因
- 本地验证

2. 解决步骤
```bash
# 查看日志
gh run view

# 本地测试
npm test

# 修复问题
git commit -m "fix: resolve test failures"
```

## 最佳实践总结

### 1. 工具使用

1. 选择合适工具
- 项目需求
- 团队熟悉度
- 维护成本
- 扩展性

2. 工具配置
```json
{
  "editor.formatOnSave": true,
  "git.enableSmartCommit": true,
  "git.confirmSync": false
}
```

### 2. 工作流程

1. 分支策略
```bash
# 主分支
main

# 开发分支
develop

# 功能分支
feature/*

# 发布分支
release/*
```

2. 提交规范
```bash
# 提交格式
type(scope): message

# 示例
feat(auth): implement user authentication
fix(api): resolve data parsing issue
```

## 学习要点
1. 掌握工具使用
2. 理解集成流程
3. 实践工作流程
4. 解决常见问题

## 小结
通过这些练习，你应该能够熟练使用各种 Git 工具和集成功能，并能够在实际项目中应用这些知识。

## 下一步
1. 尝试更多工具
2. 优化工作流程
3. 探索新功能
4. 分享经验
