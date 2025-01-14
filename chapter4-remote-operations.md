# 第四章：远程仓库操作

## 4.1 远程仓库基础

### git remote：管理远程仓库
```bash
# 查看远程仓库
git remote -v

# 添加远程仓库
git remote add <name> <url>

# 删除远程仓库
git remote remove <name>

# 重命名远程仓库
git remote rename <old-name> <new-name>

# 修改远程仓库地址
git remote set-url <name> <new-url>
```

### git fetch：获取远程更新
```bash
# 获取所有远程分支的更新
git fetch --all

# 获取特定远程仓库的更新
git fetch <remote>

# 获取特定分支的更新
git fetch <remote> <branch>

# 清理已删除的远程分支
git fetch --prune
```

### git pull：拉取并合并更新
```bash
# 拉取当前分支的更新
git pull

# 拉取特定远程分支的更新
git pull <remote> <branch>

# 使用rebase方式拉取更新
git pull --rebase

# 指定合并策略
git pull --strategy=recursive -X theirs
```

### git push：推送本地更新
```bash
# 推送当前分支到远程
git push

# 推送到特定远程分支
git push <remote> <branch>

# 强制推送
git push --force

# 推送所有分支
git push --all

# 推送标签
git push --tags
```

## 4.2 协作流程

### Fork & Pull Request 工作流

#### 1. Fork 仓库
1. 在 GitHub/GitLab 上 Fork 目标仓库
2. 克隆 Fork 的仓库到本地
```bash
git clone <your-fork-url>
```

#### 2. 保持与上游同步
```bash
# 添加上游仓库
git remote add upstream <original-repo-url>

# 获取上游更新
git fetch upstream

# 合并上游更新
git merge upstream/main
```

#### 3. 创建功能分支
```bash
# 创建并切换到新分支
git checkout -b feature/new-feature

# 开发新功能并提交
git add .
git commit -m "Add new feature"

# 推送到 Fork 仓库
git push origin feature/new-feature
```

#### 4. 创建 Pull Request
1. 在 GitHub/GitLab 上创建 Pull Request
2. 等待代码审查
3. 根据反馈修改代码
4. 合并 Pull Request

### 处理冲突

#### 1. 在 Pull Request 中解决冲突
```bash
# 更新主分支
git checkout main
git pull upstream main

# 切换回功能分支
git checkout feature/new-feature
git rebase main

# 解决冲突后
git add .
git rebase --continue

# 推送更新
git push --force-with-lease origin feature/new-feature
```

#### 2. 常见冲突解决策略
- 使用 `git mergetool` 可视化解决冲突
- 选择保留某一方的更改
- 手动合并双方更改
- 与团队成员沟通确认最佳方案

### Code Review 最佳实践

#### 1. 提交者注意事项
- 保持提交小而精确
- 提供清晰的提交信息和PR描述
- 自测代码确保质量
- 及时响应审查意见

#### 2. 审查者注意事项
- 关注代码质量和设计
- 提供建设性的反馈
- 验证功能正确性
- 检查是否符合项目规范

## 4.3 高级远程操作

### 子模块管理
```bash
# 添加子模块
git submodule add <repository> <path>

# 初始化子模块
git submodule init

# 更新子模块
git submodule update

# 递归克隆包含子模块的项目
git clone --recursive <repository>
```

### 多远程仓库管理
```bash
# 添加多个远程仓库
git remote add github <github-url>
git remote add gitlab <gitlab-url>

# 推送到多个远程仓库
git push github main
git push gitlab main
```

## 实践练习

### 练习 1：远程仓库基本操作
1. 创建 GitHub 账号并创建新仓库
2. 将本地仓库推送到远程
3. 修改代码并同步到远程
4. 在其他位置克隆仓库

### 练习 2：Fork & Pull Request
1. Fork 一个开源项目
2. 克隆到本地并添加功能
3. 创建 Pull Request
4. 处理代码审查反馈

### 练习 3：冲突处理
1. 模拟团队协作场景
2. 创造并解决合并冲突
3. 使用不同的冲突解决策略

## 注意事项
1. 推送前先拉取最新代码
2. 谨慎使用 force push
3. 保持提交历史清晰
4. 及时同步上游更新
5. 遵循项目的贡献指南
