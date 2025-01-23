---
title: "Git 进阶学习"
slug: "further-learning"
description: "探索 Git 的高级特性和集成应用，包括变基操作、子树操作、钩子脚本以及 CI/CD 集成等内容"
author: "Git Fun <support@git.fun>"
status: "published"
created_at: "2024-01-01"
updated_at: "2024-01-01"
estimated_minutes: 45
---

# Git 进阶学习

本节将介绍 Git 的高级特性和集成应用，帮助你更深入地理解和使用 Git。通过学习本章节，你将掌握：

- 使用变基操作优化提交历史
- 管理复杂项目中的子树
- 利用钩子脚本自动化工作流程
- 集成 CI/CD 实现自动化部署

## 高级特性

### 变基操作

1. 交互式变基
```bash
# 开始变基
git rebase -i HEAD~3

# 变基命令
# p, pick = 使用提交
# r, reword = 修改提交信息
# e, edit = 修改提交
# s, squash = 合并到前一个提交
# f, fixup = 合并到前一个提交，丢弃信息
# d, drop = 删除提交
```

2. 变基策略
```bash
# 拆分提交
git rebase -i HEAD~1
# 编辑提交
git reset HEAD^
git add file1.txt
git commit -m "feat: first part"
git add file2.txt
git commit -m "feat: second part"
git rebase --continue

# 合并提交
git rebase -i HEAD~3
# 将后面的提交标记为 squash
```

### 子树操作

1. 子树添加
```bash
# 添加远程仓库
git remote add -f sub-repo https://git.fun/user/sub-repo.git

# 添加子树
git subtree add --prefix=sub-repo sub-repo main --squash

# 更新子树
git subtree pull --prefix=sub-repo sub-repo main --squash
```

2. 子树推送
```bash
# 推送更改
git subtree push --prefix=sub-repo sub-repo main

# 分割子树
git subtree split --prefix=sub-repo -b split-branch

# 提取子树
git subtree extract --prefix=sub-repo -b extract-branch
```

### 钩子脚本

1. 客户端钩子
```bash
# pre-commit 钩子
cat > .git/hooks/pre-commit << 'EOF'
#!/bin/sh
npm test
if [ $? -ne 0 ]; then
  echo "Tests failed, commit aborted"
  exit 1
fi
EOF
chmod +x .git/hooks/pre-commit

# commit-msg 钩子
cat > .git/hooks/commit-msg << 'EOF'
#!/bin/sh
commit_msg=$(cat $1)
if ! echo "$commit_msg" | grep -qE "^(feat|fix|docs|style|refactor|test|chore):";
then
  echo "Invalid commit message format"
  exit 1
fi
EOF
chmod +x .git/hooks/commit-msg
```

## 集成应用

### CI/CD 集成

1. GitHub Actions
```yaml
# .github/workflows/ci.yml
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
      - name: Setup Node.js
        uses: actions/setup-node@v2
        with:
          node-version: '16'
      - name: Install dependencies
        run: npm ci
      - name: Run tests
        run: npm test
```

2. GitLab CI/CD
```yaml
# .gitlab-ci.yml
image: node:16

stages:
  - test
  - build
  - deploy

test:
  stage: test
  script:
    - npm ci
    - npm test

build:
  stage: build
  script:
    - npm ci
    - npm run build
  artifacts:
    paths:
      - dist/

deploy:
  stage: deploy
  script:
    - npm ci
    - npm run deploy
  only:
    - tags
```

### 自动化部署

1. 部署钩子
```bash
# post-receive 钩子
cat > hooks/post-receive << 'EOF'
#!/bin/sh
GIT_WORK_TREE=/var/www/app git checkout -f
cd /var/www/app
npm install
npm run build
EOF
chmod +x hooks/post-receive
```

2. 持续部署
```yaml
# .github/workflows/cd.yml
name: CD

on:
  push:
    tags:
      - 'v*'

jobs:
  deploy:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v2
      - name: Build
        run: |
          npm ci
          npm run build
      - name: Deploy
        uses: peaceiris/actions-gh-pages@v3
        with:
          github_token: ${{ secrets.GITHUB_TOKEN }}
          publish_dir: ./dist
```