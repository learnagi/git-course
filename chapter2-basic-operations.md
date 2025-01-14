# 第二章：Git 基本操作

## 2.1 创建仓库

### git init：初始化仓库
```bash
# 在当前目录初始化仓库
git init

# 在指定目录初始化仓库
git init <directory>
```

初始化后会创建一个 `.git` 目录，它包含了仓库的所有配置和历史记录。

### git clone：克隆远程仓库
```bash
# 基本克隆
git clone <repository-url>

# 克隆到指定目录
git clone <repository-url> <directory>

# 克隆特定分支
git clone -b <branch-name> <repository-url>
```

## 2.2 文件操作

### git add：添加文件到暂存区
```bash
# 添加单个文件
git add <file>

# 添加多个文件
git add <file1> <file2>

# 添加当前目录所有文件
git add .

# 交互式添加
git add -i
```

### git commit：提交更改
```bash
# 基本提交
git commit -m "提交信息"

# 添加并提交
git commit -am "提交信息"

# 修改最后一次提交
git commit --amend
```

提交信息的最佳实践：
- 第一行是简短的摘要（不超过50个字符）
- 空一行
- 详细描述（可选）

### git status：查看仓库状态
```bash
# 完整状态
git status

# 简短状态
git status -s

# 忽略未跟踪的文件
git status -uno
```

状态标记说明：
- `??` - 未跟踪的文件
- `A` - 新添加到暂存区的文件
- `M` - 修改过的文件
- `D` - 删除的文件

### git log：查看提交历史
```bash
# 基本日志
git log

# 单行显示
git log --oneline

# 图形化显示
git log --graph

# 显示变更内容
git log -p

# 显示统计信息
git log --stat
```

常用的日志格式化选项：
```bash
# 自定义格式
git log --pretty=format:"%h - %an, %ar : %s"
```

## 2.3 撤销操作

### git checkout：检出文件或分支
```bash
# 检出文件（撤销工作区修改）
git checkout -- <file>

# 检出分支
git checkout <branch-name>

# 创建并检出新分支
git checkout -b <new-branch>
```

### git reset：重置修改
```bash
# 软重置（保留工作区和暂存区的修改）
git reset --soft HEAD^

# 混合重置（保留工作区的修改）
git reset HEAD^

# 硬重置（丢弃所有修改）
git reset --hard HEAD^
```

重置的三种模式比较：
1. `--soft`：仅移动 HEAD 指针
2. `--mixed`（默认）：移动 HEAD 指针并重置暂存区
3. `--hard`：移动 HEAD 指针并重置暂存区和工作区

### git revert：撤销提交
```bash
# 撤销最近的一次提交
git revert HEAD

# 撤销指定的提交
git revert <commit-hash>

# 撤销多个提交
git revert <commit-hash1> <commit-hash2>
```

`revert` 与 `reset` 的区别：
- `revert` 创建新的提交来撤销修改
- `reset` 直接修改历史记录
- `revert` 适合已推送到远程的提交
- `reset` 适合本地修改

## 实践练习

### 练习 1：基本的文件操作
1. 创建一个新文件并添加一些内容
2. 使用 `git add` 和 `git commit` 提交文件
3. 修改文件并查看状态
4. 再次提交修改

### 练习 2：撤销修改
1. 修改一个文件但不想保存修改
2. 使用 `git checkout` 撤销修改
3. 提交一个修改后使用 `git revert` 撤销
4. 尝试不同的 `git reset` 模式

### 练习 3：查看历史
1. 使用不同的 `git log` 选项查看提交历史
2. 尝试使用 `git log --graph` 查看分支历史
3. 使用自定义格式显示日志

## 注意事项
1. 在使用 `reset --hard` 和 `checkout` 时要特别小心，因为这些操作可能会丢失未提交的修改
2. 养成经常使用 `git status` 的习惯，了解仓库的当前状态
3. 提交信息要清晰明了，便于日后查看和理解
4. 经常性地提交修改，而不是一次提交大量修改
