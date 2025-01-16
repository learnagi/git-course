# 扩展学习练习

本节提供一系列实践练习，帮助你掌握 Git 扩展应用。

## 高级特性练习

### 练习 1：变基操作

1. 场景设置
```bash
# 初始化仓库
git init rebase-practice
cd rebase-practice

# 创建提交
echo "Initial content" > file.txt
git add file.txt
git commit -m "feat: initial commit"

# 创建分支
git checkout -b feature
echo "Feature content" >> file.txt
git commit -am "feat: add feature"
```

2. 练习步骤
```bash
# 交互式变基
git rebase -i HEAD~2

# 修改提交
git commit --amend

# 继续变基
git rebase --continue

# 处理冲突
git mergetool
```

### 练习 2：子树操作

1. 场景设置
```bash
# 创建主仓库
git init main-repo
cd main-repo

# 添加子仓库
git remote add -f sub-repo https://github.com/user/sub-repo.git

# 添加子树
git subtree add --prefix=sub-repo sub-repo main --squash
```

2. 练习步骤
```bash
# 更新子树
git subtree pull --prefix=sub-repo sub-repo main --squash

# 修改子树
echo "New content" > sub-repo/file.txt
git commit -am "feat: update sub-repo"

# 推送子树
git subtree push --prefix=sub-repo sub-repo main
```

## CI/CD 练习

### 练习 1：GitHub Actions

1. 配置文件
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
      - name: Setup Node.js
        uses: actions/setup-node@v2
        with:
          node-version: '16'
      - name: Install dependencies
        run: npm ci
      - name: Run tests
        run: npm test
```

2. 实践步骤
```bash
# 创建测试
cat > test.js << 'EOF'
test('example test', () => {
  expect(1 + 1).toBe(2);
});
EOF

# 提交更改
git add .github/workflows/ci.yml test.js
git commit -m "ci: add GitHub Actions workflow"

# 推送更改
git push origin main
```

### 练习 2：GitLab CI/CD

1. 配置文件
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
    - main
```

2. 实践步骤
```bash
# 创建构建脚本
cat > build.js << 'EOF'
console.log('Building project...');
EOF

# 更新 package.json
{
  "scripts": {
    "build": "node build.js",
    "test": "jest",
    "deploy": "echo 'Deploying...'"
  }
}

# 提交配置
git add .gitlab-ci.yml package.json build.js
git commit -m "ci: add GitLab CI configuration"
```

## 工具集成练习

### 练习 1：Husky

1. 安装配置
```bash
# 安装依赖
npm install --save-dev husky lint-staged prettier

# 配置 package.json
{
  "scripts": {
    "prepare": "husky install"
  },
  "lint-staged": {
    "*.js": [
      "prettier --write",
      "eslint --fix"
    ]
  }
}
```

2. 添加钩子
```bash
# 创建钩子
npx husky add .husky/pre-commit "npx lint-staged"
npx husky add .husky/commit-msg "npx commitlint --edit $1"

# 测试提交
echo "console.log('test')" > test.js
git add test.js
git commit -m "test: add test file"
```

### 练习 2：Docker

1. 配置文件
```dockerfile
# Dockerfile
FROM node:16

WORKDIR /app

COPY package*.json ./
RUN npm ci

COPY . .
RUN npm run build

CMD ["npm", "start"]
```

2. 构建运行
```bash
# 构建镜像
docker build -t git-app .

# 运行容器
docker run -p 3000:3000 git-app

# 查看日志
docker logs git-app
```

## 监控练习

### 练习 1：Prometheus

1. 配置文件
```yaml
# prometheus.yml
global:
  scrape_interval: 15s

scrape_configs:
  - job_name: 'git_metrics'
    static_configs:
      - targets: ['localhost:9090']
```

2. 实现指标
```python
# metrics.py
from prometheus_client import start_http_server, Counter

# 创建计数器
commits = Counter('git_commits_total', 'Total number of commits')

# 启动服务器
start_http_server(9090)

# 记录提交
commits.inc()
```

### 练习 2：Grafana

1. 仪表板配置
```json
{
  "dashboard": {
    "id": null,
    "title": "Git Metrics",
    "panels": [
      {
        "title": "Commits per Hour",
        "type": "graph",
        "datasource": "Prometheus",
        "targets": [
          {
            "expr": "rate(git_commits_total[1h])",
            "legendFormat": "Commits"
          }
        ]
      }
    ]
  }
}
```

