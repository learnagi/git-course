# 持续集成

本节将介绍如何将 Git 与持续集成系统集成，实现自动化构建、测试和部署。

## GitHub Actions

### 基本配置

1. 工作流配置
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
    - name: Set up Node.js
      uses: actions/setup-node@v2
      with:
        node-version: '16'
    - name: Install dependencies
      run: npm install
    - name: Run tests
      run: npm test
```

2. 触发条件
```yaml
on:
  push:
    branches:
      - main
      - 'releases/**'
    tags:
      - v*
  pull_request:
    types: [opened, synchronize]
```

### 高级功能

1. 矩阵构建
```yaml
jobs:
  test:
    runs-on: ${{ matrix.os }}
    strategy:
      matrix:
        os: [ubuntu-latest, windows-latest]
        node: [14, 16, 18]
    steps:
      - uses: actions/checkout@v2
      - name: Use Node.js ${{ matrix.node }}
        uses: actions/setup-node@v2
        with:
          node-version: ${{ matrix.node }}
```

2. 缓存依赖
```yaml
jobs:
  build:
    steps:
      - uses: actions/cache@v2
        with:
          path: ~/.npm
          key: ${{ runner.os }}-node-${{ hashFiles('**/package-lock.json') }}
          restore-keys: |
            ${{ runner.os }}-node-
```

## GitLab CI/CD

### 基本配置

1. Pipeline 配置
```yaml
# .gitlab-ci.yml
stages:
  - build
  - test
  - deploy

build:
  stage: build
  script:
    - npm install
    - npm run build
  artifacts:
    paths:
      - dist/

test:
  stage: test
  script:
    - npm run test
```

2. 环境变量
```yaml
variables:
  NODE_ENV: production

job:
  variables:
    DB_URL: $CI_DB_URL
  script:
    - echo $DB_URL
```

### 高级特性

1. 并行作业
```yaml
test:
  parallel: 3
  script:
    - npm test -- --split=$CI_NODE_INDEX/$CI_NODE_TOTAL
```

2. 部署配置
```yaml
deploy:
  stage: deploy
  environment:
    name: production
    url: https://example.com
  script:
    - deploy-script.sh
  only:
    - main
```

## Jenkins

### 基本设置

1. Jenkinsfile
```groovy
pipeline {
    agent any
    stages {
        stage('Build') {
            steps {
                sh 'npm install'
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

2. 触发器配置
```groovy
pipeline {
    triggers {
        githubPush()
        pollSCM('H/15 * * * *')
    }
}
```

### 高级配置

1. 并行执行
```groovy
pipeline {
    stages {
        stage('Parallel Tests') {
            parallel {
                stage('Unit Tests') {
                    steps {
                        sh 'npm run test:unit'
                    }
                }
                stage('Integration Tests') {
                    steps {
                        sh 'npm run test:integration'
                    }
                }
            }
        }
    }
}
```

2. 环境配置
```groovy
pipeline {
    environment {
        DEPLOY_TO = 'production'
    }
    stages {
        stage('Deploy') {
            environment {
                SECRET_KEY = credentials('secret-key')
            }
            steps {
                sh './deploy.sh'
            }
        }
    }
}
```

## Travis CI

### 基本配置

1. 配置文件
```yaml
# .travis.yml
language: node_js
node_js:
  - "14"
  - "16"

install:
  - npm install

script:
  - npm test
```

2. 构建矩阵
```yaml
matrix:
  include:
    - node_js: "14"
      env: TEST_SUITE=unit
    - node_js: "16"
      env: TEST_SUITE=integration
```

### 部署配置

1. 自动部署
```yaml
deploy:
  provider: heroku
  api_key: $HEROKU_API_KEY
  app: myapp
  on:
    branch: main
```

2. 条件部署
```yaml
deploy:
  provider: script
  script: bash deploy.sh
  on:
    tags: true
```

## CircleCI

### 基本配置

1. 配置文件
```yaml
# .circleci/config.yml
version: 2.1
jobs:
  build:
    docker:
      - image: cimg/node:16.0
    steps:
      - checkout
      - run: npm install
      - run: npm test
```

2. 工作流配置
```yaml
workflows:
  version: 2
  build_and_test:
    jobs:
      - build
      - test:
          requires:
            - build
```

### 高级特性

1. 缓存配置
```yaml
jobs:
  build:
    steps:
      - restore_cache:
          keys:
            - v1-deps-{{ .Branch }}-{{ checksum "package.json" }}
      - save_cache:
          key: v1-deps-{{ .Branch }}-{{ checksum "package.json" }}
          paths:
            - node_modules
```

2. 并行测试
```yaml
jobs:
  test:
    parallelism: 3
    steps:
      - run:
          command: |
            TEST_FILES=$(circleci tests glob "test/**/*.js" | circleci tests split)
            npm test $TEST_FILES
```

## 最佳实践

### 1. 工作流设计

1. 分支策略
```yaml
# GitHub Actions
on:
  push:
    branches:
      - main
      - develop
      - 'feature/**'
```

2. 环境管理
```yaml
# GitLab CI
.deploy_template: &deploy_template
  script:
    - deploy.sh
  only:
    - main

deploy_staging:
  <<: *deploy_template
  variables:
    ENVIRONMENT: staging

deploy_production:
  <<: *deploy_template
  variables:
    ENVIRONMENT: production
```

### 2. 性能优化

1. 缓存策略
```yaml
# CircleCI
jobs:
  build:
    steps:
      - restore_cache:
          keys:
            - deps-{{ checksum "package-lock.json" }}
            - deps-
```

2. 并行化
```yaml
# Jenkins
parallel {
    stage('Unit Tests') {
        steps {
            sh 'npm run test:unit'
        }
    }
    stage('Integration Tests') {
        steps {
            sh 'npm run test:integration'
        }
    }
}
```

### 3. 安全实践

1. 密钥管理
```yaml
# GitHub Actions
jobs:
  deploy:
    steps:
      - name: Deploy
        env:
          SSH_KEY: ${{ secrets.SSH_KEY }}
        run: |
          echo "$SSH_KEY" > deploy_key
          chmod 600 deploy_key
```

2. 权限控制
```yaml
# GitLab CI
deploy:
  script:
    - deploy.sh
  only:
    - main
  when: manual
```

## 调试技巧

### 1. 日志分析

1. 查看构建日志
```bash
# GitHub Actions
gh run view

# GitLab CI
gitlab-runner --debug run
```

2. 调试构建
```yaml
# CircleCI
jobs:
  build:
    steps:
      - run:
          command: |
            set -x
            npm install
```

### 2. 问题排查

1. 本地测试
```bash
# GitHub Actions
act -n

# GitLab CI
gitlab-runner exec docker build
```

2. 环境检查
```bash
# Jenkins
sh 'printenv'

# Travis CI
travis lint .travis.yml
```

## 学习要点
1. 掌握 CI/CD 配置
2. 理解工作流设计
3. 熟悉性能优化
4. 了解安全实践

## 小结
持续集成是现代软件开发的重要组成部分。通过本节的学习，你应该能够配置和使用各种 CI/CD 工具。

## 练习题
1. 配置基本的 CI 流程
2. 实现自动化测试
3. 设置自动部署
4. 优化构建性能
