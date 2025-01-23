---
title: "Git 提交管理技巧"
slug: "commit-tips"
sequence: 4
description: "Git 提交相关的常用操作技巧和命令"
status: "published"
---

# 提交管理技巧

## 提交操作

### 修改最近的提交信息
```bash
# 修改最近一次提交的信息
git commit -v --amend

# 示例：修改提交信息以符合项目规范
# 原始提交："fix bug"
# 修改为："fix: 修复用户认证失败问题 (git.fun#1234)"
```

### 修改提交作者信息
```bash
# 修改作者信息为项目规范格式
git commit --amend --author='Git Fun <support@git.fun>'
```

### 重置作者信息
```bash
# 重置为 Git 全局配置中的作者信息
git commit --amend --reset-author --no-edit
```

## 撤销操作

### 创建新提交来撤销之前的提交
```bash
git revert <commit-ish>
```

### 重置到特定提交（私有分支）
```bash
git reset <commit-ish>
```

### 保留工作区更改的重置
```bash
git reset --keep <commit-ish>
```

## 提交历史

### 查看当前分支的提交历史
```bash
git cherry -v master
```

### 查看特定文件的提交历史
```bash
git log -p <file_name>
```

### 搜索提交内容
```bash
git log -S'<search_term>'
```

### 查看提交中修改的文件列表
```bash
git diff-tree --no-commit-id --name-only -r <commit-ish>
```

## 提交清理

### 删除敏感数据
```bash
git filter-branch --force --index-filter 'git rm --cached --ignore-unmatch <path-to-file>' --prune-empty --tag-name-filter cat -- --all
```

### 重置首次提交
```bash
git update-ref -d HEAD
```

## 高级技巧

### Git 钩子使用
```bash
# 查看可用的钩子模板
ls .git/hooks/

# 启用提交前检查钩子
cp .git/hooks/pre-commit.sample .git/hooks/pre-commit
chmod +x .git/hooks/pre-commit
```

### 二分查找调试
```bash
# 开始二分查找
git bisect start

# 标记当前版本为有问题的版本
git bisect bad

# 标记已知的正常版本
git bisect good <commit-ish>

# 完成调试后退出
git bisect reset
```

### 交互式变基
```bash
# 对最近的 n 个提交进行交互式变基
git rebase -i HEAD~<n>

# 对指定提交之后的所有提交进行变基
git rebase -i <commit-ish>
```

### 储藏管理
```bash
# 储藏当前修改
git stash push -m "描述信息"

# 查看储藏列表
git stash list

# 应用并删除最近的储藏
git stash pop

# 应用但保留储藏
git stash apply stash@{n}

# 删除特定储藏
git stash drop stash@{n}
```

### 子树合并
```bash
# 添加子项目仓库
git remote add -f <name> <repository>

# 合并子项目到指定目录
git merge -s subtree --squash <name>/master
```

### 提交签名
```bash
# 创建带签名的提交
git commit -S -m "提交信息"

# 验证提交签名
git verify-commit <commit-ish>
```

# 注意事项
- 在共享分支上使用 revert 而不是 reset
- 修改已推送的提交要谨慎
- 清理敏感数据后需要强制推送
- 建议在重要操作前创建备份分支
- 使用钩子时注意权限设置
- 交互式变基时注意保持提交历史清晰
- 定期清理不需要的储藏记录