# 大型仓库管理

本节将介绍管理大型 Git 仓库的技巧和方法，帮助你有效处理大规模代码库。

## 仓库分析

### 1. 规模评估

1. 仓库统计
```bash
# 查看仓库大小
du -sh .git

# 统计文件数量
git ls-files | wc -l

# 分析提交历史
git rev-list --count --all
```

2. 性能分析
```bash
# 使用 git-sizer
git-sizer -v

# 分析大文件
git rev-list --objects --all |
  git cat-file --batch-check='%(objecttype) %(objectname) %(objectsize) %(rest)' |
  sort -nr -k3
```

### 2. 问题诊断

1. 存储问题
```bash
# 检查松散对象
git count-objects -v

# 分析包文件
git verify-pack -v .git/objects/pack/*.idx |
  sort -k 3 -n |
  tail -10
```

2. 性能问题
```bash
# 操作计时
GIT_TRACE=1 git status

# 内存使用
git gc --aggressive --prune=now
```

## 存储优化

### 1. 大文件处理

1. Git LFS
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
```

2. 子模块
```bash
# 添加子模块
git submodule add <repository> path/to/submodule

# 更新子模块
git submodule update --init --recursive

# 配置子模块
git config -f .gitmodules submodule.path/to/submodule.shallow true
```

### 2. 历史优化

1. 清理历史
```bash
# 创建新分支
git checkout --orphan temp_branch

# 添加当前文件
git add -A
git commit -m "chore: start fresh history"

# 删除旧分支
git branch -D main
git branch -m main
```

2. 重写历史
```bash
# 使用 BFG
java -jar bfg.jar --strip-blobs-bigger-than 100M repo.git

# 手动重写
git filter-branch --tree-filter 'rm -f path/to/large/file' HEAD
```

## 分布式策略

### 1. 部分克隆

1. 浅克隆
```bash
# 浅克隆最新版本
git clone --depth 1 <repository>

# 获取更多历史
git fetch --unshallow

# 克隆单个分支
git clone --single-branch --branch main <repository>
```

2. 稀疏检出
```bash
# 初始化稀疏检出
git clone --filter=blob:none <repository>
git sparse-checkout init

# 设置检出路径
git sparse-checkout set <directory>

# 禁用稀疏检出
git sparse-checkout disable
```

### 2. 分布式存储

1. 镜像仓库
```bash
# 创建镜像
git clone --mirror <repository>

# 更新镜像
git remote update

# 推送镜像
git push --mirror
```

2. 代理设置
```bash
# 配置 HTTP 代理
git config --global http.proxy http://proxy.example.com:8080

# 配置 SOCKS 代理
git config --global http.proxy socks5://proxy.example.com:1080
```

## 工作流优化

### 1. 分支策略

1. 分支管理
```bash
# 创建开发分支
git checkout -b develop

# 特性分支
git checkout -b feature/new-feature develop

# 发布分支
git checkout -b release/1.0.0 develop
```

2. 合并策略
```bash
# 压缩合并
git merge --squash feature/new-feature

# 变基合并
git rebase -i develop

# 选择性合并
git cherry-pick <commit-hash>
```

### 2. 协作流程

1. 代码评审
```bash
# 创建评审分支
git checkout -b review/feature-name

# 添加评审人
git request-pull main origin review/feature-name
```

2. 持续集成
```yaml
# .github/workflows/ci.yml
name: CI
on:
  push:
    branches: [ main, develop ]
  pull_request:
    branches: [ main, develop ]

jobs:
  build:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v2
        with:
          fetch-depth: 0
```

## 性能调优

### 1. 配置优化

1. 核心配置
```bash
# 配置文件系统缓存
git config --global core.fscache true

# 配置预加载
git config --global core.preloadindex true

# 配置压缩
git config --global core.compression 9
```

2. 网络配置
```bash
# 配置缓冲区
git config --global http.postBuffer 524288000

# 配置并行下载
git config --global submodule.fetchJobs 8

# 配置重试
git config --global http.retryCount 3
```

### 2. 维护策略

1. 定期维护
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
EOF
```

2. 监控告警
```bash
# 创建监控脚本
cat > monitor.sh << 'EOF'
#!/bin/bash

# 检查仓库大小
size=$(du -sh .git | cut -f1)
threshold="10G"

if [ $(numfmt --from=iec $size) -gt $(numfmt --from=iec $threshold) ]; then
    echo "Repository size exceeds threshold"
fi
EOF
```

## 工具支持

### 1. 开发工具

1. IDE 配置
```json
{
  "git.enabled": true,
  "git.autofetch": false,
  "git.confirmSync": false,
  "git.ignoreLimitWarning": true
}
```

2. 性能工具
```bash
# 安装性能工具
npm install -g git-stats
npm install -g git-time-machine

# 使用分析工具
git-stats
git-time-machine
```

### 2. 自动化工具

1. 预提交检查
```bash
# 安装 husky
npm install husky --save-dev

# 配置钩子
npx husky add .husky/pre-commit "npm test"
npx husky add .husky/pre-push "npm run build"
```

2. 自动化脚本
```bash
# 创建自动化脚本
cat > automation.sh << 'EOF'
#!/bin/bash

# 更新代码
git pull

# 清理分支
git branch --merged | grep -v "\*" | xargs -n 1 git branch -d

# 运行测试
npm test
EOF
```

## 最佳实践

### 1. 团队规范

1. 提交规范
```bash
# 配置提交模板
git config --global commit.template .gitmessage

# 使用 commitlint
npm install -g @commitlint/cli @commitlint/config-conventional
```

2. 工作流规范
```markdown
## 分支命名
- feature/*: 新功能
- bugfix/*: 错误修复
- release/*: 版本发布
- hotfix/*: 紧急修复

## 提交信息
- feat: 新功能
- fix: 修复
- docs: 文档
- style: 格式
- refactor: 重构
- test: 测试
- chore: 其他
```

### 2. 性能优化

1. 日常优化
- 定期清理
- 避免大文件
- 使用子模块
- 合理分支

2. 长期维护
- 监控大小
- 优化存储
- 更新工具
- 培训团队

## 学习要点
1. 分析仓库规模
2. 优化存储结构
3. 改进工作流程
4. 实施最佳实践

## 小结
通过本节的学习，你应该掌握了管理大型 Git 仓库的技巧和方法。这些知识将帮助你更好地处理大规模代码库。

## 练习题
1. 分析仓库状态
2. 优化存储结构
3. 实施分布式策略
4. 制定维护计划
