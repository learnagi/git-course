# 性能优化基础

本节将介绍 Git 性能优化的基本概念和方法，帮助你提高 Git 操作的效率。

## 性能指标

### 1. 关键指标

1. 操作延迟
- 克隆时间
- 提交速度
- 切换分支
- 合并效率

2. 资源消耗
```bash
# 查看仓库大小
du -sh .git

# 查看对象数量
git count-objects -v
```

### 2. 监控工具

1. 内置工具
```bash
# 性能追踪
GIT_TRACE=1 git status

# 操作计时
time git clone <repository>
```

2. 外部工具
```bash
# 使用 git-sizer
git-sizer -v

# 使用 git-stats
git-stats
```

## 配置优化

### 1. 核心配置

1. 基本设置
```bash
# 启用文件系统缓存
git config --global core.fscache true

# 设置压缩级别
git config --global core.compression 9
```

2. 网络优化
```bash
# 启用 HTTP 缓存
git config --global http.postBuffer 524288000

# 配置并行下载
git config --global submodule.fetchJobs 8
```

### 2. 高级配置

1. 垃圾回收
```bash
# 配置自动 GC
git config --global gc.auto 256

# 配置打包限制
git config --global gc.packSizeLimit 100m
```

2. 预加载
```bash
# 启用预读取
git config --global core.preloadindex true

# 配置差异算法
git config --global diff.algorithm histogram
```

## 存储优化

### 1. 对象存储

1. 压缩对象
```bash
# 手动压缩
git gc --aggressive

# 重新打包
git repack -ad
```

2. 清理对象
```bash
# 清理松散对象
git prune

# 清理未引用对象
git gc --prune=now
```

### 2. 仓库优化

1. 仓库瘦身
```bash
# 查找大文件
git rev-list --objects --all |
  git cat-file --batch-check='%(objecttype) %(objectname) %(objectsize) %(rest)' |
  sed -n 's/^blob //p' |
  sort -k2nr |
  head -10

# 删除大文件历史
git filter-branch --force --tree-filter 'rm -f path/to/large/file' HEAD
```

2. 历史优化
```bash
# 压缩提交历史
git rebase -i HEAD~10

# 清理远程分支
git remote prune origin
```

## 工作流优化

### 1. 分支策略

1. 分支管理
```bash
# 删除已合并分支
git branch --merged | grep -v "\*" | xargs -n 1 git branch -d

# 清理远程追踪
git fetch --prune
```

2. 工作区优化
```bash
# 排除文件
cat >> .gitignore << 'EOF'
*.log
node_modules/
build/
EOF

# 配置稀疏检出
git sparse-checkout set <directory>
```

### 2. 提交策略

1. 提交优化
```bash
# 合并提交
git commit --amend

# 压缩提交
git rebase -i HEAD~5
```

2. 标签管理
```bash
# 删除旧标签
git tag -l | xargs git tag -d
git fetch --tags

# 打包标签
git gc --prune=now
```

## 网络优化

### 1. 克隆优化

1. 浅克隆
```bash
# 浅克隆
git clone --depth 1 <repository>

# 单分支克隆
git clone --single-branch --branch main <repository>
```

2. 部分克隆
```bash
# 稀疏检出
git clone --filter=blob:none <repository>

# 按需获取
git fetch origin main:main --depth 1
```

### 2. 同步优化

1. 拉取优化
```bash
# 单分支拉取
git pull origin main --depth 1

# 并行拉取
git -c fetch.parallel=0 pull
```

2. 推送优化
```bash
# 压缩推送
git push --thin

# 强制推送
git push --force-with-lease
```

## 工具优化

### 1. IDE 集成

1. VS Code 设置
```json
{
  "git.enabled": true,
  "git.autofetch": true,
  "git.confirmSync": false,
  "git.enableSmartCommit": true
}
```

2. 性能设置
```json
{
  "git.ignoreLimitWarning": true,
  "git.ignoreLegacyWarning": true,
  "git.autorefresh": false
}
```

### 2. 辅助工具

1. Git LFS
```bash
# 安装 Git LFS
git lfs install

# 追踪大文件
git lfs track "*.psd"
```

2. 预提交钩子
```bash
# 安装 husky
npm install husky --save-dev

# 配置钩子
npx husky add .husky/pre-commit "npm test"
```

## 监控和维护

### 1. 性能监控

1. 日志分析
```bash
# 查看操作日志
git reflog

# 分析提交历史
git log --stat
```

2. 资源监控
```bash
# 查看磁盘使用
git count-objects -vH

# 检查包文件
git verify-pack -v .git/objects/pack/*.idx
```

### 2. 定期维护

1. 自动维护
```bash
# 创建维护脚本
cat > git-maintenance.sh << 'EOF'
#!/bin/bash
git gc --aggressive
git prune
git repack -ad
EOF
chmod +x git-maintenance.sh
```

2. 计划任务
```bash
# 添加定时任务
crontab -e
# 每周日凌晨 2 点执行维护
0 2 * * 0 /path/to/git-maintenance.sh
```

## 最佳实践

### 1. 日常优化

1. 工作习惯
- 定期提交
- 及时清理
- 避免大文件
- 使用 .gitignore

2. 团队协作
- 统一配置
- 共享规范
- 定期维护
- 性能监控

### 2. 性能调优

1. 配置优化
```bash
# 性能配置模板
git config --global core.preloadindex true
git config --global core.fscache true
git config --global gc.auto 256
```

2. 维护计划
```bash
# 每月维护清单
1. 运行垃圾回收
2. 检查大文件
3. 清理远程分支
4. 优化本地存储
```

## 学习要点
1. 了解性能指标
2. 掌握优化方法
3. 建立维护计划
4. 实施最佳实践

## 小结
通过本节的学习，你应该了解了 Git 性能优化的基本概念和方法。这些知识将帮助你提高 Git 操作的效率。

## 练习题
1. 分析仓库性能
2. 优化配置参数
3. 实施存储优化
4. 建立维护计划
