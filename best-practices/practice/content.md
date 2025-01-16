# 最佳实践练习

本节提供一系列实践练习，帮助你掌握 Git 最佳实践。

## 工作流练习

### 练习 1：分支管理

1. 任务描述
- 创建分支结构
- 实施分支策略
- 管理分支生命周期
- 处理分支合并

2. 实践步骤
```bash
# 初始化仓库
git init practice-repo
cd practice-repo

# 创建主分支
echo "# Project" > README.md
git add README.md
git commit -m "docs: initial commit"

# 创建开发分支
git checkout -b develop
echo "Development branch" >> README.md
git commit -am "docs: add development info"

# 创建特性分支
git checkout -b feature/user-auth
echo "function auth() {}" > auth.js
git add auth.js
git commit -m "feat: add user authentication"
```

### 练习 2：提交规范

1. 场景设置
- 配置提交模板
- 规范提交信息
- 使用提交工具
- 管理提交历史

2. 解决步骤
```bash
# 配置提交模板
cat > .gitmessage << 'EOF'
<type>(<scope>): <subject>

<body>

<footer>
EOF

git config --global commit.template .gitmessage

# 安装提交工具
npm install --save-dev commitizen
npm install --save-dev @commitlint/cli
npm install --save-dev @commitlint/config-conventional

# 配置提交检查
cat > .commitlintrc.json << 'EOF'
{
  "extends": ["@commitlint/config-conventional"]
}
EOF

# 实践提交
git commit -m "feat(auth): implement user login"
git commit -m "fix(auth): resolve session issue"
```

## 团队协作练习

### 练习 1：代码评审

1. 评审流程
```bash
# 创建评审分支
git checkout -b review/login-feature

# 添加代码
echo "function login() {}" > login.js
git add login.js
git commit -m "feat: add login function"

# 创建 PR
gh pr create

# 评审代码
gh pr review
```

2. 评审标准
```markdown
## 评审清单
1. 代码质量
   - 代码规范
   - 命名规则
   - 注释完整
   - 错误处理

2. 功能完整
   - 需求覆盖
   - 边界处理
   - 异常处理
   - 兼容性

3. 测试覆盖
   - 单元测试
   - 集成测试
   - 性能测试
   - 安全测试
```

### 练习 2：持续集成

1. CI 配置
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
      - name: Setup Node.js
        uses: actions/setup-node@v2
        with:
          node-version: '16'
      - name: Install dependencies
        run: npm ci
      - name: Run tests
        run: npm test
      - name: Run linters
        run: |
          npm run lint
          npm run prettier
```

2. 自动化测试
```javascript
// test/login.test.js
describe('Login Function', () => {
  test('should login with valid credentials', () => {
    expect(login('user', 'pass')).toBeTruthy();
  });

  test('should fail with invalid credentials', () => {
    expect(login('user', 'wrong')).toBeFalsy();
  });
});
```

## 质量控制练习

### 练习 1：代码检查

1. 配置工具
```bash
# 安装工具
npm install --save-dev eslint prettier husky lint-staged

# 配置 ESLint
cat > .eslintrc.json << 'EOF'
{
  "extends": ["eslint:recommended"],
  "rules": {
    "indent": ["error", 2],
    "quotes": ["error", "single"]
  }
}
EOF

# 配置 Prettier
cat > .prettierrc << 'EOF'
{
  "singleQuote": true,
  "trailingComma": "es5",
  "printWidth": 80
}
EOF

# 配置 lint-staged
cat > .lintstagedrc << 'EOF'
{
  "*.js": ["eslint --fix", "prettier --write"],
  "*.{json,md}": ["prettier --write"]
}
EOF
```

2. 实践检查
```bash
# 创建测试文件
cat > test.js << 'EOF'
function   badFormatting(  ) {
    console.log("Hello World");
}
EOF

# 运行检查
npx eslint test.js
npx prettier --write test.js
```

### 练习 2：测试覆盖

1. 测试配置
```javascript
// jest.config.js
module.exports = {
  collectCoverage: true,
  coverageThreshold: {
    global: {
      branches: 80,
      functions: 80,
      lines: 80,
      statements: 80
    }
  }
};

// package.json
{
  "scripts": {
    "test": "jest",
    "test:coverage": "jest --coverage"
  }
}
```

2. 测试实践
```javascript
// src/calculator.js
class Calculator {
  add(a, b) {
    return a + b;
  }
  subtract(a, b) {
    return a - b;
  }
}

// test/calculator.test.js
describe('Calculator', () => {
  const calc = new Calculator();

  test('should add numbers correctly', () => {
    expect(calc.add(1, 2)).toBe(3);
    expect(calc.add(-1, 1)).toBe(0);
  });

  test('should subtract numbers correctly', () => {
    expect(calc.subtract(3, 2)).toBe(1);
    expect(calc.subtract(1, 1)).toBe(0);
  });
});
```

## 文档管理练习

### 练习 1：项目文档

1. 基本文档
```markdown
# Project Name

## Description
Brief description of the project.

## Installation
```bash
npm install
```

## Usage
```javascript
const app = require('./app');
app.start();
```

## Contributing
Please read [CONTRIBUTING.md](CONTRIBUTING.md) for details.

## License
This project is licensed under the MIT License.
```

2. 技术文档
```markdown
# API Documentation

## Authentication
### Login
POST /api/login

Request:
```json
{
  "username": "string",
  "password": "string"
}
```

Response:
```json
{
  "token": "string",
  "user": {
    "id": "string",
    "name": "string"
  }
}
```
```

### 练习 2：知识库

1. 最佳实践
```markdown
# Git 最佳实践

## 分支管理
1. 使用有意义的分支名
2. 及时删除已合并分支
3. 保持分支最新
4. 避免长期分支

