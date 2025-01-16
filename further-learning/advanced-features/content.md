# 高级特性

本节将介绍 Git 的高级特性和功能。

## 高级命令

### 1. 变基操作

1. 交互式变基
```bash
# 开始变基
git rebase -i HEAD~3

# 变基命令
# p, pick = 使用提交
# r, reword = 修改提交信息
# e, edit = 修改提交
# s, squash = 合并到前一个提交
# f, fixup = 合并到前一个提交，丢弃信息
# d, drop = 删除提交
```

2. 变基策略
```bash
# 拆分提交
git rebase -i HEAD~1
# 编辑提交
git reset HEAD^
git add file1.txt
git commit -m "feat: first part"
git add file2.txt
git commit -m "feat: second part"
git rebase --continue

# 合并提交
git rebase -i HEAD~3
# 将后面的提交标记为 squash
```

### 2. 子树操作

1. 子树添加
```bash
# 添加远程仓库
git remote add -f sub-repo https://github.com/user/sub-repo.git

# 添加子树
git subtree add --prefix=sub-repo sub-repo main --squash

# 更新子树
git subtree pull --prefix=sub-repo sub-repo main --squash
```

2. 子树推送
```bash
# 推送更改
git subtree push --prefix=sub-repo sub-repo main

# 分割子树
git subtree split --prefix=sub-repo -b split-branch

# 提取子树
git subtree extract --prefix=sub-repo -b extract-branch
```

### 3. 钩子脚本

1. 客户端钩子
```bash
# pre-commit 钩子
cat > .git/hooks/pre-commit << 'EOF'
#!/bin/sh
npm test
if [ $? -ne 0 ]; then
  echo "Tests failed, commit aborted"
  exit 1
fi
EOF
chmod +x .git/hooks/pre-commit

# commit-msg 钩子
cat > .git/hooks/commit-msg << 'EOF'
#!/bin/sh
commit_msg=$(cat $1)
if ! echo "$commit_msg" | grep -qE "^(feat|fix|docs|style|refactor|test|chore):"; then
  echo "Invalid commit message format"
  exit 1
fi
EOF
chmod +x .git/hooks/commit-msg
```

2. 服务器钩子
```bash
# pre-receive 钩子
cat > hooks/pre-receive << 'EOF'
#!/bin/sh
while read oldrev newrev refname; do
  branch=$(git rev-parse --symbolic --abbrev-ref $refname)
  if [ "$branch" = "main" ]; then
    echo "Direct push to main branch is not allowed"
    exit 1
  fi
done
EOF
chmod +x hooks/pre-receive

# post-receive 钩子
cat > hooks/post-receive << 'EOF'
#!/bin/sh
while read oldrev newrev refname; do
  if [ "$refname" = "refs/heads/main" ]; then
    echo "Deploying main branch..."
    cd /var/www/html
    git pull origin main
    npm install
    npm run build
  fi
done
EOF
chmod +x hooks/post-receive
```

## 高级功能

### 1. 二分查找

1. 基本使用
```bash
# 开始二分查找
git bisect start

# 标记好的版本
git bisect good v1.0.0

# 标记坏的版本
git bisect bad HEAD

# 检查版本
git bisect good/bad

# 结束查找
git bisect reset
```

2. 自动化查找
```bash
# 创建测试脚本
cat > test.sh << 'EOF'
#!/bin/sh
npm test
exit $?
EOF
chmod +x test.sh

# 自动二分查找
git bisect start HEAD v1.0.0
git bisect run ./test.sh
```

### 2. 补丁管理

1. 创建补丁
```bash
# 创建单个提交的补丁
git format-patch -1 HEAD

# 创建多个提交的补丁
git format-patch HEAD~3

# 创建分支的补丁
git format-patch main..feature-branch

# 指定输出目录
git format-patch -o patches/ HEAD~3
```

2. 应用补丁
```bash
# 检查补丁
git apply --check 0001-patch.patch

# 应用补丁
git am 0001-patch.patch

# 应用目录中的所有补丁
git am patches/*.patch

# 处理冲突
git am --abort
git am --continue
```

### 3. 归档管理

1. 创建归档
```bash
# 创建 tar 归档
git archive --format=tar HEAD > project.tar

# 创建 zip 归档
git archive --format=zip HEAD > project.zip

# 指定输出文件
git archive --output=project.tar.gz --format=tar HEAD

# 包含子模块
git submodule foreach --recursive 'git archive --format=tar HEAD > $sha1.tar'
```

2. 导出版本
```bash
# 导出特定版本
git archive v1.0.0 | tar -x -C /target/directory

# 导出特定目录
git archive --format=zip HEAD:src > source.zip

# 添加前缀
git archive --prefix=project/ HEAD > project.tar

# 排除文件
git archive --format=tar HEAD $(git ls-files | grep -v "\.git") > project.tar
```

## 高级配置

### 1. 属性配置

1. 文件属性
```bash
# .gitattributes 文件
*.txt text
*.jpg binary
*.sh text eol=lf
*.bat text eol=crlf

# 差异处理
*.pdf diff=pdf
*.docx diff=word

# 合并策略
*.xml merge=xmlmerge
database.xml merge=ours
```

2. 过滤器
```bash
# 配置过滤器
git config filter.indent.clean indent
git config filter.indent.smudge cat

# .gitattributes
*.c filter=indent
*.h filter=indent

# 清理脚本
cat > .git/hooks/pre-commit << 'EOF'
#!/bin/sh
git diff --cached --name-only | grep '\.c$' | xargs indent
git diff --cached --name-only | grep '\.c$' | xargs git add
EOF
chmod +x .git/hooks/pre-commit
```

