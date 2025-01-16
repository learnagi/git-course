# 高级问题

本节将介绍 Git 使用中的高级问题及其解决方法。

## 历史问题

### 1. 历史修改

1. 修改历史
```bash
# 交互式变基
git rebase -i HEAD~5

# 修改提交
git commit --amend
git rebase --continue

# 压缩提交
git reset --soft HEAD~3
git commit -m "feat: combine three commits"
```

2. 历史清理
```bash
# 删除文件历史
git filter-branch --force --index-filter \
  'git rm --cached --ignore-unmatch path/to/file' \
  --prune-empty --tag-name-filter cat -- --all

# 清理大文件
git filter-branch --tree-filter 'rm -f path/to/large/file' HEAD

# 重写作者信息
git filter-branch --env-filter '
if [ "$GIT_AUTHOR_EMAIL" = "old@example.com" ]; then
    GIT_AUTHOR_EMAIL="new@example.com"
    GIT_AUTHOR_NAME="New Name"
fi
' HEAD
```

### 2. 历史分析

1. 日志分析
```bash
# 查看提交统计
git shortlog -sn

# 分析文件历史
git log --follow -p -- path/to/file

# 查找引入问题的提交
git bisect start
git bisect bad HEAD
git bisect good v1.0
```

2. 责任追踪
```bash
# 查看文件责任
git blame path/to/file

# 查看行历史
git log -L 1,10:path/to/file

# 查看提交范围
git log --since="1 month ago" --author="username"
```

## 存储问题

### 1. 大文件处理

1. Git LFS
```bash
# 安装 Git LFS
git lfs install

# 跟踪大文件
git lfs track "*.psd"
git lfs track "*.zip"

# 迁移现有文件
git lfs migrate import --include="*.psd"
```

2. 存储优化
```bash
# 检查存储
git count-objects -vH

# 压缩存储
git gc --aggressive
git repack -ad
git prune

# 清理大文件
git rev-list --objects --all |
  git cat-file --batch-check='%(objecttype) %(objectname) %(objectsize) %(rest)' |
  sort -k3nr |
  head -10
```

### 2. 子模块问题

1. 子模块管理
```bash
# 添加子模块
git submodule add <repository> path/to/submodule

# 更新子模块
git submodule update --init --recursive

# 删除子模块
git submodule deinit path/to/submodule
git rm path/to/submodule
```

2. 子模块同步
```bash
# 检查状态
git submodule status

# 同步更改
git submodule sync
git submodule update --remote

# 批量操作
git submodule foreach 'git checkout main'
```

## 分支策略

### 1. 分支重组

1. 分支重构
```bash
# 创建新主分支
git checkout --orphan new-main

# 重建提交
git add -A
git commit -m "chore: rebuild main branch"

# 替换主分支
git branch -D main
git branch -m main
```

2. 分支合并
```bash
# 压缩合并
git merge --squash feature-branch

# 选择性合并
git cherry-pick <commit-hash>

# 变基合并
git rebase -i main
```

### 2. 分支管理

1. 分支策略
```bash
# 保护分支
git branch -M main
git push -u origin main

# 锁定分支
git branch --edit-description main "Protected branch"

# 分支权限
git config branch.main.mergeoptions "--no-ff"
```

2. 分支清理
```bash
# 清理远程分支
git remote prune origin

# 清理本地分支
git branch --merged |
  grep -v "\*" |
  xargs -n 1 git branch -d

# 清理标签
git tag -l | xargs git tag -d
git fetch --tags
```

## 工作流问题

### 1. 工作流冲突

1. 流程冲突
```bash
# 检查工作流
git flow init

# 解决冲突
git flow feature finish feature-name
git flow hotfix finish hotfix-name

# 重置工作流
git flow reset
```

2. 团队冲突
```bash
# 创建功能分支
git flow feature start feature-name

# 发布版本
git flow release start 1.0.0
git flow release finish 1.0.0

# 修复问题
git flow hotfix start hotfix-name
```

### 2. 工作流优化

1. 流程优化
```bash
# 配置工作流
git config --global flow.prefix "feature/"
git config --global flow.release.finish.notag true

# 自动化流程
git config --global alias.feature 'flow feature'
git config --global alias.release 'flow release'
```

2. 团队协作
```bash
# 团队同步
git fetch --all
git rebase origin/main

# 代码评审
git push -u origin feature/branch
gh pr create

# 合并更改
gh pr merge
```

## 安全问题

### 1. 凭证问题

1. 凭证管理
```bash
# 检查凭证
git config --global credential.helper

# 存储凭证
git config --global credential.helper store

# 缓存凭证
git config --global credential.helper 'cache --timeout=3600'
```

