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

## 凭证存储

### 1. 系统存储

1. macOS Keychain
```bash
# 配置 Keychain
git config --global credential.helper osxkeychain

# 查看配置
git config --global --get credential.helper
```

2. Windows Credential Manager
```bash
# 配置凭证管理器
git config --global credential.helper wincred

# 清除凭证
cmdkey /delete:git:https://github.com
```

### 2. 自定义存储

1. 文件存储
```bash
# 创建凭证文件
touch ~/.git-credentials
chmod 600 ~/.git-credentials

# 配置存储
git config --global credential.helper 'store --file ~/.git-credentials'
```

2. 内存存储
```bash
# 临时存储
git config --global credential.helper cache

# 设置超时时间
git config --global credential.helper 'cache --timeout=3600'
```

## 凭证加密

### 1. GPG 加密

1. 生成密钥
```bash
# 生成 GPG 密钥
gpg --full-generate-key

# 列出密钥
gpg --list-secret-keys --keyid-format LONG
```

2. 配置签名
```bash
# 配置签名密钥
git config --global user.signingkey GPG_KEY_ID

# 启用自动签名
git config --global commit.gpgsign true
```

### 2. 加密工具

1. git-crypt
```bash
# 初始化
git-crypt init

# 添加用户
git-crypt add-gpg-user USER_ID

# 加密文件
echo "pattern filter=git-crypt diff=git-crypt" >> .gitattributes
```

2. git-secret
```bash
# 初始化
git secret init

# 添加用户
git secret tell user@email.com

# 加密文件
git secret add sensitive.file
git secret hide
```

## 安全实践

### 1. 凭证轮换

1. 访问令牌
```bash
# 生成新令牌
# 通过 GitHub/GitLab UI 操作

# 更新远程 URL
git remote set-url origin https://username:new_token@github.com/username/repo.git
```

2. SSH 密钥
```bash
# 备份旧密钥
cp ~/.ssh/id_ed25519 ~/.ssh/id_ed25519.bak

# 生成新密钥
ssh-keygen -t ed25519 -C "your.email@example.com"

# 更新远程服务器
```

### 2. 安全审计

1. 凭证检查
```bash
# 检查配置
git config --list | grep credential

# 查找敏感信息
git grep -l "password"
git grep -l "token"
```

2. 访问日志
```bash
# 查看认证日志
git log --author="username"

# 检查远程操作
git reflog show origin/main
```

## 多账户管理

### 1. SSH 配置

1. 配置文件
```bash
# ~/.ssh/config
Host github-work
    HostName github.com
    User git
    IdentityFile ~/.ssh/id_work
    IdentitiesOnly yes

Host github-personal
    HostName github.com
    User git
    IdentityFile ~/.ssh/id_personal
    IdentitiesOnly yes
```

2. 使用配置
```bash
# 克隆仓库
git clone git@github-work:org/repo.git

# 设置远程
git remote add origin git@github-personal:username/repo.git
```

### 2. 仓库配置

1. 本地配置
```bash
# 设置仓库用户信息
git config user.name "Work Name"
git config user.email "work@example.com"

# 验证配置
git config --local --list
```

2. 远程配置
```bash
# 添加多个远程
git remote add work git@github-work:org/repo.git
git remote add personal git@github-personal:username/repo.git

# 推送到不同远程
git push work main
git push personal main
```

## 故障排除

### 1. 认证问题

1. SSH 问题
```bash
# 测试连接
ssh -vT git@github.com

# 检查权限
ls -l ~/.ssh/
chmod 600 ~/.ssh/id_ed25519
```

2. 凭证问题
```bash
# 清除凭证
git credential reject
protocol=https
host=github.com

# 重置凭证
git config --global --unset credential.helper
```

### 2. 访问控制

1. 权限检查
```bash
# 检查远程访问
git ls-remote origin

# 验证权限
ssh -T git@gitlab.com
```

2. 错误处理
```bash
# 处理认证失败
git config --global credential.helper cache

# 处理权限拒绝
git remote set-url origin git@github.com:username/repo.git
```

## 最佳实践

### 1. 安全建议

1. 凭证保护
- 使用强密码
- 定期轮换凭证
- 加密敏感信息
- 避免共享凭证

2. 访问控制
- 最小权限原则
- 定期审查权限
- 及时撤销访问
- 监控异常活动

### 2. 工作流程

1. 开发流程
```bash
# 克隆仓库
git clone git@github.com:org/repo.git

# 配置本地设置
git config user.name "Your Name"
git config user.email "your.email@example.com"
```

2. 团队协作
```bash
# 配置团队成员
git secret tell team@email.com

# 共享配置
git config --local include.path ../.gitconfig
```

## 学习要点
1. 理解凭证类型
2. 掌握存储方式
3. 实践安全管理
4. 处理认证问题

## 小结
安全的凭证管理是 Git 使用中的重要环节。通过本节的学习，你应该能够安全地管理和使用各种 Git 凭证。

## 练习题
1. 配置多账户管理
2. 实施凭证轮换
3. 处理认证问题
4. 审计凭证使用
