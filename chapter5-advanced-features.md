# 第五章：Git 高级特性

## 5.1 Git 内部原理

### Git 对象类型

#### 1. blob 对象
- 存储文件内容
- 不包含文件名等元数据
- 通过 SHA-1 值唯一标识
```bash
# 查看 blob 对象内容
git cat-file -p <blob-hash>
```

#### 2. tree 对象
- 记录目录结构和文件权限
- 包含 blob 对象和其他 tree 对象的引用
```bash
# 查看 tree 对象内容
git cat-file -p <tree-hash>
```

#### 3. commit 对象
- 包含提交信息、作者、时间等
- 指向对应的 tree 对象
- 包含父提交的引用
```bash
# 查看 commit 对象内容
git cat-file -p <commit-hash>
```

#### 4. tag 对象
- 存储标签信息
- 可以指向任何类型的 Git 对象
```bash
# 查看 tag 对象内容
git cat-file -p <tag-hash>
```

### Git 引用

#### 1. 分支引用
- 存储在 `.git/refs/heads/` 目录下
- 指向最新的提交对象
```bash
# 查看分支指向的提交
git rev-parse <branch-name>
```

#### 2. 远程引用
- 存储在 `.git/refs/remotes/` 目录下
- 记录远程仓库的分支状态
```bash
# 查看远程分支指向的提交
git rev-parse origin/<branch-name>
```

#### 3. 标签引用
- 存储在 `.git/refs/tags/` 目录下
- 可以是轻量标签或附注标签
```bash
# 创建附注标签
git tag -a v1.0 -m "Version 1.0"
```

### 包文件
- Git 会定期将松散对象打包
- 减少存储空间
- 提高访问效率
```bash
# 手动触发打包
git gc

# 查看打包统计
git count-objects -v
```

## 5.2 高级操作

### git rebase：变基操作
```bash
# 基本变基
git rebase <base-branch>

# 交互式变基
git rebase -i HEAD~3

# 中止变基
git rebase --abort

# 继续变基
git rebase --continue
```

交互式变基命令：
- `pick`：使用提交
- `reword`：修改提交信息
- `edit`：修改提交内容
- `squash`：合并到上一个提交
- `fixup`：合并且丢弃提交信息
- `drop`：删除提交

### git cherry-pick：选择性合并
```bash
# 合并单个提交
git cherry-pick <commit-hash>

# 合并多个提交
git cherry-pick <commit1>..<commit2>

# 不自动提交
git cherry-pick -n <commit-hash>
```

### git reflog：引用日志
```bash
# 查看引用日志
git reflog

# 查看特定引用的日志
git reflog show <reference>

# 恢复到特定状态
git reset --hard HEAD@{2}
```

### git submodule：子模块管理
```bash
# 添加子模块
git submodule add <repository>

# 更新子模块
git submodule update --init --recursive

# 删除子模块
git submodule deinit <path>
```

## 5.3 工作区管理

### .gitignore 文件
```gitignore
# 忽略所有 .log 文件
*.log

# 忽略 build 目录
/build/

# 不忽略特定文件
!important.log

# 忽略特定目录下的所有文件
logs/*
```

常见的忽略模式：
- `*` 匹配任意字符
- `?` 匹配单个字符
- `[abc]` 匹配方括号中的任意字符
- `**` 匹配任意中间目录

### git stash：暂存修改
```bash
# 暂存修改
git stash

# 带说明的暂存
git stash save "message"

# 查看暂存列表
git stash list

# 应用暂存
git stash apply stash@{0}

# 删除暂存
git stash drop stash@{0}

# 应用并删除暂存
git stash pop
```

### git clean：清理工作区
```bash
# 查看将被删除的文件
git clean -n

# 删除未跟踪的文件
git clean -f

# 删除未跟踪的文件和目录
git clean -fd

# 删除忽略的文件
git clean -fX
```

## 实践练习

### 练习 1：变基操作
1. 创建一系列提交
2. 使用交互式变基重写历史
3. 解决变基冲突

### 练习 2：子模块管理
1. 添加一个子模块
2. 更新子模块
3. 在主项目中提交子模块更改

### 练习 3：工作区管理
1. 创建 .gitignore 文件
2. 使用 stash 管理临时修改
3. 清理工作区

## 注意事项
1. 变基操作会改变提交历史，需谨慎使用
2. 定期清理和优化仓库以提高性能
3. 合理使用 .gitignore 避免提交不必要的文件
4. 使用 stash 时注意及时应用或删除
5. 在团队协作中谨慎使用历史修改操作