2. 密钥管理
```bash
# 生成密钥
ssh-keygen -t ed25519 -C "email@example.com"

# 添加密钥
ssh-add ~/.ssh/id_ed25519

# 测试连接
ssh -T git@github.com
```

### 2. 安全漏洞

1. 漏洞扫描
```bash
# 安装工具
npm install -g git-secrets

# 配置规则
git secrets --install
git secrets --register-aws

# 扫描仓库
git secrets --scan
```

2. 漏洞修复
```bash
# 删除敏感信息
git filter-branch --force --index-filter \
  'git rm --cached --ignore-unmatch config.ini' \
  --prune-empty --tag-name-filter cat -- --all

# 强制推送
git push --force --all

# 更新 .gitignore
echo "config.ini" >> .gitignore
```

## 性能优化

### 1. 仓库优化

1. 存储优化
```bash
# 检查大小
du -sh .git

# 压缩存储
git gc --aggressive --prune=now

# 重新打包
git repack -ad
```

2. 索引优化
```bash
# 更新索引
git update-index --refresh

# 验证索引
git fsck

# 重建索引
git reset --hard HEAD
```

### 2. 网络优化

1. 克隆优化
```bash
# 浅克隆
git clone --depth 1 <repository>

# 单分支克隆
git clone --single-branch --branch main <repository>

# 稀疏检出
git clone --filter=blob:none <repository>
```

2. 传输优化
```bash
# 压缩传输
git config --global core.compression 9

# 批量传输
git config --global transfer.fsckObjects true

# 并行传输
git config --global submodule.fetchJobs 4
```

## 工具集成

### 1. CI/CD 问题

1. 集成配置
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
      - name: Build
        run: |
          npm ci
          npm run build
```

2. 部署问题
```yaml
# .github/workflows/deploy.yml
name: Deploy

on:
  push:
    tags:
      - 'v*'

jobs:
  deploy:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v2
      - name: Deploy
        run: |
          npm ci
          npm run deploy
```

### 2. 工具问题

1. IDE 集成
```json
{
  "git.enableSmartCommit": true,
  "git.confirmSync": false,
  "git.autofetch": true,
  "git.pruneOnFetch": true
}
```

2. 命令行工具
```bash
# 安装工具
brew install git-flow
brew install git-lfs
brew install gh

# 配置工具
git flow init
git lfs install
gh auth login
```

## 故障恢复

### 1. 数据恢复

1. 提交恢复
```bash
# 查找丢失提交
git reflog

# 恢复提交
git cherry-pick <commit-hash>

# 恢复分支
git branch recover-branch <commit-hash>
```

2. 文件恢复
```bash
# 从暂存区恢复
git checkout -- path/to/file

# 从提交恢复
git checkout <commit-hash> path/to/file

# 从远程恢复
git fetch origin
git checkout origin/main path/to/file
```

### 2. 系统恢复

1. 配置恢复
```bash
# 备份配置
git config --list > git-config-backup.txt

# 重置配置
git config --global --unset-all

# 恢复配置
while read line; do
  git config --global "${line%=*}" "${line#*=}"
done < git-config-backup.txt
```

2. 仓库恢复
```bash
# 创建备份
git bundle create repo.bundle --all

# 验证备份
git bundle verify repo.bundle

# 恢复仓库
git clone repo.bundle recovered-repo
```

## 最佳实践

### 1. 问题预防

1. 定期检查
```bash
# 检查状态
git status
git remote -v
git submodule status

# 更新远程
git fetch --all --prune
git remote update origin --prune

# 维护仓库
git gc
git prune
```

2. 自动化检查
```yaml
# .github/workflows/check.yml
name: Check

on:
  schedule:
    - cron: '0 0 * * *'

jobs:
  check:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v2
      - name: Run checks
        run: |
          git fsck
          git gc
```

### 2. 应急处理

1. 应急预案
```bash
# 创建恢复点
git tag recovery-point

# 备份数据
git bundle create repo.bundle --all

# 记录状态
git status > status.txt
git config --list > config.txt
```

2. 快速恢复
```bash
# 重置状态
git reset --hard HEAD
git clean -fd

# 更新远程
git fetch origin
git reset --hard origin/main

# 恢复配置
git config --local include.path ../.gitconfig
```

## 学习要点
1. 掌握高级问题
2. 学会优化性能
3. 加强安全防护
4. 准备应急预案

## 小结
通过本节的学习，你应该能够处理 Git 使用中的高级问题，并采取适当的优化措施。

## 练习题
1. 处理历史问题
2. 优化存储性能
3. 加强安全防护
4. 制定应急预案
