# 第三章：分支管理

## 3.1 分支基础

### 什么是分支？
分支是Git中最强大的功能之一，它允许我们从主开发线上分离出来，在不影响主线的情况下进行开发。分支本质上是指向提交对象的可变指针。

### 分支的基本操作

#### 创建分支
```bash
# 创建分支
git branch <branch-name>

# 创建并切换到新分支
git checkout -b <branch-name>

# 基于特定提交创建分支
git branch <branch-name> <commit-hash>
```

#### 查看分支
```bash
# 列出本地分支
git branch

# 列出远程分支
git branch -r

# 列出所有分支
git branch -a

# 查看分支详细信息
git branch -v
```

#### 切换分支
```bash
# 切换到指定分支
git checkout <branch-name>

# 切换到上一个分支
git checkout -
```

#### 删除分支
```bash
# 删除已合并的分支
git branch -d <branch-name>

# 强制删除分支
git branch -D <branch-name>
```

### 合并分支

#### git merge：合并分支
```bash
# 合并指定分支到当前分支
git merge <branch-name>

# 使用--no-ff参数保留分支信息
git merge --no-ff <branch-name>
```

#### 解决合并冲突
当两个分支修改了同一个文件的同一部分时，会产生冲突：
1. Git会在文件中标记冲突区域
2. 手动编辑解决冲突
3. 使用 `git add` 标记冲突已解决
4. 执行 `git commit` 完成合并

## 3.2 分支策略

### 功能分支（Feature Branch）
- 用途：开发新功能
- 命名规范：feature/功能名称
- 基于：develop 分支
- 合并到：develop 分支
```bash
# 创建功能分支
git checkout -b feature/new-feature develop

# 完成功能开发后合并回develop
git checkout develop
git merge --no-ff feature/new-feature
```

### 发布分支（Release Branch）
- 用途：准备发布新版本
- 命名规范：release/版本号
- 基于：develop 分支
- 合并到：master 和 develop
```bash
# 创建发布分支
git checkout -b release/1.0.0 develop

# 完成发布准备后
git checkout master
git merge --no-ff release/1.0.0
git tag -a v1.0.0
```

### 热修复分支（Hotfix Branch）
- 用途：修复生产环境的紧急问题
- 命名规范：hotfix/问题描述
- 基于：master 分支
- 合并到：master 和 develop
```bash
# 创建热修复分支
git checkout -b hotfix/bug-fix master

# 完成修复后
git checkout master
git merge --no-ff hotfix/bug-fix
git tag -a v1.0.1
```

## 3.3 GitFlow 工作流

GitFlow 是一个基于分支的严格开发模型，定义了一套完整的分支管理流程。

### 主要分支
- `master`：存储正式发布的版本
- `develop`：日常开发分支

### 辅助分支
- `feature/*`：新功能开发
- `release/*`：版本发布准备
- `hotfix/*`：生产环境紧急修复

### GitFlow 工作流程
1. 从 `develop` 创建 `feature` 分支进行功能开发
2. 功能完成后合并回 `develop`
3. 从 `develop` 创建 `release` 分支准备发布
4. 发布完成后同时合并到 `master` 和 `develop`
5. 如果生产环境出现问题，从 `master` 创建 `hotfix` 分支
6. 修复完成后同时合并到 `master` 和 `develop`

## 实践练习

### 练习 1：基本分支操作
1. 创建一个新分支并切换到该分支
2. 在分支上做一些修改并提交
3. 切换回主分支，然后合并刚才的分支
4. 删除已合并的分支

### 练习 2：解决冲突
1. 在两个不同的分支修改同一个文件的同一部分
2. 尝试合并这两个分支
3. 解决产生的冲突
4. 完成合并

### 练习 3：GitFlow 实践
1. 使用 GitFlow 模型创建一个新功能分支
2. 在功能分支上开发并提交
3. 创建发布分支并进行发布准备
4. 完成发布并合并到主分支

## 注意事项
1. 分支名称要有意义，遵循团队的命名规范
2. 定期清理已合并的分支，保持仓库整洁
3. 合并分支时注意检查代码，确保没有遗漏的冲突
4. 重要的合并操作建议使用 `--no-ff` 参数，保留分支信息
5. 在团队中统一使用相同的分支管理策略