2. 实践步骤
```bash
# 导入仪表板
curl -X POST -H "Content-Type: application/json" \
  -d @dashboard.json \
  http://localhost:3000/api/dashboards/db

# 配置数据源
curl -X POST -H "Content-Type: application/json" \
  -d '{"name":"Prometheus","type":"prometheus","url":"http://localhost:9090"}' \
  http://localhost:3000/api/datasources
```

## 文档集成练习

### 练习 1：GitBook

1. 配置文件
```json
{
  "title": "Git Guide",
  "description": "A comprehensive guide to Git",
  "structure": {
    "readme": "README.md",
    "summary": "SUMMARY.md"
  },
  "plugins": [
    "github",
    "edit-link",
    "anchors"
  ]
}
```

2. 创建内容
```markdown
# SUMMARY.md
* [简介](README.md)
* [基础知识](basics/README.md)
  * [安装配置](basics/installation.md)
  * [基本操作](basics/operations.md)
* [高级特性](advanced/README.md)
  * [分支管理](advanced/branching.md)
  * [工作流程](advanced/workflow.md)
```

### 练习 2：Docusaurus

1. 配置文件
```javascript
// docusaurus.config.js
module.exports = {
  title: 'Git Documentation',
  tagline: 'Learn Git the right way',
  url: 'https://your-docusaurus-site.com',
  baseUrl: '/',
  organizationName: 'your-org',
  projectName: 'git-docs',
  plugins: [
    '@docusaurus/plugin-content-docs',
    '@docusaurus/plugin-content-pages'
  ]
};
```

2. 创建文档
```markdown
# docs/intro.md
---
sidebar_position: 1
---

# Git 教程

欢迎学习 Git！本教程将帮助你掌握 Git 的基本概念和高级特性。

## 学习路径

1. 基础知识
2. 常用命令
3. 高级特性
4. 最佳实践
```

## 自动化练习

### 练习 1：Jenkins

1. 配置文件
```groovy
// Jenkinsfile
pipeline {
    agent any
    
    stages {
        stage('Checkout') {
            steps {
                git 'https://github.com/user/repo.git'
            }
        }
        
        stage('Build') {
            steps {
                sh 'npm ci'
                sh 'npm run build'
            }
        }
        
        stage('Test') {
            steps {
                sh 'npm test'
            }
        }
    }
}
```

2. 实践步骤
```bash
# 创建测试
cat > Jenkinsfile << 'EOF'
pipeline {
    agent any
    stages {
        stage('Test') {
            steps {
                sh 'echo "Testing..."'
            }
        }
    }
}
EOF

# 提交配置
git add Jenkinsfile
git commit -m "ci: add Jenkins pipeline"
```

### 练习 2：GitHub Apps

1. 配置文件
```json
{
  "name": "Git Helper",
  "version": "1.0.0",
  "description": "GitHub App for Git automation",
  "main": "index.js",
  "scripts": {
    "start": "node index.js"
  },
  "dependencies": {
    "probot": "^12.2.4"
  }
}
```

2. 实现功能
```javascript
// index.js
module.exports = app => {
  app.on('issues.opened', async context => {
    const issueComment = context.issue({
      body: 'Thanks for opening this issue!'
    });
    return context.octokit.issues.createComment(issueComment);
  });
};
```

## 代码质量练习

### 练习 1：ESLint

1. 配置文件
```json
{
  "extends": "eslint:recommended",
  "env": {
    "node": true,
    "es6": true
  },
  "rules": {
    "indent": ["error", 2],
    "quotes": ["error", "single"],
    "semi": ["error", "always"]
  }
}
```

2. 实践步骤
```bash
# 安装 ESLint
npm install --save-dev eslint

# 创建测试文件
echo 'function test() { console.log("test") }' > test.js

# 运行检查
npx eslint test.js

# 自动修复
npx eslint --fix test.js
```

### 练习 2：SonarQube

1. 配置文件
```properties
# sonar-project.properties
sonar.projectKey=my-project
sonar.sources=src
sonar.tests=test
sonar.javascript.lcov.reportPaths=coverage/lcov.info
sonar.coverage.exclusions=test/**/*
```

2. 实践步骤
```bash
# 创建源文件
mkdir -p src test
echo 'function add(a, b) { return a + b; }' > src/math.js

# 创建测试
echo 'test("add", () => { expect(add(1, 1)).toBe(2); });' > test/math.test.js

# 运行分析
sonar-scanner
```

## 学习要点
1. 实践高级特性
2. 配置自动化流程
3. 集成开发工具
4. 实现质量控制

## 小结
通过这些练习，你应该能够熟练运用 Git 的扩展特性，并在实际项目中实现自动化和质量控制。

## 下一步
1. 深入学习工具
2. 优化工作流程
3. 提高代码质量
4. 加强自动化
