---
title: "Git 配置管理技巧"
slug: "config-tips"
sequence: 2
description: "Git 配置相关的常用技巧和命令"
status: "published"
---

# Git 配置管理技巧

## 基本配置

### 列出所有配置和别名
```bash
git config --list
```

### 编辑全局配置
```bash
git config --global -e
```

### 编辑本地仓库配置
```bash
git config --local -e
```

## 常用配置项

### 设置大小写敏感
```bash
git config --global core.ignorecase false
```

### 添加自定义编辑器
```bash
git config --global core.editor "vim"
```

### 开启自动纠错
```bash
git config --global help.autocorrect 1
```

### 防止 CRLF 自动替换
```bash
git config --global core.autocrlf false
```

## 别名配置

### 列出所有 Git 别名
```bash
git config --get-regexp alias
```

### 删除全局配置项
```bash
git config --global --unset <entry-name>
```

## 远程仓库配置

### 修改远程仓库 URL
```bash
git remote set-url origin <new-url>
```

### 使用 SSH 替代 HTTPS
```bash
git remote set-url origin git@github.com:username/repo.git
```

# 注意事项
- 修改配置前先备份当前配置
- 全局配置会影响所有仓库
- 本地配置优先级高于全局配置
- 某些配置可能影响到团队协作