### 2. 别名配置

1. 基本别名
```bash
# 常用别名
git config --global alias.co checkout
git config --global alias.br branch
git config --global alias.ci commit
git config --global alias.st status

# 日志别名
git config --global alias.lg "log --graph --pretty=format:'%Cred%h%Creset -%C(yellow)%d%Creset %s %Cgreen(%cr) %C(bold blue)<%an>%Creset' --abbrev-commit"
```

2. 高级别名
```bash
# 功能别名
git config --global alias.undo "reset HEAD~1 --mixed"
git config --global alias.amend "commit --amend --reuse-message=HEAD"
git config --global alias.cleanup "!git branch --merged | grep -v '\\*' | xargs -n 1 git branch -d"

# 脚本别名
git config --global alias.release '!sh -c "git tag -a $1 -m \"Release $1\" && git push origin $1"' -
```

### 3. 工作流配置

1. 分支配置
```bash
# 分支保护
git config branch.main.mergeoptions "--no-ff"
git config branch.main.rebase true

# 推送设置
git config push.default current
git config push.followTags true

# 拉取设置
git config pull.rebase true
git config pull.ff only
```

2. 远程配置
```bash
# 远程设置
git config remote.origin.prune true
git config remote.origin.tagopt --tags

# 代理设置
git config http.proxy http://proxy.example.com:8080
git config https.proxy https://proxy.example.com:8080

# 认证设置
git config credential.helper store
git config credential.helper 'cache --timeout=3600'
```

## 高级技巧

### 1. 工作区管理

1. 工作区切换
```bash
# 保存工作区
git stash save "WIP: feature implementation"
git stash push -m "WIP: bug fix"

# 应用工作区
git stash apply stash@{0}
git stash pop

# 管理工作区
git stash list
git stash drop stash@{0}
git stash clear
```

2. 工作区操作
```bash
# 创建补丁
git stash show -p > patch.diff

# 应用补丁
git apply patch.diff

# 交互式储藏
git stash -p

# 包含未跟踪文件
git stash -u
```

### 2. 历史管理

1. 历史修改
```bash
# 修改作者信息
git filter-branch --env-filter '
if [ "$GIT_AUTHOR_EMAIL" = "old@example.com" ]; then
    GIT_AUTHOR_EMAIL="new@example.com"
    GIT_AUTHOR_NAME="New Name"
fi
' HEAD

# 删除文件历史
git filter-branch --force --index-filter \
  'git rm --cached --ignore-unmatch path/to/file' \
  --prune-empty --tag-name-filter cat -- --all
```

2. 历史分析
```bash
# 查看贡献统计
git shortlog -sn
git log --author="username" --pretty=tformat: --numstat

# 分析文件历史
git log --follow -p -- path/to/file
git blame -w -M -C path/to/file

# 查找提交
git log --grep="keyword"
git log -S"code-string" --patch
```

### 3. 仓库维护

1. 仓库优化
```bash
# 检查完整性
git fsck --full

# 优化存储
git gc --aggressive --prune=now
git repack -ad

# 清理文件
git clean -fd
git clean -fdx
```

2. 仓库迁移
```bash
# 克隆镜像
git clone --mirror old-repo new-repo
cd new-repo
git remote set-url origin new-url
git push --mirror

# 更新引用
git remote rename origin old-origin
git remote add origin new-url
git push -u origin --all
git push -u origin --tags
```

## 学习资源

### 1. 官方资源

1. 文档
```markdown
## Git 文档
- [Git 参考手册](https://git-scm.com/docs)
- [Git 书籍](https://git-scm.com/book/en/v2)
- [Git 教程](https://git-scm.com/docs/gittutorial)

## Git 社区
- [Git 邮件列表](https://git-scm.com/community)
- [Git Wiki](https://git.wiki.kernel.org/index.php/Main_Page)
```

2. 工具
```markdown
## Git 工具
- [Git GUI 客户端](https://git-scm.com/downloads/guis)
- [Git 命令行工具](https://git-scm.com/downloads)
- [Git 扩展](https://git-scm.com/docs/git#_external_commands)
```

### 2. 扩展资源

1. 学习资源
```markdown
## 在线教程
- [GitHub Learning Lab](https://lab.github.com/)
- [Atlassian Git 教程](https://www.atlassian.com/git/tutorials)
- [Git Immersion](http://gitimmersion.com/)

## 练习资源
- [Learn Git Branching](https://learngitbranching.js.org/)
- [Git Katas](https://github.com/eficode-academy/git-katas)
```

2. 工具资源
```markdown
## 开发工具
- [Git 集成开发环境](https://git-scm.com/downloads/guis)
- [Git 命令行增强](https://github.com/tj/git-extras)
- [Git 流程工具](https://github.com/nvie/gitflow)

## 可视化工具
- [Git Graph](https://marketplace.visualstudio.com/items?itemName=mhutchie.git-graph)
- [GitKraken](https://www.gitkraken.com/)
- [SourceTree](https://www.sourcetreeapp.com/)
```

## 学习要点
1. 掌握高级命令
2. 理解高级功能
3. 熟悉高级配置
4. 运用高级技巧

## 小结
通过本节的学习，你应该对 Git 的高级特性有了深入的了解，并能够在实际工作中运用这些功能。

## 练习题
1. 使用高级命令
2. 配置工作环境
3. 优化工作流程
4. 解决复杂问题
