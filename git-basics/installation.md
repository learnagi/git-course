---
title: "Git 安装指南"
slug: "git-installation"
sequence: 2
description: "详细介绍如何在 Windows、macOS 和 Linux 系统上安装和配置 Git"
is_published: true
estimated_minutes: 20
---

# Git 安装指南

本指南将帮助你在不同的操作系统上安装 Git。我们将介绍 Windows、macOS 和 Linux 系统的安装步骤。

## Windows 系统安装

### 方法一：使用官方安装包

1. 访问 Git 官方网站：[https://git-scm.com/download/win](https://git-scm.com/download/win)
2. 下载适合你系统的版本（32位或64位）
3. 运行下载的安装程序，按照以下步骤进行：
   - 接受许可协议
   - 选择安装位置（建议使用默认路径：`C:\Program Files\Git`）
   - 选择组件（建议选择以下组件）：
     - [x] Windows Explorer integration
     - [x] Git Bash Here
     - [x] Git GUI Here
     - [x] Git LFS (Large File Support)
     - [x] Associate .git* configuration files with default text editor
     - [x] Associate .sh files to be run with Bash
   - 选择默认编辑器：
     - 推荐选择 VS Code（如果已安装）
     - 或选择 Notepad++
     - 如果都没有，可以选择 Vim（需要学习 Vim 的使用）
   - 调整 PATH 环境：
     - 推荐选择 "Git from the command line and also from 3rd-party software"
     - 这样可以在命令提示符和第三方软件中使用 Git
   - 选择 HTTPS 传输后端：
     - 保持默认的 OpenSSL
     - 这是最通用的安全传输层
   - 选择换行符处理方式：
     - 推荐 "Checkout Windows-style, commit Unix-style line endings"
     - 这样可以避免跨平台协作时的换行符问题
   - 选择终端模拟器：
     - 推荐选择 MinTTY
     - 提供更好的命令行体验
   - 配置额外选项：
     - [x] Enable file system caching
     - [x] Enable Git Credential Manager
     - [x] Enable symbolic links

### 方法二：使用包管理器（推荐）

#### 使用 Winget（Windows 10 2004 及以上版本）：
```bash
winget install --id Git.Git -e --source winget
```

#### 使用 Chocolatey：
1. 首先安装 Chocolatey（如果尚未安装）：
   ```powershell
   Set-ExecutionPolicy Bypass -Scope Process -Force; [System.Net.ServicePointManager]::SecurityProtocol = [System.Net.ServicePointManager]::SecurityProtocol -bor 3072; iex ((New-Object System.Net.WebClient).DownloadString('https://community.chocolatey.org/install.ps1'))
   ```

2. 安装 Git：
   ```bash
   choco install git
   ```

#### 使用 Scoop：
1. 安装 Scoop（如果尚未安装）：
   ```powershell
   Set-ExecutionPolicy RemoteSigned -Scope CurrentUser
   irm get.scoop.sh | iex
   ```

2. 安装 Git：
   ```bash
   scoop install git
   ```

## macOS 系统安装

### 方法一：使用 Homebrew（推荐）

1. 安装 Homebrew：
   ```bash
   /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
   ```

2. 配置 Homebrew 环境变量（M1/M2 芯片需要）：
   ```bash
   echo 'eval "$(/opt/homebrew/bin/brew shellenv)"' >> ~/.zprofile
   eval "$(/opt/homebrew/bin/brew shellenv)"
   ```

3. 使用 Homebrew 安装 Git：
   ```bash
   brew install git
   ```

### 方法二：使用官方安装包

1. 访问 Git 官方网站：[https://git-scm.com/download/mac](https://git-scm.com/download/mac)
2. 下载并安装最新版本的 Git
3. 安装过程中注意以下事项：
   - 给予安装程序必要的系统权限
   - 选择安装位置（建议使用默认位置）
   - 完成后在终端验证安装

### 方法三：通过 Xcode Command Line Tools

1. 打开终端，运行：
   ```bash
   xcode-select --install
   ```

2. 在弹出的窗口中点击"安装"
3. 等待下载和安装完成
4. 验证安装：
   ```bash
   git --version
   ```

## Linux 系统安装

### Ubuntu/Debian 系统：
```bash
# 更新软件包列表
sudo apt update

# 安装 Git
sudo apt install git

# 安装额外的 Git 工具（可选）
sudo apt install git-all
```

### CentOS/RHEL 系统：
```bash
# 安装 EPEL 仓库（推荐）
sudo yum install epel-release

# 安装 Git
sudo yum install git
```

### Fedora 系统：
```bash
# 安装 Git
sudo dnf install git

# 安装 Git 图形化工具（可选）
sudo dnf install git-gui gitk
```

### Arch Linux 系统：
```bash
# 安装 Git
sudo pacman -S git

# 安装图形化工具（可选）
sudo pacman -S git-gui
```

## 验证安装

安装完成后，执行以下步骤：

1. 打开终端（命令提示符）并输入：
   ```bash
   git --version
   ```

2. 验证 Git GUI 工具：
   ```bash
   git gui
   gitk
   ```

3. 测试 Git 基本功能：
   ```bash
   mkdir git-test
   cd git-test
   git init
   git status
   ```

## 初始配置

### 基本配置

1. 设置用户信息：
   ```bash
   # 设置全局用户名
   git config --global user.name "你的名字"
   
   # 设置全局邮箱
   git config --global user.email "你的邮箱@example.com"
   ```

2. 配置默认编辑器：
   ```bash
   # 使用 VS Code 作为默认编辑器
   git config --global core.editor "code --wait"
   
   # 或使用 vim
   git config --global core.editor vim
   ```

3. 配置默认分支名：
   ```bash
   git config --global init.defaultBranch main
   ```

### 高级配置

1. 配置换行符处理：
   ```bash
   # Windows 用户
   git config --global core.autocrlf true
   
   # Mac/Linux 用户
   git config --global core.autocrlf input
   ```

2. 配置颜色输出：
   ```bash
   git config --global color.ui auto
   ```

3. 配置命令别名（可选）：
   ```bash
   git config --global alias.co checkout
   git config --global alias.br branch
   git config --global alias.ci commit
   git config --global alias.st status
   git config --global alias.unstage 'reset HEAD --'
   git config --global alias.last 'log -1 HEAD'
   ```

4. 配置凭证存储：
   ```bash
   # Windows
   git config --global credential.helper wincred
   
   # macOS
   git config --global credential.helper osxkeychain
   
   # Linux
   git config --global credential.helper cache
   ```

## 常见问题解决

### Windows 系统

1. 命令提示符无法识别 git 命令：
   - 检查环境变量：
     ```batch
     echo %PATH%
     ```
   - 手动添加 Git 路径：
     ```batch
     setx PATH "%PATH%;C:\Program Files\Git\bin"
     ```
   - 重新打开命令提示符或重启电脑

2. SSL 证书问题：
   ```bash
   # 临时解决方案（不推荐）
   git config --global http.sslVerify false
   
   # 更新证书
   git config --global http.sslCAinfo "C:/Program Files/Git/mingw64/ssl/certs/ca-bundle.crt"
   ```

### macOS 系统

1. 权限问题：
   ```bash
   # 修复 /usr/local 权限
   sudo chown -R $(whoami) /usr/local/
   
   # 修复 Homebrew 权限
   sudo chown -R $(whoami) $(brew --prefix)/*
   ```

2. Homebrew 安装问题：
   ```bash
   # 诊断 Homebrew 问题
   brew doctor
   
   # 更新 Homebrew
   brew update
   
   # 清理缓存
   brew cleanup
   ```

### Linux 系统

1. 依赖问题：
   ```bash
   # Ubuntu/Debian
   sudo apt install -f
   sudo apt --fix-broken install
   
   # CentOS/RHEL
   sudo yum clean all
   sudo yum update
   ```

2. 版本更新：
   ```bash
   # Ubuntu
   sudo add-apt-repository ppa:git-core/ppa
   sudo apt update
   sudo apt install git
   
   # CentOS
   sudo yum remove git
   sudo yum install https://packages.endpointdev.com/rhel/7/os/x86_64/endpoint-repo.x86_64.rpm
   sudo yum install git
   ```

## 安装后配置

### 配置 SSH 密钥

1. 生成 SSH 密钥：
   ```bash
   ssh-keygen -t ed25519 -C "your_email@example.com"
   ```

2. 启动 SSH 代理：
   ```bash
   # Windows
   eval $(ssh-agent -s)
   
   # macOS/Linux
   eval "$(ssh-agent -s)"
   ```

3. 添加 SSH 密钥：
   ```bash
   ssh-add ~/.ssh/id_ed25519
   ```

### 配置 Git 代理（可选）

1. 设置 HTTP 代理：
   ```bash
   git config --global http.proxy http://proxy.example.com:8080
   ```

2. 设置 HTTPS 代理：
   ```bash
   git config --global https.proxy https://proxy.example.com:8080
   ```

## 推荐的开发工具集成

### VS Code 集成
1. 安装 Git 相关扩展：
   - GitLens
   - Git History
   - Git Graph

### JetBrains IDE 集成
1. 启用内置的 Git 集成
2. 配置 Git 可执行文件路径

### Sublime Text 集成
1. 安装 Git 插件
2. 配置命令面板集成

## 推荐的 GUI 客户端

### GitHub Desktop
- 优点：简单易用，适合初学者
- 下载：[https://desktop.github.com/](https://desktop.github.com/)
- 支持平台：Windows, macOS

### Sourcetree
- 优点：功能强大，可视化效果好
- 下载：[https://www.sourcetreeapp.com/](https://www.sourcetreeapp.com/)
- 支持平台：Windows, macOS

### GitKraken
- 优点：界面美观，功能丰富
- 下载：[https://www.gitkraken.com/](https://www.gitkraken.com/)
- 支持平台：Windows, macOS, Linux

### TortoiseGit（Windows 专用）
- 优点：与文件资源管理器深度集成
- 下载：[https://tortoisegit.org/](https://tortoisegit.org/)
- 支持平台：仅 Windows

## 学习资源

1. 官方文档：
   - [Git 官方文档](https://git-scm.com/doc)
   - [Pro Git 书籍](https://git-scm.com/book/zh/v2)

2. 在线学习平台：
   - [GitHub Learning Lab](https://lab.github.com/)
   - [Git 简易指南](http://rogerdudler.github.io/git-guide/index.zh.html)

3. 交互式学习：
   - [Learn Git Branching](https://learngitbranching.js.org/?locale=zh_CN)
   - [Git-it](https://github.com/jlord/git-it-electron)

## 下一步

完成安装和基本配置后，建议：

1. 熟悉基本的 Git 命令
2. 创建一个测试仓库进行练习
3. 学习分支管理和版本控制概念
4. 参与开源项目，积累实践经验
5. 探索高级 Git 功能和工作流程

记住：Git 是一个强大的版本控制工具，掌握它需要时间和练习。从基础开始，逐步深入学习更高级的功能。
