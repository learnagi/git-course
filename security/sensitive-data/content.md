# 敏感数据处理

本节将介绍如何处理和保护 Git 仓库中的敏感数据，包括预防措施和补救方法。

## 敏感数据识别

### 1. 常见类型

1. 凭证信息
- API 密钥
- 访问令牌
- 数据库密码
- 加密密钥

2. 个人信息
- 用户数据
- 邮箱地址
- 电话号码
- 身份证号

### 2. 检测方法

1. 手动检查
```bash
# 搜索敏感词
git grep -i "password"
git grep -i "api[_-]key"
git grep -i "secret"

# 检查特定文件
git log -p config.* | grep -i "password"
```

2. 自动化工具
```bash
# 使用 git-secrets
git secrets --register-aws
git secrets --scan

# 使用 GitGuardian
gg scan
```

## 预防措施

### 1. 配置文件

1. .gitignore
```bash
# 创建 .gitignore
touch .gitignore

# 添加规则
*.env
*.key
*secret*
config/database.yml
```

2. .gitattributes
```bash
# 创建 .gitattributes
touch .gitattributes

# 添加规则
*.key filter=git-crypt diff=git-crypt
sensitive/* filter=git-crypt diff=git-crypt
```

### 2. 钩子配置

1. pre-commit
```bash
#!/bin/sh
# .git/hooks/pre-commit

# 检查敏感信息
if git diff --cached | grep -i "password="
then
    echo "Error: Potential password in commit"
    exit 1
fi
```

2. pre-push
```bash
#!/bin/sh
# .git/hooks/pre-push

# 检查大文件
git diff --cached --name-only | while read file; do
    if [ $(git ls-files -s "$file" | cut -f2) -gt 10485760 ]; then
        echo "Error: $file is too large"
        exit 1
    fi
done
```

## 加密方案

### 1. git-crypt

1. 基本配置
```bash
# 安装
brew install git-crypt

# 初始化
git-crypt init

# 配置文件
echo "sensitive-file filter=git-crypt diff=git-crypt" >> .gitattributes
```

2. 用户管理
```bash
# 导出密钥
git-crypt export-key ~/git-crypt-key

# 添加用户
git-crypt add-gpg-user USER_ID

# 解锁仓库
git-crypt unlock
```

### 2. git-secret

1. 基本使用
```bash
# 初始化
git secret init

# 添加文件
git secret add sensitive.file

# 加密文件
git secret hide

# 解密文件
git secret reveal
```

2. 团队管理
```bash
# 添加用户
git secret tell user@email.com

# 重新加密
git secret hide -d

# 删除文件
git secret remove sensitive.file
```

## 环境变量

### 1. 本地环境

1. 环境文件
```bash
# 创建示例文件
cp .env.example .env

# 配置忽略
echo ".env" >> .gitignore
```

2. 变量管理
```bash
# 开发环境
export DEV_API_KEY="xxx"
export DEV_DB_PASSWORD="xxx"

# 生产环境
export PROD_API_KEY="xxx"
export PROD_DB_PASSWORD="xxx"
```

### 2. CI/CD 环境

1. GitHub Actions
```yaml
# .github/workflows/ci.yml
env:
  GLOBAL_VAR: ${{ secrets.GLOBAL_VAR }}

jobs:
  build:
    env:
      API_KEY: ${{ secrets.API_KEY }}
    steps:
      - uses: actions/checkout@v2
```

2. GitLab CI
```yaml
# .gitlab-ci.yml
variables:
  API_KEY: $CI_API_KEY

job:
  script:
    - echo $API_KEY
  only:
    - main
```

## 清理历史

### 1. 删除敏感数据

1. BFG Repo-Cleaner
```bash
# 下载 BFG
java -jar bfg.jar --delete-files id_rsa

# 清理引用
git reflog expire --expire=now --all
git gc --prune=now --aggressive
```

2. filter-branch
```bash
# 删除文件
git filter-branch --force --index-filter \
  "git rm --cached --ignore-unmatch PATH-TO-FILE" \
  --prune-empty --tag-name-filter cat -- --all

# 强制推送
git push origin --force --all
```

### 2. 历史重写

1. 修改提交
```bash
# 交互式 rebase
git rebase -i HEAD~3

# 修改最后一次提交
git commit --amend
```

2. 压缩历史
```bash
# 创建孤立分支
git checkout --orphan latest_branch

# 添加所有文件
git add -A

# 提交
git commit -m "chore: clean history"
```

## 应急响应

### 1. 泄露处理

1. 立即行动
```bash
# 撤销访问
git remote set-url origin new-url

# 更改凭证
git config --unset credential.helper
```

2. 通知相关方
- 通知安全团队
- 联系服务提供商
- 告知受影响用户
- 记录事件详情

### 2. 预防措施

1. 监控设置
```bash
# 配置 Git 钩子
#!/bin/sh
# .git/hooks/pre-commit
git secrets --pre_commit_hook -- "$@"
```

2. 审计日志
```bash
# 检查提交历史
git log --author="username" --since="1 week ago"

# 查看文件历史
git log --follow -p -- sensitive-file
```

## 最佳实践

### 1. 开发流程

1. 项目设置
```bash
# 初始化项目
git init
git-crypt init

# 配置忽略文件
echo ".env*" >> .gitignore
echo "*.key" >> .gitignore
```

2. 团队协作
```bash
# 共享配置
cp .env.example .env.team

# 文档说明
echo "# Security Guidelines" >> SECURITY.md
```

### 2. 安全检查

1. 定期审计
```bash
# 检查配置
git config --list

# 扫描仓库
git secrets --scan-history
```

2. 更新维护
```bash
# 更新依赖
npm audit fix

# 更新工具
brew upgrade git-crypt
```

## 学习要点
1. 识别敏感数据
2. 实施预防措施
3. 使用加密工具
4. 处理数据泄露

## 小结
正确处理敏感数据是 Git 安全使用中的关键环节。通过本节的学习，你应该能够有效地预防和处理敏感数据问题。

## 练习题
1. 配置 Git 钩子
2. 使用加密工具
3. 清理敏感数据
4. 处理泄露事件
