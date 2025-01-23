---
title: "安全管理"
slug: "security"
description: "掌握 Git 安全管理的基本概念和实践"
is_published: true
estimated_minutes: 30
---

# 安全管理

本节将介绍 Git 安全管理的基本概念和实践方法。

## 安全基础

### 安全威胁

1. 常见威胁
- 代码泄露：敏感信息提交、权限配置错误、仓库可见性问题
- 身份冒用：凭证泄露、SSH 密钥被盗、未验证的提交
- 恶意代码：依赖注入、脚本注入、钓鱼攻击

2. 基本防护
```bash
# 设置仓库权限
git config --local core.sharedRepository group

# 禁止强制推送
git config --local receive.denyNonFastForwards true

# 禁止删除分支
git config --local receive.denyDeletes true
```

## 凭证管理

### 凭证类型

1. 基本凭证
```bash
# 配置用户信息
git config --global user.name "Your Name"
git config --global user.email "your.email@example.com"

# 存储凭证
git config --global credential.helper store
```

2. SSH 密钥
```bash
# 生成 ED25519 密钥（推荐）
ssh-keygen -t ed25519 -C "your.email@example.com"

# 添加私钥
eval "$(ssh-agent -s)"
ssh-add ~/.ssh/id_ed25519

# 测试连接
ssh -T git@github.com
```

### 凭证安全

1. 系统凭证管理器
```bash
# Windows
git config --global credential.helper wincred

# macOS
git config --global credential.helper osxkeychain

# Linux
git config --global credential.helper libsecret
```

2. GPG 签名
```bash
# 生成 GPG 密钥
gpg --gen-key

# 配置 Git 使用 GPG
git config --global user.signingkey <key-id>
git config --global commit.gpgsign true

# 验证提交签名
git verify-commit <commit-hash>
```

## 敏感数据处理

### 预防措施

1. 配置文件
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

2. 检测方法
```bash
# 搜索敏感词
git grep -i "password"
git grep -i "api[_-]key"
git grep -i "secret"

# 使用 git-secrets
git secrets --register-aws
git secrets --scan
```

### 加密工具

1. git-crypt
```bash
# 初始化 git-crypt
git-crypt init

# 添加用户密钥
git-crypt add-gpg-user USER_ID

# 解锁仓库
git-crypt unlock
```

2. 文件权限
```bash
# 设置密钥权限
chmod 600 ~/.ssh/id_ed25519
chmod 600 ~/.ssh/id_ed25519.pub

# 设置配置文件权限
chmod 640 .git/config
```