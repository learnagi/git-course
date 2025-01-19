---
title: "撤销操作"
slug: "undo-operations"
sequence: 3
description: "学习 Git 中的各种撤销操作，包括撤销修改、重置提交等"
is_published: true
estimated_minutes: 25
---

# Git 撤销操作

在使用 Git 过程中，经常需要撤销某些操作。本节将介绍 Git 中的各种撤销命令及其使用场景。

## 撤销工作区修改

### 撤销未暂存的修改

1. 撤销单个文件的修改：
   ```bash
   git checkout -- filename
   # 或使用新语法
   git restore filename
   ```

2. 撤销所有未暂存的修改：
   ```bash
   git checkout .
   # 或使用新语法
   git restore .
   ```

### 撤销已暂存的修改

1. 取消暂存单个文件：
   ```bash
   git reset HEAD filename
   # 或使用新语法
   git restore --staged filename
   ```

2. 取消所有暂存：
   ```bash
   git reset HEAD
   # 或使用新语法
   git restore --staged .
   ```

## 修改提交

### 修改最后一次提交

1. 修改提交信息：
   ```bash
   git commit --amend -m "新的提交信息"
   ```

2. 追加文件到最后一次提交：
   ```bash
   git add forgotten_file
   git commit --amend --no-edit
   ```

### 撤销提交

1. 创建新的提交来撤销之前的提交：
   ```bash
   git revert <commit-hash>
   ```

2. 重置到指定提交：
   ```bash
   # 保留工作区修改
   git reset --soft <commit-hash>
   
   # 重置工作区和暂存区
   git reset --hard <commit-hash>
   ```

## 暂存操作

### 储藏更改

1. 储藏当前更改：
   ```bash
   git stash
   ```

2. 储藏时添加说明：
   ```bash
   git stash save "修改说明"
   ```

### 管理储藏

1. 查看储藏列表：
   ```bash
   git stash list
   ```

2. 应用储藏：
   ```bash
   # 应用最近的储藏
   git stash apply
   
   # 应用指定的储藏
   git stash apply stash@{n}
   ```

3. 删除储藏：
   ```bash
   # 删除最近的储藏
   git stash drop
   
   # 删除指定的储藏
   git stash drop stash@{n}
   ```

## 分支操作撤销

### 删除分支

1. 删除已合并的分支：
   ```bash
   git branch -d branch_name
   ```

2. 强制删除分支：
   ```bash
   git branch -D branch_name
   ```

### 恢复已删除的分支

1. 查找分支的最后一次提交：
   ```bash
   git reflog
   ```

2. 基于提交创建新分支：
   ```bash
   git branch branch_name <commit-hash>
   ```

## 高级撤销操作

### 交互式变基

1. 开始交互式变基：
   ```bash
   git rebase -i <commit-hash>
   ```

2. 常用变基命令：
   - pick：保留提交
   - reword：修改提交信息
   - edit：修改提交内容
   - squash：合并到上一个提交
   - drop：删除提交

### 清理操作

1. 清理未跟踪的文件：
   ```bash
   # 预览要清理的文件
   git clean -n
   
   # 实际清理文件
   git clean -f
   ```

2. 清理包括目录：
   ```bash
   git clean -fd
   ```

## 最佳实践

1. **安全原则**
   - 在重要操作前创建备份分支
   - 使用 `--dry-run` 预览效果
   - 谨慎使用 `--hard` 选项

2. **提交管理**
   - 及时提交有意义的更改
   - 保持提交历史清晰
   - 适当使用 `git revert`

3. **储藏使用**
   - 为储藏添加清晰的说明
   - 及时处理储藏的内容
   - 定期清理不需要的储藏

## 常见问题

1. 意外的重置
   - 使用 reflog 恢复
   - 检查重要文件的备份
   - 确认命令参数

2. 储藏冲突
   - 解决冲突后重新储藏
   - 使用不同的储藏说明
   - 分步骤应用储藏

3. 分支误删
   - 使用 reflog 查找记录
   - 及时创建备份分支
   - 谨慎使用强制删除

## 练习

1. 练习不同类型的撤销操作
2. 使用储藏管理临时更改
3. 尝试交互式变基
4. 恢复误删的提交或分支 