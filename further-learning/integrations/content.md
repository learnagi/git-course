# 集成应用

本节将介绍 Git 与其他工具的集成应用。

## CI/CD 集成

### 1. GitHub Actions

1. 基本配置
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

2. 高级配置
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

### 2. GitLab CI/CD

1. 基本配置
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

2. 高级配置
```yaml
# .gitlab-ci.yml
include:
  - template: Security/SAST.gitlab-ci.yml
  - template: Security/Dependency-Scanning.gitlab-ci.yml

variables:
  DOCKER_HOST: tcp://docker:2375
  DOCKER_DRIVER: overlay2

services:
  - docker:dind

before_script:
  - docker info

build:
  image: docker:latest
  stage: build
  script:
    - docker build -t $CI_REGISTRY_IMAGE:$CI_COMMIT_TAG .
    - docker push $CI_REGISTRY_IMAGE:$CI_COMMIT_TAG
```

## IDE 集成

### 1. VS Code

1. 基本设置
```json
{
  "git.enableSmartCommit": true,
  "git.confirmSync": false,
  "git.autofetch": true,
  "git.pruneOnFetch": true,
  "git.inputValidation": "warn",
  "git.detectSubmodules": true
}
```

2. 扩展配置
```bash
# 安装扩展
code --install-extension eamodio.gitlens
code --install-extension mhutchie.git-graph
code --install-extension donjayamanne.githistory

# 配置 GitLens
{
  "gitlens.currentLine.enabled": true,
  "gitlens.hovers.currentLine.over": "line",
  "gitlens.codeLens.enabled": true,
  "gitlens.statusBar.enabled": true
}
```

### 2. JetBrains IDE

1. 基本设置
```markdown
## Git 设置
1. Version Control > Git
   - Path to Git executable: /usr/bin/git
   - SSH executable: Native

2. Commit 设置
   - Force non-empty commit comments
   - Show commit options before commit
```

2. 插件配置
```markdown
## 推荐插件
1. .ignore
   - 支持各种忽略文件
   - 文件模板

2. Git Flow Integration
   - 图形化 Git Flow
   - 分支管理

3. GitToolBox
   - 提交历史
   - 行注释
```

## 容器集成

### 1. Docker

1. Dockerfile
```dockerfile
# Dockerfile
FROM node:16

WORKDIR /app

# 安装 Git
RUN apt-get update && \
    apt-get install -y git

# 克隆代码
RUN git clone https://github.com/user/repo.git .

# 构建应用
RUN npm ci
RUN npm run build

CMD ["npm", "start"]
```

2. Docker Compose
```yaml
# docker-compose.yml
version: '3'

services:
  app:
    build: .
    ports:
      - "3000:3000"
    environment:
      - GIT_USER=username
      - GIT_TOKEN=token
    volumes:
      - .:/app
      - ~/.gitconfig:/root/.gitconfig
```

### 2. Kubernetes

1. 部署配置
```yaml
# deployment.yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: git-app
spec:
  replicas: 3
  selector:
    matchLabels:
      app: git-app
  template:
    metadata:
      labels:
        app: git-app
    spec:
      containers:
      - name: git-app
        image: git-app:latest
        env:
        - name: GIT_USER
          valueFrom:
            secretKeyRef:
              name: git-credentials
              key: username
        - name: GIT_TOKEN
          valueFrom:
            secretKeyRef:
              name: git-credentials
              key: token
```

2. 密钥配置
```yaml
# secret.yaml
apiVersion: v1
kind: Secret
metadata:
  name: git-credentials
type: Opaque
data:
  username: base64-encoded-username
  token: base64-encoded-token
```

## 自动化集成

### 1. Husky

1. 基本配置
```json
{
  "scripts": {
    "prepare": "husky install"
  },
  "husky": {
    "hooks": {
      "pre-commit": "lint-staged",
      "commit-msg": "commitlint -E HUSKY_GIT_PARAMS"
    }
  }
}
```

2. 钩子配置
```bash
# 安装 husky
npm install husky --save-dev

# 添加钩子
npx husky add .husky/pre-commit "npm test"
npx husky add .husky/pre-push "npm run build"
npx husky add .husky/commit-msg "npx commitlint --edit $1"
```

### 2. Jenkins

1. Jenkinsfile
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
        
        stage('Deploy') {
            when {
                tag "v*"
            }
            steps {
                sh 'npm run deploy'
            }
        }
    }
}
```

2. 配置脚本
```groovy
// config.groovy
def gitConfig = [
    url: 'https://github.com/user/repo.git',
    branch: 'main',
    credentials: 'git-credentials'
]

def buildConfig = [
    nodeVersion: '16',
    npmRegistry: 'https://registry.npmjs.org/'
]

def deployConfig = [
    environment: 'production',
    domain: 'example.com'
]
```

## 监控集成

### 1. Prometheus

1. 配置文件
```yaml
# prometheus.yml
global:
  scrape_interval: 15s

scrape_configs:
  - job_name: 'git_metrics'
    static_configs:
      - targets: ['localhost:9090']
    metrics_path: '/metrics'
```

2. 监控指标
```python
# metrics.py
from prometheus_client import Counter, Gauge, Histogram

# 提交计数器
commits = Counter('git_commits_total', 'Total number of commits')

# 仓库大小
repo_size = Gauge('git_repo_size_bytes', 'Repository size in bytes')

# 提交延迟
commit_latency = Histogram('git_commit_latency_seconds',
                          'Time taken for commit operations')
```

### 2. Grafana

1. 仪表板配置
```json
{
  "dashboard": {
    "id": null,
    "title": "Git Metrics",
    "tags": ["git", "metrics"],
    "timezone": "browser",
    "panels": [
      {
        "title": "Commits per Day",
        "type": "graph",
        "datasource": "Prometheus",
        "targets": [
          {
            "expr": "rate(git_commits_total[1d])",
            "legendFormat": "Commits"
          }
        ]
      }
    ]
  }
}
```

2. 告警规则
```yaml
# alerts.yml
groups:
  - name: git_alerts
    rules:
      - alert: HighCommitRate
        expr: rate(git_commits_total[5m]) > 10
        for: 5m
        labels:
          severity: warning
        annotations:
          summary: High commit rate detected
```

## 工具集成

### 1. 代码质量

1. ESLint
```json
{
  "scripts": {
    "lint": "eslint ."
  },
  "husky": {
    "hooks": {
      "pre-commit": "npm run lint"
    }
  },
  "eslintConfig": {
    "extends": ["eslint:recommended"],
    "env": {
      "node": true,
      "es6": true
    }
  }
}
```

2. SonarQube
```yaml
# sonar-project.properties
sonar.projectKey=my-project
sonar.sources=src
sonar.tests=test
sonar.javascript.lcov.reportPaths=coverage/lcov.info
sonar.coverage.exclusions=test/**/*
```

### 2. 文档工具

1. GitBook
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

2. Docusaurus
```javascript
// docusaurus.config.js
module.exports = {
  title: 'Git Documentation',
  tagline: 'Comprehensive Git documentation',
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

## 学习要点
1. 掌握工具集成
2. 理解自动化流程
3. 配置监控系统
4. 优化开发体验

## 小结
通过本节的学习，你应该能够将 Git 与各种工具和平台进行集成，提高开发效率。

## 练习题
1. 配置 CI/CD
2. 设置开发工具
3. 实现自动化
4. 搭建监控系统
