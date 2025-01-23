---
title: "敏感数据处理"
slug: "sensitive-data"
description: "掌握敏感数据的处理和保护方法"
is_published: true
estimated_minutes: 25
---

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
cat > .gitignore << EOL
# 敏感文件
.env
.env.*
config.json
secrets.yaml

# 密钥文件
*.pem
*.key
*.p12
*.pfx
EOL
```

2. .gitattributes
```bash
# 创建 .gitattributes
cat > .gitattributes << EOL
# 加密敏感文件
secrets.* filter=git-crypt diff=git-crypt
*.key filter=git-crypt diff=git-crypt
EOL
```

### 2. 加密工具

1. git-crypt
```bash
# 初始化 git-crypt
git-crypt init

# 添加用户密钥
git-crypt add-gpg-user USER_ID

# 解锁仓库
git-crypt unlock
```

2. git-secret
```bash
# 初始化 git-secret
git secret init

# 添加用户
git secret tell your@email.com

# 隐藏文件
git secret hide
```

## 补救措施

### 1. 历史清理

1. BFG Repo-Cleaner
```bash
# 删除密码
java -jar bfg.jar --replace-text passwords.txt repo.git

# 删除大文件
java -jar bfg.jar --strip-blobs-bigger-than 100M repo.git
```

2. filter-branch
```bash
# 删除文件
git filter-branch --force --index-filter \
  'git rm --cached --ignore-unmatch config.production.json' \
  --prune-empty --tag-name-filter cat -- --all

# 强制更新
git push origin --force --all
```

### 2. 应急响应

1. 立即行动
```bash
# 吊销凭证
git remote set-url origin https://username:new_token@github.com/username/repo.git

# 更新密钥
ssh-keygen -f ~/.ssh/id_ed25519 -p
```

2. 通知相关方
- 通知安全团队
- 联系平台支持
- 告知受影响用户
- 记录事件过程