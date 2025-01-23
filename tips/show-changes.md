---
title: "如何查看文件的历史变更？"
slug: "show-changes"
sequence: 1
description: "展示如何查看特定文件随时间的变更历史"
status: "published"
---

# 问题
如何查看一个文件在不同时间点的变更历史？

# 解决方案
使用 git log 命令可以查看特定文件的变更历史：

```bash
git log -p filename
```

# 示例
1. 查看 README.md 文件的所有变更历史：
```bash
git log -p README.md
```

2. 使用更简洁的格式查看变更：
```bash
git log --pretty=oneline README.md
```

3. 查看具体的改动内容：
```bash
git show commit_hash README.md
```

# 注意事项
- `-p` 参数会显示每次提交的具体改动
- 可以使用 `--follow` 参数追踪文件重命名历史
- 使用 `git blame` 可以查看每一行代码的最后修改者

# 相关命令
- `git log -p <file>`
- `git blame <file>`
- `git show <commit> <file>`