# 常见问题

本节将介绍 Git 使用中的常见问题及其解决方法。

## 提交问题

### 1. 提交错误

1. 修改最后提交
```bash
# 修改提交信息
git commit --amend -m "feat: correct message"

# 添加遗漏文件
git add forgotten-file.txt
git commit --amend --no-edit

# 修改作者信息
git commit --amend --author="Name <email@example.com>"
```

2. 撤销提交
```bash
# 撤销最后一次提交
git reset HEAD~1

# 保留更改
git reset --soft HEAD~1

# 丢弃更改
git reset --hard HEAD~1
```

### 2. 提交丢失

1. 查找提交
```bash
# 查看引用日志
git reflog

# 查找特定提交
git fsck --lost-found

# 恢复提交
git cherry-pick <commit-hash>
```

2. 恢复文件
```bash
# 从最后提交恢复
git checkout HEAD <file>

# 从特定提交恢复
git checkout <commit-hash> <file>

# 从暂存区恢复
git checkout -- <file>
```

## 分支问题

### 1. 分支冲突

1. 合并冲突
```bash
# 查看冲突文件
git status

# 解决冲突
git mergetool

# 完成合并
git add .
git commit -m "merge: resolve conflicts"
```

2. 变基冲突
```bash
# 开始变基
git rebase main

# 解决冲突
git mergetool

# 继续变基
git rebase --continue

# 放弃变基
git rebase --abort
```

### 2. 分支混乱

1. 清理分支
```bash
# 列出已合并分支
git branch --merged

# 删除已合并分支
git branch --merged |
  grep -v "\*" |
  grep -v "main" |
  grep -v "develop" |
  xargs -n 1 git branch -d

# 清理远程分支
git remote prune origin
```

2. 重置分支
```bash
# 重置到远程分支
git fetch origin
git reset --hard origin/main

# 强制推送
git push --force-with-lease

# 重建分支
git checkout --orphan new-main
git add -A
git commit -m "chore: start fresh"
```

## 远程问题

### 1. 推送问题

1. 推送失败
```bash
# 更新本地
git fetch origin
git rebase origin/main

# 强制推送
git push --force-with-lease

# 设置上游分支
git push -u origin feature/branch
```

2. 认证问题
```bash
# 检查远程 URL
git remote -v

# 更新认证
git remote set-url origin https://username@github.com/repo.git

# 存储凭证
git config --global credential.helper store
```

### 2. 同步问题

1. 分支不同步
```bash
# 检查远程分支
git remote show origin

# 同步分支
git fetch --prune
git remote update origin --prune

# 重置分支
git reset --hard origin/main
```

2. 标签同步
```bash
# 获取所有标签
git fetch --tags

# 推送标签
git push --tags

# 删除远程标签
git push --delete origin tagname
```

## 配置问题

### 1. 用户配置

1. 身份配置
```bash
# 检查配置
git config --list

# 设置用户信息
git config --global user.name "Your Name"
git config --global user.email "email@example.com"

# 项目特定配置
git config user.name "Project Name"
git config user.email "project@example.com"
```

2. 配置文件
```bash
# 编辑全局配置
git config --global --edit

# 编辑项目配置
git config --local --edit

# 删除配置
git config --unset user.name
```

### 2. 工具配置

1. 编辑器配置
```bash
# 设置编辑器
git config --global core.editor "code --wait"

# 设置差异工具
git config --global diff.tool vscode
git config --global difftool.vscode.cmd 'code --wait --diff $LOCAL $REMOTE'

# 设置合并工具
git config --global merge.tool vscode
git config --global mergetool.vscode.cmd 'code --wait $MERGED'
```

2. 别名配置
```bash
# 设置别名
git config --global alias.co checkout
git config --global alias.br branch
git config --global alias.ci commit
git config --global alias.st status

# 删除别名
git config --global --unset alias.co
```

## 性能问题

### 1. 仓库性能

1. 仓库优化
```bash
# 垃圾回收
git gc --aggressive

# 重新打包
git repack -ad

# 清理松散对象
git prune
```

2. 大文件处理
```bash
# 查找大文件
git rev-list --objects --all |
  git cat-file --batch-check='%(objecttype) %(objectname) %(objectsize) %(rest)' |
  sort -k3nr |
  head -10

# 清理历史
git filter-branch --tree-filter 'rm -f path/to/large/file' HEAD
```

### 2. 网络性能

1. 克隆优化
```bash
# 浅克隆
git clone --depth 1 <repository>

# 单分支克隆
git clone --single-branch --branch main <repository>

# 稀疏检出
git clone --filter=blob:none <repository>
```

2. 代理设置
```bash
# HTTP 代理
git config --global http.proxy http://proxy.example.com:8080

# SOCKS 代理
git config --global http.proxy socks5://proxy.example.com:1080

# 取消代理
git config --global --unset http.proxy
```

## 工具问题

### 1. IDE 集成

1. VS Code 问题
```json
{
  "git.enabled": true,
  "git.autofetch": true,
  "git.confirmSync": false,
  "git.enableSmartCommit": true,
  "git.ignoreLegacyWarning": true
}
```

2. 插件问题
```bash
# 重置插件
code --disable-extensions
code --list-extensions

# 重新安装插件
code --install-extension eamodio.gitlens
```

### 2. 命令行工具

1. 工具安装
```bash
# macOS
brew install git
brew install git-lfs
brew install git-flow

# Linux
sudo apt-get update
sudo apt-get install git git-lfs git-flow
```

2. 工具更新
```bash
# 更新 Git
git --version
brew upgrade git

# 更新工具
brew upgrade git-lfs
brew upgrade git-flow
```

## 常见错误

### 1. 错误信息

1. 常见错误
```bash
# 文件未找到
git add missing-file.txt
> fatal: pathspec 'missing-file.txt' did not match any files

# 分支不存在
git checkout non-existent-branch
> error: pathspec 'non-existent-branch' did not match any file(s) known to git

# 合并冲突
git merge feature-branch
> CONFLICT (content): Merge conflict in file.txt
```

2. 解决方法
```bash
# 检查文件状态
git status

# 检查日志
git log --oneline

# 检查配置
git config --list
```

### 2. 错误处理

1. 基本处理
```bash
# 取消操作
git merge --abort
git rebase --abort
git cherry-pick --abort

# 重置状态
git reset --hard HEAD
git clean -fd
```

2. 高级处理
```bash
# 备份当前状态
git stash

# 检查问题
git fsck

# 修复问题
git gc --auto
git prune
```

## 最佳实践

### 1. 预防措施

1. 日常检查
```bash
# 检查状态
git status

# 检查日志
git log --oneline

# 检查远程
git remote -v
```

2. 定期维护
```bash
# 更新远程
git fetch --all --prune

# 清理本地
git gc
git prune

# 验证完整性
git fsck
```

### 2. 应急预案

1. 数据备份
```bash
# 创建备份
git bundle create repo.bundle --all

# 克隆备份
git clone repo.bundle backup-repo

# 验证备份
cd backup-repo
git log --oneline
```

2. 恢复计划
```bash
# 创建恢复点
git tag recovery-point

# 推送备份
git push --tags

# 恢复操作
git reset --hard recovery-point
```

## 学习要点
1. 理解常见问题
2. 掌握解决方法
3. 学会预防措施
4. 准备应急预案

## 小结
通过本节的学习，你应该能够处理 Git 使用中的常见问题，并采取适当的预防措施。

## 练习题
1. 解决提交问题
2. 处理分支冲突
3. 配置开发环境
4. 优化仓库性能
