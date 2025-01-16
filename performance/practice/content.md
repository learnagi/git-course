# 性能优化实践

本节提供一系列实践练习，帮助你掌握 Git 性能优化的技巧。

## 基础优化练习

### 练习 1：仓库分析

1. 任务描述
- 分析仓库大小
- 检查文件数量
- 评估性能状况
- 识别潜在问题

2. 实践步骤
```bash
# 克隆测试仓库
git clone <repository>
cd <repository>

# 分析仓库
du -sh .git
git count-objects -v
git rev-list --count --all

# 检查大文件
git rev-list --objects --all |
  git cat-file --batch-check='%(objecttype) %(objectname) %(objectsize) %(rest)' |
  sort -k3nr |
  head -10
```

### 练习 2：配置优化

1. 场景设置
- 优化核心配置
- 设置网络参数
- 配置压缩选项
- 启用缓存功能

2. 解决步骤
```bash
# 配置核心参数
git config --global core.preloadindex true
git config --global core.fscache true
git config --global gc.auto 256

# 网络优化
git config --global http.postBuffer 524288000
git config --global http.maxRequestBuffer 100M
git config --global http.lowSpeedLimit 1000
git config --global http.lowSpeedTime 60

# 压缩设置
git config --global core.compression 9
git config --global pack.windowMemory "100m"
git config --global pack.packSizeLimit "100m"
```

## 存储优化练习

### 练习 1：垃圾回收

1. 基本操作
```bash
# 检查当前状态
git count-objects -v

# 运行垃圾回收
git gc
git gc --aggressive
git gc --prune=now

# 验证结果
git count-objects -v
du -sh .git
```

2. 高级操作
```bash
# 重新打包
git repack -ad
git repack -A -d

# 清理松散对象
git prune
git prune-packed

# 验证完整性
git fsck --full
```

### 练习 2：大文件处理

1. Git LFS 配置
```bash
# 安装 Git LFS
git lfs install

# 配置跟踪
git lfs track "*.zip"
git lfs track "*.psd"
git lfs track "*.iso"

# 提交配置
git add .gitattributes
git commit -m "chore: configure git lfs"

# 迁移大文件
git lfs migrate import --include="*.zip,*.psd,*.iso"
```

2. 子模块管理
```bash
# 添加子模块
git submodule add <repository> external/large-files

# 更新子模块
git submodule update --init --recursive
git submodule update --remote

# 删除子模块
git submodule deinit external/large-files
git rm external/large-files
```

## 分布式优化练习

### 练习 1：克隆优化

1. 浅克隆
```bash
# 浅克隆
git clone --depth 1 <repository>

# 获取更多历史
git fetch --unshallow

# 指定分支克隆
git clone --single-branch --branch main <repository>
```

2. 稀疏检出
```bash
# 初始化稀疏检出
git clone --filter=blob:none <repository>
git sparse-checkout init

# 设置检出路径
git sparse-checkout set src/
git sparse-checkout add docs/

# 列出当前设置
git sparse-checkout list
```

### 练习 2：镜像管理

1. 创建镜像
```bash
# 创建裸仓库
git clone --mirror <repository> repo.git

# 更新镜像
cd repo.git
git remote update

# 推送镜像
git push --mirror <backup-repository>
```

2. 代理配置
```bash
# HTTP 代理
git config --global http.proxy http://proxy.example.com:8080

# SOCKS 代理
git config --global http.proxy socks5://proxy.example.com:1080

# 验证配置
git config --get-regexp http.*
```

## 工作流优化练习

### 练习 1：分支管理

1. 分支清理
```bash
# 列出已合并分支
git branch --merged

# 删除已合并分支
git branch --merged |
  grep -v "\*" |
  grep -v "main" |
  grep -v "develop" |
  xargs -n 1 git branch -d

# 清理远程分支
git remote prune origin
```

2. 分支策略
```bash
# 创建开发分支
git checkout -b develop

# 创建特性分支
git checkout -b feature/new-feature develop

# 合并特性
git checkout develop
git merge --no-ff feature/new-feature
```

### 练习 2：提交优化

1. 提交压缩
```bash
# 查看提交历史
git log --oneline

# 交互式变基
git rebase -i HEAD~5

# 压缩提交
git reset --soft HEAD~3
git commit -m "feat: combined changes"
```

2. 提交规范
```bash
# 创建提交模板
cat > .gitmessage << 'EOF'
type(scope): subject

body

BREAKING CHANGE:
Closes #
EOF

# 配置模板
git config --global commit.template .gitmessage
```

## 监控维护练习

### 练习 1：性能监控

