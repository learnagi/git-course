---
title: "如何在重置时保留未提交的更改？"
slug: "preserve-changes"
sequence: 3
description: "展示如何在重置提交时保留工作区的未提交更改"
status: "published"
---

# 问题
如何在重置到特定提交时保留工作区中未提交的更改？

# 解决方案
使用 git reset 命令的 --keep 选项可以在重置时保留未提交的本地更改：

```bash
git reset --keep <commit>
```

# 示例
1. 重置到特定提交并保留更改：
```bash
git reset --keep abc123
```

2. 重置到上一个提交并保留更改：
```bash
git reset --keep HEAD^
```

3. 重置到远程分支并保留更改：
```bash
git reset --keep origin/master
```

# 注意事项
- --keep 选项会保留工作区的修改
- 如果重置的提交与未提交的更改有冲突，命令将会失败
- 与 --hard 选项相比更安全，因为不会丢失未提交的更改
- 建议在执行前先确认工作区状态

# 相关命令
- `git reset --hard <commit>`
- `git reset --soft <commit>`
- `git reset --mixed <commit>`