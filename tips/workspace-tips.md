---
title: "Git 工作区管理技巧"
slug: "workspace-tips"
sequence: 3
description: "Git 工作区和暂存区的常用操作技巧和命令"
status: "published"
---

# 工作区管理技巧

## 文件变更查看

### 查看未暂存的变更
```bash
git diff
```

### 查看已暂存的变更
```bash
git diff --cached
# 或者
git diff --staged
```

### 查看所有变更（已暂存和未暂存）
```bash
git diff HEAD
```

## 文件状态管理

### 查看特定文件的变更历史
```bash
git log -p <file_name>
```

### 恢复已删除的文件
```bash
git checkout <deleting_commit>^ -- <file_path>
```

### 将文件恢复到特定提交状态
```bash
git checkout <commit> -- <file_path>
```

## 暂存区操作

### 暂存文件的部分变更
```bash
git add -p <file_name>
```

### 取消暂存的文件
```bash
git reset HEAD <file_name>
```

### 丢弃工作区的修改
```bash
git checkout -- <file_name>
```

## 清理操作

### 列出所有未跟踪的文件
```bash
git ls-files --others --exclude-standard
```

### 删除未跟踪的文件（先查看要删除的文件）
```bash
git clean -n
```

### 强制删除未跟踪的文件
```bash
git clean -f
```

### 删除未跟踪的目录
```bash
git clean -fd
```

# 注意事项
- 在执行清理操作前，建议先使用 -n 选项预览要删除的文件
- 使用 checkout 恢复文件时要小心，这会丢失当前的修改
- 建议在重要操作前先创建备份或提交当前更改
- 使用 git add -p 可以更精确地控制要暂存的内容