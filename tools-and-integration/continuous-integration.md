---
title: "持续集成"
slug: "continuous-integration"
description: "掌握 Git 与 CI/CD 的集成"
is_published: true
estimated_minutes: 30
---

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
        node-version: [14.x, 16.x, 18.x]
    steps:
    - uses: actions/checkout@v2
    - name: Use Node.js ${{ matrix.node-version }}
      uses: actions/setup-node@v2
      with:
        node-version: ${{ matrix.node-version }}
    - run: npm test
```

2. 工作流调度
```yaml
on:
  schedule:
    - cron: '0 0 * * *'  # 每天午夜运行
  workflow_dispatch:     # 手动触发
```

## Jenkins

### 基本配置

1. Jenkinsfile
```groovy
pipeline {
    agent any
    
    stages {
        stage('Build') {
            steps {
                sh 'npm install'
            }
        }
        stage('Test') {
            steps {
                sh 'npm test'
            }
        }
        stage('Deploy') {
            steps {
                sh 'npm run build'
            }
        }
    }
    
    post {
        always {
            cleanWs()
        }
    }
}
```

2. 多分支流水线
```groovy
properties([
    pipelineTriggers([pollSCM('H/15 * * * *')]),
    parameters([string(name: 'BRANCH_NAME', defaultValue: 'main')])
])

pipeline {
    agent any
    stages {
        stage('Checkout') {
            steps {
                git branch: params.BRANCH_NAME, url: 'https://github.com/user/repo.git'
            }
        }
        stage('Build') {
            steps {
                sh 'npm install'
                sh 'npm run build'
            }
        }
    }
}
```