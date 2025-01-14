# 第六章：Git 最佳实践

## 6.1 提交规范

### 提交信息格式

#### Conventional Commits 规范
```
<type>(<scope>): <description>

[optional body]

[optional footer(s)]
```

提交类型（type）：
- `feat`: 新功能
- `fix`: 修复bug
- `docs`: 文档更新
- `style`: 代码格式修改
- `refactor`: 代码重构
- `perf`: 性能优化
- `test`: 测试相关
- `chore`: 构建过程或辅助工具的变动

示例：
```
feat(user): add user registration API

- Add endpoint for user registration
- Implement email verification
- Add unit tests

Closes #123
```

### 原子提交
- 每次提交只做一件事
- 保持提交粒度适中
- 便于代码审查和回滚

好的实践：
```bash
# 添加新功能
git commit -m "feat: add login button to navbar"

# 修复相关bug
git commit -m "fix: correct login button styling"
```

### 提交频率
- 经常性小批量提交
- 确保每次提交后代码可以运行
- 避免积累大量未提交的更改

## 6.2 工作流程

### 团队协作最佳实践

#### 1. 分支命名规范
```
feature/    # 新功能分支
bugfix/     # 修复分支
hotfix/     # 紧急修复分支
release/    # 发布分支
support/    # 支持分支
```

示例：
```bash
git checkout -b feature/user-authentication
git checkout -b bugfix/login-validation
git checkout -b hotfix/security-patch
```

#### 2. 代码审查流程
1. 创建功能分支
2. 开发并测试
3. 提交 Pull Request
4. 代码审查
5. 处理反馈
6. 合并到主分支

#### 3. 持续集成实践
- 提交前本地测试
- 自动化测试
- 代码质量检查
- 自动化部署

### 分支管理策略

#### 1. 主分支保护
```bash
# 禁止直接推送到主分支
git branch --set-upstream-to=origin/main main
git config branch.main.pushRemote no_push
```

#### 2. 分支生命周期管理
- 及时删除已合并分支
- 定期清理过期分支
- 维护分支最新状态

```bash
# 删除已合并的本地分支
git branch --merged | grep -v "\*" | xargs -n 1 git branch -d

# 删除已合并的远程分支
git remote prune origin
```

### 版本发布流程

#### 1. 语义化版本
```
主版本号.次版本号.修订号
```
- 主版本号：不兼容的API修改
- 次版本号：向下兼容的功能性新增
- 修订号：向下兼容的问题修正

#### 2. 发布流程
1. 创建发布分支
```bash
git checkout -b release/1.2.0 develop
```

2. 版本号更新
```bash
# 更新版本文件
vim VERSION
git commit -m "chore: bump version to 1.2.0"
```

3. 测试和修复
```bash
# 修复发布分支中的问题
git commit -m "fix: address release feedback"
```

4. 合并和标签
```bash
git checkout main
git merge release/1.2.0
git tag -a v1.2.0 -m "Release version 1.2.0"
```

## 6.3 项目规范

### 1. 项目结构
```
.
├── .git/
├── .gitignore
├── README.md
├── docs/
├── src/
├── tests/
├── scripts/
└── config/
```

### 2. 文档规范
- README.md 必备内容
  - 项目简介
  - 安装说明
  - 使用示例
  - 贡献指南
  - 许可证信息

### 3. Git配置规范
```bash
# 设置行尾符号
git config --global core.autocrlf input

# 设置默认编辑器
git config --global core.editor vim

# 设置合并工具
git config --global merge.tool vimdiff
```

## 实践练习

### 练习 1：提交规范
1. 使用 Conventional Commits 格式提交
2. 练习编写清晰的提交信息
3. 尝试不同类型的提交

### 练习 2：工作流程
1. 模拟完整的功能开发流程
2. 实践代码审查流程
3. 执行版本发布流程

### 练习 3：项目规范
1. 创建标准的项目结构
2. 编写完整的项目文档
3. 配置Git工作环境

## 注意事项
1. 始终遵循团队约定的规范
2. 保持提交信息的一致性和清晰性
3. 定期回顾和优化工作流程
4. 重视文档的维护和更新
5. 确保配置的一致性
