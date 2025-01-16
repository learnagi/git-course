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
# 查看仓库权限
git ls-remote --get-url

# 设置仓库可见性
# GitHub/GitLab UI 操作
```

2. 分支保护
```bash
# 保护主分支
git config branch.main.protect true

# 设置推送限制
git config receive.denyNonFastForwards true
```

### 2. 身份验证

1. 用户配置
```bash
# 设置用户信息
git config --global user.name "Your Name"
git config --global user.email "your.email@example.com"

# 验证配置
git config --list
```

2. SSH 配置
```bash
# 生成 SSH 密钥
ssh-keygen -t ed25519 -C "your.email@example.com"

# 添加到 SSH 代理
eval "$(ssh-agent -s)"
ssh-add ~/.ssh/id_ed25519
```

## 安全配置

### 1. 基本设置

1. 全局配置
```bash
# 启用安全功能
git config --global core.fsmonitor true
git config --global core.untrackedCache true

# 设置安全提交
git config --global commit.gpgsign true
```

2. 仓库配置
```bash
# 设置忽略文件
echo ".env*" >> .gitignore
echo "*.key" >> .gitignore

# 设置属性
echo "*.sh text eol=lf" >> .gitattributes
```

### 2. 高级设置

1. 钩子配置
```bash
# pre-commit 钩子
#!/bin/sh
# .git/hooks/pre-commit
if git diff --cached | grep -i "password"
then
    echo "Potential password in commit"
    exit 1
fi
```

2. 安全策略
```yaml
# .github/security.yml
security:
  alerts:
    enabled: true
  dependabot:
    enabled: true
    schedule: weekly
```

## 最佳实践

### 1. 代码管理

1. 提交规范
```bash
# 签名提交
git commit -S -m "feat: add secure feature"

# 验证提交
git verify-commit HEAD
```

2. 分支策略
```bash
# 创建保护分支
git branch --set-upstream-to=origin/main main

# 合并策略
git merge --no-ff feature-branch
```

### 2. 环境管理

1. 环境变量
```bash
# 使用环境文件
cp .env.example .env
echo ".env" >> .gitignore

# 加密敏感数据
git-crypt init
git-crypt add-gpg-user USER_ID
```

2. 密钥管理
```bash
# 使用密钥管理工具
# 示例：使用 git-secret
git secret init
git secret tell your@email.com
git secret add sensitive.file
```

## 安全审计

### 1. 代码审查

1. 提交历史
```bash
# 查看提交历史
git log --pretty=full

# 查找敏感信息
git log -p | grep -i "password"
```

2. 变更检查
```bash
# 查看变更
git diff HEAD^

# 检查特定文件
git blame sensitive-file.txt
```

### 2. 安全扫描

1. 依赖检查
```bash
# 使用依赖扫描工具
npm audit
yarn audit

# 更新依赖
npm update
```

2. 代码扫描
```bash
# 使用代码扫描工具
# 示例：使用 GitGuardian
gg scan
```

## 事件响应

### 1. 安全事件

1. 检测泄露
```bash
# 查找敏感信息
git grep -l "password"

# 检查日志
git log --grep="password"
```

2. 应对措施
```bash
# 撤销提交
git revert HEAD

# 清理历史
git filter-branch --force --index-filter \
  "git rm --cached --ignore-unmatch PATH-TO-FILE" \
  --prune-empty --tag-name-filter cat -- --all
```

### 2. 恢复策略

1. 备份恢复
```bash
# 创建备份
git bundle create repo.bundle --all

# 恢复备份
git clone repo.bundle restored-repo
```

2. 版本回滚
```bash
# 回滚到安全版本
git reset --hard commit-hash

# 强制推送
git push --force-with-lease origin main
```

## 学习要点
1. 理解安全威胁
2. 掌握基本防护
3. 实施安全配置
4. 应对安全事件

## 小结
Git 安全是一个持续的过程，需要在日常使用中保持警惕并遵循最佳实践。通过本节的学习，你应该能够理解基本的安全概念并采取适当的防护措施。

## 练习题
1. 配置基本安全设置
2. 实施分支保护
3. 处理敏感信息
4. 进行安全审计
