# Git 图表生成说明

本目录包含了使用 Mermaid.js 生成的 Git 流程图代码。要将这些 .mmd 文件渲染成图片，您可以：

1. 使用 Mermaid Live Editor：
   - 访问 https://mermaid.live
   - 将 .mmd 文件中的代码复制到编辑器中
   - 下载生成的 SVG 或 PNG 图片

2. 使用命令行工具：
   ```bash
   # 安装 @mermaid-js/mermaid-cli
   npm install -g @mermaid-js/mermaid-cli
   
   # 转换 .mmd 文件为图片
   mmdc -i input.mmd -o output.png
   ```

3. 使用 VS Code：
   - 安装 "Markdown Preview Mermaid Support" 插件
   - 在 Markdown 文件中使用 ```mermaid 代码块
   - 预览或导出图片

## 图表说明

- git-commit-process.mmd: Git 提交流程图
- git-branch.mmd: Git 分支操作流程图
- git-workspace.mmd: Git 工作区状态图