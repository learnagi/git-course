---
title: "如何列出所有冲突文件？"
slug: "list-conflicts"
sequence: 4
description: "展示如何列出 Git 仓库中所有存在冲突的文件"
status: "published"
---

# 问题
如何快速找出 Git 仓库中所有存在合并冲突的文件？

# 解决方案
使用 git diff 命令配合 --name-only 和 --diff-filter=U 选项可以列出所有冲突文件：

```bash
git diff --name-only --diff-filter=U
```

# 示例
1. 列出当前所有冲突文件：
```bash
git diff --name-only --diff-filter=U
```

2. 查看冲突文件的详细信息：
```bash
git status
```

3. 查看具体的冲突内容：
```bash
git diff
```

# 注意事项
- --name-only 选项只显示文件名
- --diff-filter=U 筛选出未合并（有冲突）的文件
- 建议配合 git status 使用以获取更多信息
- 解决冲突后记得使用 git add 标记为已解决

# 相关命令
- `git status`
- `git diff`
- `git checkout --ours <file>`
- `git checkout --theirs <file>`