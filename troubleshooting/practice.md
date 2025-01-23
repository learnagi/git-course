---
title: "故障排查实践"
slug: "troubleshooting-practice"
description: "通过实践案例掌握 Git 故障排查技巧"
is_published: true
estimated_minutes: 45
---

# 故障排查实践

本节将通过具体的实践案例，帮助你掌握 Git 故障排查的技巧。

## 实践一：提交问题修复

### 场景描述

开发者发现最近的提交包含了敏感信息，需要从历史记录中删除。

### 解决步骤

1. 定位问题提交
```bash
# 查看提交历史
git log --oneline

# 查看具体更改
git show <commit-hash>
```

2. 删除敏感信息
```bash
# 使用 filter-branch
git filter-branch --force --index-filter \
'git rm --cached --ignore-unmatch config.json' HEAD

# 强制推送更改
git push origin --force --all
```

3. 清理历史
```bash
# 清理备份
rm -rf .git/refs/original/
git reflog expire --expire=now --all
git gc --prune=now
```

## 实践二：合并冲突处理

### 场景描述

在合并分支时遇到复杂的冲突，需要正确处理以保持代码完整性。

### 解决步骤

1. 分析冲突
```bash
# 查看冲突文件
git status

# 查看具体冲突
git diff
```

2. 使用合并工具
```bash
# 配置合并工具
git config --global merge.tool vimdiff

# 启动合并工具
git mergetool
```

3. 完成合并
```bash
# 确认更改
git add .

# 提交合并结果
git commit -m "merge: resolve conflicts in feature branch"
```

## 实践三：丢失提交恢复

### 场景描述

意外删除了重要的提交，需要找回丢失的代码。

### 解决步骤

1. 查找丢失提交
```bash
# 查看 reflog
git reflog

# 查看具体提交
git show <commit-hash>
```

2. 恢复提交
```bash
# 创建新分支
git checkout -b recovery-branch

# 恢复提交
git cherry-pick <commit-hash>
```

3. 验证恢复
```bash
# 检查文件
git diff main

# 合并恢复的更改
git checkout main
git merge recovery-branch
```

## 练习

1. 模拟一个包含敏感信息的提交，然后尝试安全地删除它。

2. 创建两个分支进行并行开发，故意制造冲突，然后练习解决这些冲突。

3. 尝试使用不同的方法（reset、revert、cherry-pick）来处理错误的提交。

## 总结

通过本节的实践，你应该能够：

1. 处理敏感信息泄露
2. 解决复杂的合并冲突
3. 恢复丢失的提交
4. 使用各种 Git 工具进行故障排查

记住，在进行任何可能影响代码历史的操作之前，务必先创建备份。