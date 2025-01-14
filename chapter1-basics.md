# 第一章：Git 基础入门

## 1.1 Git 简介

### 什么是版本控制？
版本控制是一种记录文件内容变化，以便将来查阅特定版本修订情况的系统。版本控制最重要的是可以让你：
- 回溯到项目的任何历史状态
- 比较文件的不同版本
- 协作开发时不会互相干扰
- 追踪每个变更是谁在什么时候做的

### Git 的历史和特点
Git 诞生于 2005 年，由 Linux 之父 Linus Torvalds 创建。它的诞生源于 Linux 内核开发所使用的版本控制系统 BitKeeper 收回了免费使用权。这促使 Linus 花了两周时间用 C 语言写出了 Git 的第一个版本。

Git 的主要特点包括：
- **分布式系统**：每个开发者都拥有完整的代码仓库副本
- **高性能**：采用本地操作为主，大多数操作都很快
- **数据完整性**：使用 SHA-1 哈希算法确保数据完整性
- **分支管理**：轻量级的分支创建和合并
- **暂存区概念**：提供了一个中间层来精确控制提交内容

### Git 与其他版本控制系统的区别

#### 与集中式版本控制系统（如 SVN）的区别：
1. **存储方式**
   - SVN：增量存储，保存文件的差异
   - Git：快照存储，保存文件的完整状态

2. **联网需求**
   - SVN：需要持续联网
   - Git：可以本地工作，仅在同步时需要联网

3. **分支操作**
   - SVN：分支是完整的目录复制，操作较重
   - Git：分支仅是指针的移动，轻量快速

4. **版本号**
   - SVN：顺序数字版本号
   - Git：SHA-1 哈希值

## 1.2 安装和配置

### 各操作系统下的安装方法

#### macOS
```bash
# 使用 Homebrew 安装
brew install git

# 验证安装
git --version
```

#### Linux (Ubuntu/Debian)
```bash
sudo apt-get update
sudo apt-get install git
```

#### Windows
1. 下载 Git for Windows (https://git-scm.com/download/win)
2. 运行安装程序，按照向导完成安装

### 基本配置

安装完 Git 后，需要进行一些基本配置：

1. **设置用户信息**
```bash
git config --global user.name "Your Name"
git config --global user.email "your.email@example.com"
```

2. **配置默认编辑器**
```bash
git config --global core.editor "vim"  # 或其他编辑器
```

3. **查看配置**
```bash
git config --list
```

4. **配置别名（可选但推荐）**
```bash
git config --global alias.st status
git config --global alias.co checkout
git config --global alias.br branch
git config --global alias.ci commit
```

### Git GUI 工具介绍

虽然命令行是使用 Git 最有力的方式，但有时使用图形界面工具也很有帮助：

1. **SourceTree**
   - 免费的 Git 客户端
   - 提供直观的界面
   - 支持 Git-flow 工作流
   - 适合初学者

2. **GitKraken**
   - 现代化界面
   - 跨平台支持
   - 内置代码编辑器
   - 提供团队协作功能

3. **GitHub Desktop**
   - 简洁的界面
   - 与 GitHub 完美集成
   - 适合简单的 Git 操作

4. **VS Code 的 Git 集成**
   - 作为编辑器的内置功能
   - 提供基本的 Git 操作
   - 可通过插件扩展功能

## 实践练习

### 练习 1：配置 Git
1. 安装 Git
2. 配置用户名和邮箱
3. 验证配置是否正确

### 练习 2：创建第一个仓库
1. 创建一个新目录
2. 初始化 Git 仓库
3. 添加一个文件并提交

### 练习 3：尝试 GUI 工具
1. 安装一个 Git GUI 工具
2. 使用 GUI 工具克隆一个仓库
3. 尝试基本的文件操作
