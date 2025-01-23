---
title: "安全基础"
slug: "security-basics"
description: "了解 Git 安全的基本概念和原则"
is_published: true
estimated_minutes: 20
---

# 安全基础

本节将介绍 Git 安全的基本概念和原则，帮助你建立安全意识并采取适当的防护措施。

## 安全威胁

### 1. 常见威胁

1. 代码泄露
- 敏感信息提交
- 权限配置错误
- 仓库可见性问题

2. 身份冒用
- 凭证泄露
- SSH 密钥被盗
- 未验证的提交

3. 恶意代码
- 依赖注入
- 脚本注入
- 钓鱼攻击

### 2. 攻击方式

1. 仓库入侵
```bash
# 未授权访问
git clone https://private-repo-url

# 强制推送
git push -f origin main
```

2. 历史操作
```bash
# 查看所有提交
git log --all

# 恢复删除的提交
git reflog
git reset --hard HEAD@{1}
```

## 基本防护

### 1. 访问控制

1. 仓库权限
```bash
# 设置仓库权限
git config --local core.sharedRepository group

# 修改文件权限
chmod 640 .git/config
```

2. 分支保护
```bash
# 禁止强制推送
git config --local receive.denyNonFastForwards true

# 禁止删除分支
git config --local receive.denyDeletes true
```

### 2. 提交验证

1. GPG 签名
```bash
# 生成 GPG 密钥
gpg --gen-key

# 配置 Git 使用 GPG
git config --global user.signingkey <key-id>
git config --global commit.gpgsign true
```

2. 提交检查
```bash
# 验证提交签名
git verify-commit <commit-hash>

# 查看提交历史
git log --show-signature
```