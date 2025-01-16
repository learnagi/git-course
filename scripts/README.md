# 教程同步脚本

这个脚本用于将 Markdown 格式的教程内容同步到教程管理系统。

## 功能特点

- 自动扫描教程目录结构
- 同步教程、章节和小节内容
- 支持元数据和内容文件的读取
- 提供详细的日志记录
- 错误处理和异常报告
- 自动登录和令牌管理

## 目录结构要求

```
git-fun/
├── metadata.json           # 教程元数据
├── chapter1/              # 章节目录
│   ├── metadata.json      # 章节元数据
│   └── section1/          # 小节目录
│       ├── metadata.json  # 小节元数据
│       └── content.md     # 小节内容
└── scripts/               # 脚本目录
    ├── tutorials_admin_sync.py
    ├── requirements.txt
    └── .env
```

## 安装依赖

```bash
cd scripts
pip install -r requirements.txt
```

## 配置

1. 复制环境变量示例文件：
```bash
cp .env.example .env
```

2. 编辑 `.env` 文件，设置以下参数：
- `API_BASE_URL`: API 服务器地址
- `API_EMAIL`: 管理员邮箱
- `API_PASSWORD`: 管理员密码
- `LOG_LEVEL`: 日志级别（INFO/DEBUG/ERROR）

## 使用方法

```bash
cd scripts
python tutorials_admin_sync.py
```

## 日志输出

脚本运行时会输出详细的日志信息，包括：
- 登录状态
- 同步状态
- 错误信息
- 警告信息
- 成功消息

## 注意事项

1. 确保所有必需的文件都存在：
   - 根目录下的 `metadata.json`
   - 每个章节目录下的 `metadata.json`
   - 每个小节目录下的 `metadata.json` 和 `content.md`

2. 文件格式要求：
   - JSON 文件必须是有效的 JSON 格式
   - Markdown 文件必须使用 UTF-8 编码

3. API 访问：
   - 确保 API 服务器可访问
   - 确保登录凭据正确
   - 确保用户具有适当的权限

## 故障排除

如果遇到问题，请检查：
1. 环境变量是否正确配置
2. 网络连接是否正常
3. 文件权限是否正确
4. 日志输出中的错误信息
5. 登录凭据是否有效

## 贡献

欢迎提交 Issue 和 Pull Request 来改进这个脚本。
