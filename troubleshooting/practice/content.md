# 故障排除练习

本节提供一系列实践练习，帮助你掌握 Git 故障排除技能。

## 基础练习

### 练习 1：提交问题

1. 场景设置
```bash
# 初始化仓库
git init practice-repo
cd practice-repo

# 创建文件
echo "Initial content" > file.txt
git add file.txt
git commit -m "feat: initial commit"

# 错误提交
echo "Wrong content" > file.txt
git commit -am "feat: wrong commit"
```

2. 解决步骤
```bash
# 修改最后提交
git commit --amend

# 撤销提交
git reset --soft HEAD~1

# 重写提交
git rebase -i HEAD~2
```

### 练习 2：分支问题

1. 场景设置
```bash
# 创建分支
git checkout -b feature-branch

# 修改文件
echo "Feature content" > feature.txt
git add feature.txt
git commit -m "feat: add feature"

# 切换分支
git checkout main
echo "Main content" > feature.txt
git add feature.txt
git commit -m "feat: update feature"
```

2. 解决步骤
```bash
# 合并分支
git merge feature-branch

# 解决冲突
git mergetool

# 完成合并
git add feature.txt
git commit -m "merge: resolve conflicts"
```

## 高级练习

### 练习 1：历史问题

1. 场景设置
```bash
# 创建提交
for i in {1..5}; do
  echo "Content $i" > file$i.txt
  git add file$i.txt
  git commit -m "feat: add file $i"
done

# 添加大文件
dd if=/dev/zero of=large-file.bin bs=1M count=100
git add large-file.bin
git commit -m "feat: add large file"
```

2. 解决步骤
```bash
# 分析历史
git log --oneline
git rev-list --objects --all

# 清理大文件
git filter-branch --tree-filter 'rm -f large-file.bin' HEAD

# 重写历史
git rebase -i HEAD~5
```

### 练习 2：存储问题

1. 场景设置
```bash
# 创建大文件
for i in {1..5}; do
  dd if=/dev/zero of=large-file-$i.bin bs=1M count=100
  git add large-file-$i.bin
  git commit -m "feat: add large file $i"
done
```

2. 解决步骤
```bash
# 配置 LFS
git lfs install
git lfs track "*.bin"

# 迁移文件
git lfs migrate import --include="*.bin"

# 优化存储
git gc --aggressive
git prune
```

## 工具练习

### 练习 1：工具配置

1. 场景设置
```bash
# 检查配置
git config --list

# 设置编辑器
git config --global core.editor "vim"

# 设置别名
git config --global alias.co checkout
```

2. 解决步骤
```bash
# 修改配置
git config --global core.editor "code --wait"

# 更新别名
git config --global alias.co "checkout"
git config --global alias.br "branch"

# 验证配置
git config --list
```

### 练习 2：工具集成

1. 场景设置
```bash
# 创建工作流
mkdir -p .github/workflows
touch .github/workflows/ci.yml

# 配置 IDE
touch .vscode/settings.json
```

2. 解决步骤
```yaml
# 配置 CI
name: CI

on:
  push:
    branches: [ main ]
  pull_request:
    branches: [ main ]

jobs:
  test:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v2
      - name: Run tests
        run: npm test
```

```json
// 配置 VS Code
{
  "git.enableSmartCommit": true,
  "git.confirmSync": false,
  "git.autofetch": true
}
```

## 安全练习

### 练习 1：凭证管理

1. 场景设置
```bash
# 检查凭证
git config --global credential.helper

# 创建 SSH 密钥
ssh-keygen -t ed25519 -C "email@example.com"
```

2. 解决步骤
```bash
# 配置凭证
git config --global credential.helper store

# 配置 SSH
eval "$(ssh-agent -s)"
ssh-add ~/.ssh/id_ed25519

# 测试连接
ssh -T git@github.com
```

### 练习 2：安全扫描

1. 场景设置
```bash
# 创建配置文件
echo "API_KEY=secret123" > config.ini
git add config.ini
git commit -m "feat: add config"
```

2. 解决步骤
```bash
# 安装工具
npm install -g git-secrets

# 配置规则
git secrets --install
git secrets --register-aws

# 扫描仓库
git secrets --scan
```

## 性能练习

### 练习 1：仓库优化

1. 场景设置
```bash
# 创建大量文件
for i in {1..1000}; do
  echo "Content $i" > file$i.txt
  git add file$i.txt
  git commit -m "feat: add file $i"
done
```

2. 解决步骤
```bash
# 检查大小
du -sh .git

# 优化存储
git gc --aggressive
git repack -ad
git prune

# 验证优化
git count-objects -vH
```

### 练习 2：网络优化

1. 场景设置
```bash
# 克隆大型仓库
git clone https://github.com/large/repo.git

# 拉取更新
git fetch origin
```

2. 解决步骤
```bash
# 配置压缩
git config --global core.compression 9

# 优化克隆
git clone --depth 1 https://github.com/large/repo.git
git clone --single-branch --branch main https://github.com/large/repo.git

# 配置代理
git config --global http.proxy http://proxy.example.com:8080
```

## 应急练习

### 练习 1：数据恢复

1. 场景设置
```bash
# 创建文件
echo "Important content" > important.txt
git add important.txt
git commit -m "feat: add important file"

# 删除文件
git rm important.txt
git commit -m "feat: remove important file"
```

2. 解决步骤
```bash
# 查找提交
git reflog

# 恢复文件
git checkout HEAD@{1} important.txt

# 创建恢复分支
git branch recovery HEAD@{1}
```

### 练习 2：系统恢复

1. 场景设置
```bash
# 备份配置
git config --list > config-backup.txt

# 重置配置
git config --global --unset-all
```

2. 解决步骤
```bash
# 恢复配置
while read line; do
  git config --global "${line%=*}" "${line#*=}"
done < config-backup.txt

# 验证配置
git config --list
```

## 实战练习

### 练习 1：综合问题

1. 场景设置
```bash
# 创建项目
git init complex-project
cd complex-project

# 添加文件
echo "Initial content" > main.txt
git add main.txt
git commit -m "feat: initial commit"

# 创建分支
git checkout -b feature
echo "Feature content" > feature.txt
git add feature.txt
git commit -m "feat: add feature"

# 修改主分支
git checkout main
echo "Updated content" > main.txt
git commit -am "feat: update main"
```

2. 解决步骤
```bash
# 合并分支
git merge feature

# 解决冲突
git mergetool

# 优化仓库
git gc --aggressive
git prune
```

### 练习 2：团队问题

1. 场景设置
```bash
# 克隆项目
git clone https://github.com/team/project.git
cd project

# 创建功能
git checkout -b feature/new
echo "New feature" > feature.txt
git add feature.txt
git commit -m "feat: add new feature"

# 推送更改
git push origin feature/new
```

2. 解决步骤
```bash
# 更新分支
git fetch origin
git rebase origin/main

# 解决冲突
git mergetool

# 完成功能
git flow feature finish feature/new
```

## 学习要点
1. 掌握问题诊断
2. 熟练工具使用
3. 优化性能安全
4. 应对紧急情况

## 小结
通过这些练习，你应该能够熟练处理各种 Git 问题，并在实际工作中应用这些技能。

## 下一步
1. 深入学习工具
2. 优化工作流程
3. 加强安全意识
4. 提高处理能力
