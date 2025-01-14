# 第八章：Git 进阶话题

## 8.1 大型项目管理

### 模块化管理

#### 1. Git Submodules
```bash
# 添加子模块
git submodule add <repository> <path>

# 初始化子模块
git submodule init

# 更新子模块
git submodule update --recursive

# 更新所有子模块到最新版本
git submodule update --remote --merge
```

配置文件 `.gitmodules`:
```ini
[submodule "lib/theme"]
    path = lib/theme
    url = https://github.com/username/theme.git
    branch = master
```

#### 2. Git Subtree
```bash
# 添加子树
git subtree add --prefix=<prefix> <repository> <ref>

# 更新子树
git subtree pull --prefix=<prefix> <repository> <ref>

# 推送子树更改
git subtree push --prefix=<prefix> <repository> <branch>
```

### 性能优化

#### 1. 仓库瘦身
```bash
# 查找大文件
git rev-list --objects --all | grep -f <(git verify-pack -v .git/objects/pack/*.idx | sort -k 3 -n | tail -10 | awk '{print$1}')

# 清理大文件历史
git filter-branch --force --index-filter \
  'git rm --cached --ignore-unmatch path/to/large/file' \
  --prune-empty --tag-name-filter cat -- --all

# 强制垃圾回收
git gc --prune=now --aggressive
```

#### 2. 克隆优化
```bash
# 浅克隆
git clone --depth 1 <repository>

# 单分支克隆
git clone --single-branch --branch <branch> <repository>

# 稀疏检出
git clone --filter=blob:none <repository>
git sparse-checkout set <directory>
```

#### 3. 缓存配置
```bash
# 配置文件系统缓存
git config --global core.fscache true

# 配置打包限制
git config --global pack.windowMemory "100m"
git config --global pack.packSizeLimit "100m"

# 配置增量打包
git config --global pack.deltaCacheSize "100m"
```

### 大文件处理

#### 1. Git LFS (Large File Storage)
```bash
# 安装 Git LFS
git lfs install

# 跟踪大文件
git lfs track "*.psd"
git lfs track "*.zip"

# 查看跟踪的文件模式
git lfs track

# 推送大文件
git lfs push origin master
```

配置文件 `.gitattributes`:
```
*.psd filter=lfs diff=lfs merge=lfs -text
*.zip filter=lfs diff=lfs merge=lfs -text
```

## 8.2 安全性

### 敏感信息处理

#### 1. 配置文件管理
```bash
# 创建示例配置文件
cp config.example.yml config.yml
echo "config.yml" >> .gitignore

# 使用环境变量
export DATABASE_URL="mysql://user:pass@localhost/db"
```

#### 2. 密钥管理
```bash
# 使用 git-secret
git secret init
git secret tell user@email.com
git secret add credentials.txt
git secret hide

# 使用 git-crypt
git-crypt init
git-crypt add-gpg-user USER_ID
git-crypt status
```

#### 3. 清理敏感信息
```bash
# 从所有提交中删除敏感文件
git filter-branch --force --index-filter \
  "git rm --cached --ignore-unmatch PATH_TO_FILE" \
  --prune-empty --tag-name-filter cat -- --all

# 强制推送更改
git push origin --force --all
```

### 访问控制

#### 1. 分支保护
```bash
# 设置分支保护规则
git config branch.master.protect true

# 要求签名提交
git config --global commit.gpgsign true

# 配置提交模板
git config --global commit.template ~/.gitmessage
```

#### 2. 权限管理
- 仓库级别权限
  - 读取权限
  - 写入权限
  - 管理权限
- 分支级别权限
  - 推送限制
  - 合并限制
  - 删除限制

### 安全最佳实践

#### 1. 提交签名
```bash
# 生成 GPG 密钥
gpg --gen-key

# 配置 Git 使用 GPG 密钥
git config --global user.signingkey <KEY_ID>

# 创建签名提交
git commit -S -m "Signed commit"

# 创建签名标签
git tag -s v1.0 -m "Signed tag"
```

#### 2. 审计日志
```bash
# 查看提交历史
git log --pretty=format:"%h %ad | %s%d [%an]" --graph --date=short

# 查看文件修改历史
git log --follow -p -- path/to/file

# 查看特定作者的提交
git log --author="username"
```

## 8.3 高级工作流

### 1. Trunk Based Development
- 特点：
  - 所有开发者直接在主干分支工作
  - 使用功能开关控制新功能
  - 频繁集成和部署
- 实践：
  ```bash
  # 创建功能分支
  git checkout -b feature/quick-fix

  # 频繁合并到主干
  git checkout main
  git merge feature/quick-fix
  ```

### 2. GitHub Flow
- 特点：
  - 基于分支的简单工作流
  - 通过 Pull Request 进行代码审查
  - 持续部署
- 实践：
  ```bash
  # 创建功能分支
  git checkout -b feature-branch

  # 提交更改
  git commit -am "Add feature"

  # 推送分支
  git push -u origin feature-branch
  ```

### 3. GitLab Flow
- 特点：
  - 环境分支（production, staging）
  - 基于问题跟踪的工作流
  - 版本标签管理
- 实践：
  ```bash
  # 创建环境分支
  git checkout -b production
  git checkout -b staging

  # 合并流程
  git checkout staging
  git merge feature-branch
  git checkout production
  git merge staging
  ```

## 实践练习

### 练习 1：大型项目管理
1. 设置子模块管理
2. 配置 Git LFS
3. 优化仓库性能

### 练习 2：安全实践
1. 配置 GPG 签名
2. 设置分支保护
3. 实施敏感信息管理

### 练习 3：高级工作流
1. 实践 Trunk Based Development
2. 配置 GitHub Flow
3. 实现 GitLab Flow

## 注意事项
1. 定期进行安全审计
2. 监控仓库大小和性能
3. 保持工作流程的一致性
4. 定期更新安全配置
5. 培训团队成员遵循最佳实践