## 提交规范
1. 使用规范的提交信息
2. 保持提交原子性
3. 及时提交
4. 写好提交说明
```

2. 常见问题
```markdown
# 常见问题解决

## 合并冲突
1. 问题描述
   合并分支时出现冲突

2. 解决步骤
   ```bash
   # 更新分支
   git fetch origin
   git rebase origin/main

   # 解决冲突
   git mergetool

   # 继续变基
   git rebase --continue
   ```

## 提交错误
1. 问题描述
   提交了错误的更改

2. 解决步骤
   ```bash
   # 撤销最近提交
   git reset --soft HEAD^

   # 修改提交
   git commit --amend
   ```
```

## 工具配置练习

### 练习 1：IDE 配置

1. VS Code 设置
```json
{
  "git.enableSmartCommit": true,
  "git.confirmSync": false,
  "git.autofetch": true,
  "git.pruneOnFetch": true,
  "git.inputValidation": "warn",
  "git.detectSubmodules": false,
  "git.detectSubmodulesLimit": 50
}
```

2. 插件配置
```bash
# 安装插件
code --install-extension eamodio.gitlens
code --install-extension mhutchie.git-graph
code --install-extension donjayamanne.githistory

# Git 工具配置
git config --global core.editor "code --wait"
git config --global diff.tool vscode
git config --global merge.tool vscode
```

### 练习 2：自动化工具

1. 预提交钩子
```bash
# 安装 husky
npm install husky --save-dev

# 配置钩子
npx husky add .husky/pre-commit "npm test"
npx husky add .husky/pre-push "npm run build"

# 创建检查脚本
cat > .husky/check-branch-name.sh << 'EOF'
#!/bin/bash
branch="$(git rev-parse --abbrev-ref HEAD)"
if ! [[ $branch =~ ^(feature|bugfix|release|hotfix)/ ]]; then
  echo "Branch name must start with feature/, bugfix/, release/ or hotfix/"
  exit 1
fi
EOF

chmod +x .husky/check-branch-name.sh
```

2. CI/CD 配置
```yaml
# .github/workflows/cicd.yml
name: CI/CD

on:
  push:
    branches: [ main, develop ]
  pull_request:
    branches: [ main, develop ]

jobs:
  pipeline:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v2
      
      - name: Setup
        uses: actions/setup-node@v2
        with:
          node-version: '16'
          
      - name: Install
        run: npm ci
        
      - name: Lint
        run: |
          npm run lint
          npm run prettier
          
      - name: Test
        run: npm test
        
      - name: Build
        run: npm run build
        
      - name: Deploy
        if: github.ref == 'refs/heads/main'
        run: npm run deploy
```

## 安全实践练习

### 练习 1：凭证管理

1. SSH 配置
```bash
# 生成密钥
ssh-keygen -t ed25519 -C "email@example.com"

# 添加密钥
ssh-add ~/.ssh/id_ed25519

# 配置 config
cat > ~/.ssh/config << 'EOF'
Host github.com
  IdentityFile ~/.ssh/id_ed25519
  UseKeychain yes
  AddKeysToAgent yes
EOF

# 测试连接
ssh -T git@github.com
```

2. GPG 配置
```bash
# 生成密钥
gpg --full-generate-key

# 配置 Git
git config --global user.signingkey <KEY-ID>
git config --global commit.gpgsign true

# 测试签名
git commit -S -m "feat: signed commit"
```

### 练习 2：安全检查

1. 代码扫描
```yaml
# .github/workflows/security.yml
name: Security Scan

on:
  push:
    branches: [ main ]
  schedule:
    - cron: '0 0 * * 0'

jobs:
  scan:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v2
      
      - name: Run security audit
        run: npm audit
        
      - name: Run SAST
        uses: github/codeql-action/analyze@v1
```

2. 敏感信息
```bash
# 配置 .gitignore
cat > .gitignore << 'EOF'
# Secrets
.env
*.key
*.pem
config/secrets.yml

# Dependencies
node_modules/
vendor/

# Build
dist/
build/
EOF

# 安装安全工具
npm install --save-dev git-secrets

# 配置检查
git secrets --install
git secrets --register-aws
```

## 最佳实践总结

### 1. 日常实践

1. 工作流程
```markdown
## 每日工作流
1. 更新代码
   ```bash
   git fetch origin
   git rebase origin/main
   ```

2. 开发功能
   ```bash
   git checkout -b feature/new-feature
   # 开发代码
   git commit -m "feat: add new feature"
   ```

3. 提交评审
   ```bash
   gh pr create
   ```

4. 合并代码
   ```bash
   git checkout main
   git merge feature/new-feature
   ```
```

2. 质量控制
```bash
# 运行测试
npm test

# 代码检查
npm run lint

# 格式化代码
npm run prettier

# 安全检查
npm audit
```

### 2. 团队实践

1. 协作规范
```markdown
## 团队规范
1. 分支管理
   - 使用规范的分支名
   - 及时清理分支
   - 保护重要分支

2. 提交规范
   - 清晰的提交信息
   - 合理的提交粒度
   - 签名重要提交

3. 评审规范
   - 及时评审
   - 详细反馈
   - 跟进修改
```

2. 持续改进
```markdown
## 改进计划
1. 定期回顾
   - 收集反馈
   - 分析问题
   - 制定改进

2. 技术提升
   - 工具培训
   - 最佳实践
   - 经验分享
```

## 学习要点
1. 实践工作流程
2. 优化团队协作
3. 加强质量控制
4. 注重安全管理

## 小结
通过这些练习，你应该能够熟练运用 Git 最佳实践，并在实际项目中建立高效的开发流程。

## 下一步
1. 深入学习工具
2. 优化工作流程
3. 实施自动化
4. 分享实践经验
