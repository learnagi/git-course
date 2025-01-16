# 文件操作

Git 的文件操作是日常工作中最常用的功能。本节将详细介绍如何在 Git 中进行文件操作。

## 文件状态

### 文件的四种状态
1. Untracked（未跟踪）
2. Unmodified（未修改）
3. Modified（已修改）
4. Staged（已暂存）

### 查看文件状态
```bash
# 查看仓库状态
git status

# 简短格式显示状态
git status -s

# 查看忽略的文件
git status --ignored
```

## 添加文件

### 基本添加操作

1. 添加单个文件
```bash
git add filename.txt
```

2. 添加多个文件
```bash
git add file1.txt file2.txt file3.txt
```

3. 添加目录
```bash
git add directory/
```

4. 添加所有文件
```bash
# 添加所有文件
git add .

# 添加所有已跟踪的文件
git add -u

# 添加所有文件（包括删除的文件）
git add -A
```

### 交互式添加

```bash
# 交互式添加
git add -i

# 补丁式添加
git add -p
```

## 提交更改

### 基本提交操作

1. 创建提交
```bash
# 基本提交
git commit -m "提交信息"

# 添加并提交
git commit -am "提交信息"

# 修改上一次提交
git commit --amend
```

2. 提交信息规范
```
<type>(<scope>): <subject>

<body>

<footer>
```

类型（type）：
- feat：新功能
- fix：修复
- docs：文档
- style：格式
- refactor：重构
- test：测试
- chore：构建过程或辅助工具的变动

### 查看提交历史

```bash
# 查看完整历史
git log

# 查看简化历史
git log --oneline

# 查看图形化历史
git log --graph

# 查看文件变更统计
git log --stat

# 搜索提交历史
git log --grep="关键词"
```

## 文件比较

### 工作区与暂存区比较

```bash
# 比较所有文件
git diff

# 比较特定文件
git diff filename.txt
```

### 暂存区与最新提交比较

```bash
# 比较所有文件
git diff --cached

# 比较特定文件
git diff --cached filename.txt
```

### 比较两个提交

```bash
# 比较两个提交
git diff commit1 commit2

# 比较分支
git diff branch1 branch2
```

## 移动和删除文件

### 移动文件

```bash
# 移动文件
git mv old_name new_name

# 移动到子目录
git mv file.txt subdirectory/
```

### 删除文件

```bash
# 从 Git 中删除文件
git rm filename.txt

# 从暂存区删除（保留在工作区）
git rm --cached filename.txt

# 强制删除
git rm -f filename.txt
```

## 文件恢复

### 恢复工作区文件

```bash
# 恢复单个文件
git checkout -- filename.txt

# 恢复所有文件
git checkout -- .
```

### 恢复暂存区文件

```bash
# 取消暂存
git reset HEAD filename.txt

# 恢复到特定提交
git checkout commit_hash filename.txt
```

## 高级操作

### 1. 文件重命名检测

```bash
# 开启重命名检测
git config --global diff.renames true

# 查看重命名历史
git log --follow filename
```

### 2. 文件权限管理

```bash
# 保持文件权限
git config core.fileMode true

# 忽略文件权限变化
git config core.fileMode false
```

### 3. 大文件处理

```bash
# 使用 Git LFS
git lfs install
git lfs track "*.psd"
git add .gitattributes
```

## 最佳实践

### 1. 提交规范
- 写清晰的提交信息
- 保持提交粒度适中
- 相关修改放在同一提交中
- 无关修改分开提交

### 2. 文件管理
- 及时添加和提交文件
- 适当使用 .gitignore
- 注意文件权限管理
- 谨慎处理大文件

### 3. 工作流程
- 经常检查文件状态
- 定期提交更改
- 适时使用交互式添加
- 保持工作区整洁

## 学习要点
1. 掌握文件的基本操作
2. 理解文件状态的变化
3. 熟练使用文件比较和恢复
4. 掌握提交规范

## 小结
文件操作是 Git 使用中最基础也是最重要的部分。通过本节的学习，你应该能够熟练地进行文件的添加、提交、比较和恢复等操作。

## 练习题
1. 创建多个文件并通过不同方式添加到暂存区
2. 使用交互式添加处理文件修改
3. 练习不同的文件比较命令
4. 尝试移动和重命名文件，观察 Git 的处理方式
