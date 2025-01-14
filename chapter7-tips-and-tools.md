# 第七章：Git 技巧与工具

## 7.1 常用技巧

### 别名设置
```bash
# 常用别名配置
git config --global alias.co checkout
git config --global alias.br branch
git config --global alias.ci commit
git config --global alias.st status
git config --global alias.unstage 'reset HEAD --'
git config --global alias.last 'log -1 HEAD'
git config --global alias.visual '!gitk'
```

高级别名示例：
```bash
# 漂亮的日志输出
git config --global alias.lg "log --color --graph --pretty=format:'%Cred%h%Creset -%C(yellow)%d%Creset %s %Cgreen(%cr) %C(bold blue)<%an>%Creset' --abbrev-commit"

# 查看分支最后一次提交
git config --global alias.latest 'for-each-ref --sort=-committerdate refs/heads/ --format="%(committerdate:short) %(refname:short)"'

# 交互式添加文件
git config --global alias.interactive 'add -i'
```

### 命令行技巧

#### 1. 高效导航
```bash
# 快速切换到上一个分支
git checkout -

# 查看最近切换的分支
git reflog

# 查找包含特定提交的分支
git branch --contains <commit>
```

#### 2. 搜索和过滤
```bash
# 搜索提交历史
git log --grep="bug fix"

# 搜索文件内容
git grep "TODO"

# 按作者筛选提交
git log --author="John"
```

#### 3. 文件操作
```bash
# 只显示修改的文件名
git diff --name-only

# 显示某个文件的修改历史
git log -p filename

# 查看谁修改了某行代码
git blame filename
```

### 提高效率的快捷操作

#### 1. 暂存操作
```bash
# 暂存部分文件修改
git add -p

# 取消暂存部分文件
git reset -p

# 暂存所有已跟踪文件的修改
git add -u
```

#### 2. 提交操作
```bash
# 修改最后一次提交
git commit --amend

# 快速提交所有修改
git commit -am "message"

# 空提交（用于触发CI/CD）
git commit --allow-empty -m "trigger build"
```

#### 3. 分支操作
```bash
# 创建并切换到新分支
git checkout -b new-branch

# 重命名分支
git branch -m old-name new-name

# 删除所有已合并的分支
git branch --merged | grep -v "\*" | xargs -n 1 git branch -d
```

## 7.2 实用工具

### GUI 客户端详解

#### 1. SourceTree
- 特点：
  - 免费使用
  - 直观的界面
  - 内置Git-flow支持
  - 可视化的分支管理
- 主要功能：
  - 提交历史查看
  - 分支管理
  - 冲突解决
  - 远程仓库操作

#### 2. GitKraken
- 特点：
  - 现代化界面
  - 跨平台支持
  - 集成化工作流
  - 强大的可视化
- 主要功能：
  - 交互式rebase
  - 合并冲突解决
  - 文件历史查看
  - 集成GitHub功能

#### 3. GitHub Desktop
- 特点：
  - 简洁界面
  - GitHub集成
  - 易于使用
  - 免费开源
- 主要功能：
  - 基本Git操作
  - Pull Request管理
  - 分支切换
  - 提交历史查看

### IDE 集成

#### 1. VS Code Git 集成
- 内置功能：
  - 源代码管理
  - 分支管理
  - 内联blame
  - 合并冲突解决
- 推荐插件：
  - GitLens
  - Git History
  - Git Graph
  - Git Blame

#### 2. IntelliJ IDEA Git 集成
- 主要功能：
  - 版本控制窗口
  - 本地历史
  - 智能合并
  - 交互式rebase
- 特色功能：
  - 变更列表管理
  - 搁置（Shelve）功能
  - 补丁创建和应用
  - 多仓库管理

### 辅助工具推荐

#### 1. diff 和合并工具
- Beyond Compare
- Meld
- P4Merge
- KDiff3

配置示例：
```bash
# 配置 Beyond Compare 作为 diff 工具
git config --global diff.tool bc3
git config --global difftool.bc3.path "c:/program files/beyond compare 3/bcomp.exe"

# 配置 Beyond Compare 作为合并工具
git config --global merge.tool bc3
git config --global mergetool.bc3.path "c:/program files/beyond compare 3/bcomp.exe"
```

#### 2. 命令行增强工具
- `tig`：文本模式界面的Git浏览器
- `lazygit`：终端UI的Git客户端
- `hub`：GitHub命令行工具
- `gh`：官方GitHub CLI

#### 3. Git Hook 工具
- husky：Git hooks管理
- commitlint：提交信息检查
- lint-staged：暂存文件检查

配置示例：
```json
{
  "husky": {
    "hooks": {
      "pre-commit": "lint-staged",
      "commit-msg": "commitlint -E HUSKY_GIT_PARAMS"
    }
  }
}
```

## 实践练习

### 练习 1：配置别名
1. 设置常用Git别名
2. 创建自定义复杂别名
3. 使用别名提高工作效率

### 练习 2：GUI工具使用
1. 安装并配置GUI客户端
2. 使用可视化工具进行基本操作
3. 尝试高级功能（如交互式rebase）

### 练习 3：IDE集成
1. 配置IDE的Git集成
2. 安装有用的Git插件
3. 使用IDE进行版本控制操作

## 注意事项
1. 选择适合自己的工具组合
2. 熟练使用命令行是基础
3. 定期更新工具版本
4. 备份重要的配置
5. 注意工具的安全性
