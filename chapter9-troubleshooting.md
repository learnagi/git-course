# 第九章：故障排除与调试

## 9.1 常见问题解决

### 冲突处理

#### 1. 合并冲突
```bash
# 查看冲突文件
git status

# 中止合并
git merge --abort

# 使用图形化工具解决冲突
git mergetool
```

常见冲突标记：
```
<<<<<<< HEAD
当前分支的代码
=======
要合并分支的代码
>>>>>>> branch-name
```

#### 2. 复杂冲突处理策略
```bash
# 使用我们的更改
git checkout --ours <file>

# 使用他们的更改
git checkout --theirs <file>

# 查看详细的冲突信息
git log --merge
```

### 丢失提交恢复

#### 1. 使用 reflog 恢复
```bash
# 查看操作历史
git reflog

# 恢复到特定状态
git reset --hard HEAD@{n}

# 恢复删除的分支
git checkout -b recover-branch HEAD@{n}
```

#### 2. 找回已删除的提交
```bash
# 查看所有提交（包括已删除的）
git fsck --full

# 查看悬空的提交
git fsck --lost-found

# 查看提交内容
git show <commit-hash>
```

### 性能问题

#### 1. 仓库优化
```bash
# 压缩仓库
git gc

# 完整的仓库优化
git gc --aggressive

# 清理无用的文件
git prune

# 验证仓库完整性
git fsck
```

#### 2. 网络问题处理
```bash
# 设置 HTTP 缓存
git config --global http.postBuffer 524288000

# 压缩传输数据
git config --global core.compression 9

# 使用浅克隆
git clone --depth 1 <repository>
```

## 9.2 调试技巧

### git bisect：二分查找

#### 1. 基本使用
```bash
# 开始二分查找
git bisect start

# 标记当前版本为有问题的版本
git bisect bad

# 标记已知的好版本
git bisect good <commit-hash>

# 标记当前检出的版本
git bisect good/bad

# 结束查找
git bisect reset
```

#### 2. 自动化二分查找
```bash
# 使用脚本自动化查找
git bisect start HEAD <good-commit>
git bisect run test-script.sh
```

示例测试脚本：
```bash
#!/bin/sh
# test-script.sh
make test
exit $?
```

### git blame：代码追溯

#### 1. 基本使用
```bash
# 查看文件的每一行的最后修改信息
git blame <file>

# 查看特定行的修改
git blame -L 10,20 <file>

# 忽略空白字符的修改
git blame -w <file>
```

#### 2. 高级追溯
```bash
# 显示完整的提交哈希
git blame -l <file>

# 显示原始文件名和行号
git blame -t <file>

# 显示作者邮箱
git blame -e <file>
```

### 日志分析

#### 1. 高级日志查询
```bash
# 查看特定时间段的提交
git log --since="2 weeks ago" --until="yesterday"

# 查看特定作者的提交
git log --author="John Doe"

# 搜索提交消息
git log --grep="fix:"

# 查看文件的修改历史
git log -p <file>
```

#### 2. 统计分析
```bash
# 查看提交统计
git shortlog -sn

# 查看每个作者的代码量统计
git log --author="pattern" --pretty=tformat: --numstat

# 查看文件的修改频率
git log --pretty=format: --name-only | sort | uniq -c | sort -rg
```

## 9.3 预防措施

### 1. 备份策略
```bash
# 创建仓库备份
git bundle create repo.bundle --all

# 从备份中恢复
git clone repo.bundle recovered-repo

# 备份特定分支
git bundle create feature.bundle feature-branch
```

### 2. 预提交检查
```bash
# 配置 pre-commit hook
cat > .git/hooks/pre-commit << 'EOF'
#!/bin/sh
# 运行测试
npm test

# 检查代码风格
eslint .

# 检查是否有调试代码
if grep -r "debugger" src/; then
  echo "Error: Found debugger statement"
  exit 1
fi
EOF
chmod +x .git/hooks/pre-commit
```

### 3. 自动化测试
```bash
# 配置 GitHub Actions
name: CI
on: [push, pull_request]
jobs:
  test:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v2
      - name: Run tests
        run: |
          npm install
          npm test
```

## 实践练习

### 练习 1：冲突处理
1. 创建一个冲突场景
2. 使用不同方法解决冲突
3. 使用 mergetool 解决复杂冲突

### 练习 2：代码调试
1. 使用 git bisect 找出问题提交
2. 使用 git blame 追踪代码变更
3. 分析提交日志找出模式

### 练习 3：性能优化
1. 诊断仓库性能问题
2. 实施优化措施
3. 设置自动化检查

## 注意事项
1. 定期进行仓库维护
2. 建立问题排查流程
3. 保持良好的备份习惯
4. 实施自动化测试
5. 记录常见问题的解决方案