1. 监控脚本
```bash
# 创建监控脚本
cat > monitor.sh << 'EOF'
#!/bin/bash

# 检查仓库大小
size=$(du -sh .git | cut -f1)
echo "Repository size: $size"

# 检查对象数量
git count-objects -v

# 检查大文件
git rev-list --objects --all |
  git cat-file --batch-check='%(objecttype) %(objectname) %(objectsize) %(rest)' |
  sort -k3nr |
  head -5
EOF

chmod +x monitor.sh
```

2. 告警设置
```bash
# 创建告警脚本
cat > alert.sh << 'EOF'
#!/bin/bash

# 设置阈值
SIZE_THRESHOLD="1G"
OBJECTS_THRESHOLD=100000

# 检查大小
size=$(du -sh .git | cut -f1)
if [ $(numfmt --from=iec $size) -gt $(numfmt --from=iec $SIZE_THRESHOLD) ]; then
    echo "WARNING: Repository size exceeds threshold"
fi

# 检查对象数量
objects=$(git count-objects -v | grep count | cut -d: -f2)
if [ $objects -gt $OBJECTS_THRESHOLD ]; then
    echo "WARNING: Too many objects in repository"
fi
EOF

chmod +x alert.sh
```

### 练习 2：自动维护

1. 维护脚本
```bash
# 创建维护脚本
cat > maintenance.sh << 'EOF'
#!/bin/bash

# 垃圾回收
git gc --aggressive --prune=now

# 重新打包
git repack -ad

# 验证对象
git fsck --full

# 清理远程分支
git remote prune origin

# 删除已合并分支
git branch --merged |
  grep -v "\*" |
  grep -v "main" |
  grep -v "develop" |
  xargs -n 1 git branch -d
EOF

chmod +x maintenance.sh
```

2. 定时任务
```bash
# 添加定时任务
crontab -e

# 每周日凌晨 2 点执行维护
0 2 * * 0 /path/to/maintenance.sh

# 每天检查状态
0 9 * * * /path/to/monitor.sh
```

## 工具集成练习

### 练习 1：IDE 配置

1. VS Code 设置
```json
{
  "git.enabled": true,
  "git.autofetch": false,
  "git.confirmSync": false,
  "git.ignoreLimitWarning": true,
  "git.inputValidation": "warn",
  "git.detectSubmodules": false
}
```

2. 性能插件
```bash
# 安装插件
code --install-extension eamodio.gitlens
code --install-extension mhutchie.git-graph

# 配置插件
git config --global diff.tool vscode
git config --global difftool.vscode.cmd 'code --wait --diff $LOCAL $REMOTE'
```

### 练习 2：自动化工具

1. 预提交钩子
```bash
# 安装 husky
npm install husky --save-dev

# 配置钩子
npx husky add .husky/pre-commit "npm test"
npx husky add .husky/pre-push "npm run build"

# 创建检查脚本
cat > .husky/check-size.sh << 'EOF'
#!/bin/bash

# 检查文件大小
git diff --cached --name-only | while read file; do
  if [ -f "$file" ]; then
    size=$(stat -f%z "$file")
    if [ $size -gt 1048576 ]; then
      echo "Error: $file is too large ($(($size/1024/1024))MB)"
      exit 1
    fi
  fi
done
EOF

chmod +x .husky/check-size.sh
```

2. CI/CD 配置
```yaml
# .github/workflows/performance.yml
name: Performance Checks

on:
  push:
    branches: [ main, develop ]
  pull_request:
    branches: [ main, develop ]

jobs:
  check:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v2
        with:
          fetch-depth: 0
      
      - name: Check repository size
        run: |
          size=$(du -sb .git | cut -f1)
          if [ $size -gt 1073741824 ]; then
            echo "Repository size exceeds 1GB"
            exit 1
          fi
      
      - name: Run maintenance
        run: |
          git gc --aggressive --prune=now
          git repack -ad
          git fsck --full
```

## 最佳实践总结

### 1. 日常实践

1. 配置检查
```bash
# 检查全局配置
git config --global -l

# 检查仓库配置
git config -l

# 验证 LFS 配置
git lfs env
```

2. 性能监控
```bash
# 定期检查
./monitor.sh

# 运行维护
./maintenance.sh

# 查看统计
git shortlog -sn
```

### 2. 团队实践

1. 规范制定
```markdown
## Git 性能规范
1. 避免提交大文件
2. 定期清理分支
3. 使用浅克隆
4. 配置自动维护
```

2. 培训计划
```markdown
## 培训内容
1. 性能优化基础
2. 工具使用方法
3. 最佳实践分享
4. 问题诊断处理
```

## 学习要点
1. 掌握优化方法
2. 实践维护技巧
3. 使用监控工具
4. 遵循最佳实践

## 小结
通过这些练习，你应该能够熟练运用 Git 性能优化的各种技巧，并在实际项目中实施有效的优化方案。

## 下一步
1. 深入学习工具
2. 优化工作流程
3. 实施自动化
4. 分享经验心得
