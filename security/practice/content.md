# 实践练习

本节提供一系列实践练习，帮助你巩固 Git 安全知识。

## 基础安全练习

### 练习 1：安全配置

1. 任务描述
- 配置基本安全设置
- 设置 Git 钩子
- 配置忽略文件
- 测试配置效果

2. 步骤指导
```bash
# 配置用户信息
git config --global user.name "Your Name"
git config --global user.email "your.email@example.com"

# 创建钩子
cat > .git/hooks/pre-commit << 'EOF'
#!/bin/sh
if git diff --cached | grep -i "password="
then
    echo "Error: Potential password in commit"
    exit 1
fi
EOF
chmod +x .git/hooks/pre-commit

# 配置忽略文件
echo ".env*" >> .gitignore
echo "*.key" >> .gitignore
```

### 练习 2：凭证管理

1. 场景设置
- 生成 SSH 密钥
- 配置多个账户
- 测试连接
- 验证配置

2. 解决步骤
```bash
# 生成密钥
ssh-keygen -t ed25519 -C "work@example.com"
ssh-keygen -t ed25519 -C "personal@example.com"

# 配置 SSH
cat > ~/.ssh/config << 'EOF'
Host github-work
    HostName github.com
    User git
    IdentityFile ~/.ssh/id_ed25519_work
    IdentitiesOnly yes

Host github-personal
    HostName github.com
    User git
    IdentityFile ~/.ssh/id_ed25519_personal
    IdentitiesOnly yes
EOF

# 测试连接
ssh -T git@github-work
ssh -T git@github-personal
```

## 加密实践

### 练习 1：git-crypt

1. 基本配置
```bash
# 安装 git-crypt
brew install git-crypt

# 初始化项目
git init
git-crypt init

# 配置文件
echo "sensitive.txt filter=git-crypt diff=git-crypt" >> .gitattributes
echo "secret data" > sensitive.txt

# 提交文件
git add .
git commit -m "feat: add encrypted file"
```

2. 团队协作
```bash
# 导出密钥
git-crypt export-key ~/git-crypt-key

# 在新机器上
git clone repo-url
git-crypt unlock ~/git-crypt-key
```

### 练习 2：git-secret

1. 项目设置
```bash
# 安装 git-secret
brew install git-secret

# 初始化
git secret init
git secret tell your@email.com

# 添加文件
echo "API_KEY=secret" > api-key.txt
git secret add api-key.txt
git secret hide
```

2. 文件管理
```bash
# 更新文件
git secret reveal
echo "NEW_API_KEY=updated" > api-key.txt
git secret hide

# 删除文件
git secret remove api-key.txt
git secret hide -d
```

## 敏感数据处理

### 练习 1：数据清理

1. 任务目标
- 识别敏感数据
- 清理提交历史
- 更新远程仓库
- 验证清理效果

2. 实现步骤
```bash
# 扫描仓库
git grep -l "password"

# 使用 BFG
java -jar bfg.jar --replace-text passwords.txt

# 清理历史
git reflog expire --expire=now --all
git gc --prune=now --aggressive

# 强制推送
git push origin --force --all
```

### 练习 2：预防措施

1. 配置钩子
```bash
# pre-commit 钩子
cat > .git/hooks/pre-commit << 'EOF'
#!/bin/sh

# 检查敏感信息
patterns=("password=" "api_key=" "secret=")
for pattern in "${patterns[@]}"; do
    if git diff --cached | grep -i "$pattern"; then
        echo "Error: Found potential sensitive data: $pattern"
        exit 1
    fi
done
EOF
chmod +x .git/hooks/pre-commit
```

2. 自动化检查
```bash
# 安装 git-secrets
brew install git-secrets

# 配置规则
git secrets --register-aws
git secrets --add 'password\s*=\s*.+'
git secrets --add 'api[_-]key\s*=\s*.+'

# 添加钩子
git secrets --install
```

## 安全审计

### 练习 1：代码审查

1. 审计任务
```bash
# 检查提交历史
git log --pretty=full

# 查找敏感信息
git log -p | grep -i "password"

# 检查特定文件
git blame config.js
```

2. 问题修复
```bash
# 修改最近提交
git commit --amend

# 重写历史
git rebase -i HEAD~3

# 删除敏感文件
git filter-branch --force --index-filter \
  "git rm --cached --ignore-unmatch config.js" \
  --prune-empty --tag-name-filter cat -- --all
```

### 练习 2：安全扫描

1. 依赖检查
```bash
# NPM 项目
npm audit
npm audit fix

# Python 项目
pip list --outdated
pip install --upgrade package-name
```

2. 代码扫描
```bash
# 使用 GitGuardian
gg scan

# 使用 git-secrets
git secrets --scan-history
```

## 应急响应

### 场景 1：凭证泄露

1. 问题处理
```bash
# 撤销访问
git remote set-url origin new-url

# 更改凭证
git config --unset credential.helper

# 重置令牌
# 通过 GitHub/GitLab UI 操作
```

2. 预防措施
```bash
# 配置 credential helper
git config --global credential.helper osxkeychain

# 使用环境变量
echo "export API_KEY='xxx'" >> ~/.bashrc
```

### 场景 2：数据泄露

1. 应急步骤
```bash
# 临时删除访问
git remote remove origin

# 创建新分支
git checkout -b cleanup

# 清理数据
git filter-branch --force --index-filter \
  "git rm --cached --ignore-unmatch sensitive-file" \
  --prune-empty --tag-name-filter cat -- --all
```

2. 恢复措施
```bash
# 备份数据
git bundle create repo.bundle --all

# 重置仓库
git checkout --orphan latest_branch
git add -A
git commit -m "chore: clean start"
```

## 最佳实践总结

### 1. 日常工作

1. 提交检查
```bash
# 检查变更
git diff --cached

# 验证提交
git verify-commit HEAD

# 查看日志
git log --show-signature
```

2. 安全维护
```bash
# 更新依赖
npm update
npm audit fix

# 清理历史
git gc
git prune
```

### 2. 团队协作

1. 工作流程
```bash
# 分支保护
git config branch.main.protect true

# 代码评审
git request-pull v1.0 origin main
```

2. 安全规范
```bash
# 文档编写
echo "# Security Policy" >> SECURITY.md

# 配置共享
cp .env.example .env.team
```

## 学习要点
1. 实践基础安全
2. 掌握加密工具
3. 处理敏感数据
4. 应对安全事件

## 小结
通过这些练习，你应该能够熟练运用 Git 安全知识，并在实际工作中有效地预防和处理各种安全问题。

## 下一步
1. 深入学习工具
2. 改进工作流程
3. 参与安全评审
4. 分享实践经验
