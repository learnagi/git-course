---
title: "凭证管理"
slug: "credentials"
description: "学习如何安全地管理 Git 凭证"
is_published: true
estimated_minutes: 25
---

# 凭证管理

本节将介绍如何安全地管理 Git 凭证，包括密码、令牌和密钥等。

## 凭证类型

### 1. 基本凭证

1. 用户名密码
```bash
# 配置用户信息
git config --global user.name "Your Name"
git config --global user.email "your.email@example.com"

# 存储凭证
git config --global credential.helper store
```

2. 访问令牌
```bash
# GitHub 个人访问令牌
git clone https://username:token@github.com/username/repo.git

# GitLab 访问令牌
git remote add origin https://oauth2:token@gitlab.com/username/repo.git
```

### 2. SSH 密钥

1. 生成密钥
```bash
# 生成 ED25519 密钥（推荐）
ssh-keygen -t ed25519 -C "your.email@example.com"

# 生成 RSA 密钥（兼容性更好）
ssh-keygen -t rsa -b 4096 -C "your.email@example.com"
```

2. 配置密钥
```bash
# 启动 SSH 代理
eval "$(ssh-agent -s)"

# 添加私钥
ssh-add ~/.ssh/id_ed25519

# 测试连接
ssh -T git@github.com
```

## 凭证管理

### 1. 凭证存储

1. 系统凭证管理器
```bash
# Windows
git config --global credential.helper wincred

# macOS
git config --global credential.helper osxkeychain

# Linux
git config --global credential.helper libsecret
```

2. 自定义存储
```bash
# 临时存储（15分钟）
git config --global credential.helper 'cache --timeout=900'

# 文件存储
git config --global credential.helper 'store --file ~/.git-credentials'
```

### 2. 凭证安全

1. 密钥保护
```bash
# 设置密钥权限
chmod 600 ~/.ssh/id_ed25519
chmod 600 ~/.ssh/id_ed25519.pub

# 使用密钥密码
ssh-keygen -p -f ~/.ssh/id_ed25519
```

2. 凭证轮换
```bash
# 更新访问令牌
git remote set-url origin https://username:new_token@github.com/username/repo.git

# 更新 SSH 密钥
ssh-keygen -f ~/.ssh/id_ed25519 -p
```