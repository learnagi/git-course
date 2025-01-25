import os
from pathlib import Path

def generate_mermaid_commit_process():
    mermaid_code = '''
    graph LR
        A[工作区] -->|修改文件| B[暂存区]
        B -->|git add| C[本地仓库]
        C -->|git commit| D[完成提交]
        style A fill:#f9f,stroke:#333,stroke-width:2px
        style B fill:#bbf,stroke:#333,stroke-width:2px
        style C fill:#bfb,stroke:#333,stroke-width:2px
        style D fill:#fbb,stroke:#333,stroke-width:2px
    '''
    
    # 确保输出目录存在
    output_dir = Path('images')
    output_dir.mkdir(exist_ok=True)
    
    # 保存 Mermaid 代码到文件
    with open('images/git-commit-process.mmd', 'w', encoding='utf-8') as f:
        f.write(mermaid_code)

def generate_mermaid_branch_workflow():
    mermaid_code = '''
    gitGraph
        commit
        branch develop
        checkout develop
        commit
        commit
        checkout main
        merge develop
        commit
        branch feature
        checkout feature
        commit
        checkout main
        merge feature
    '''
    
    with open('images/git-branch.mmd', 'w', encoding='utf-8') as f:
        f.write(mermaid_code)

def generate_mermaid_workspace():
    mermaid_code = '''
    graph TD
        A[工作区] -->|git add| B[暂存区]
        B -->|git commit| C[本地仓库]
        C -->|git push| D[远程仓库]
        D -->|git pull| C
        C -->|git checkout| A
        style A fill:#f9f,stroke:#333,stroke-width:2px
        style B fill:#bbf,stroke:#333,stroke-width:2px
        style C fill:#bfb,stroke:#333,stroke-width:2px
        style D fill:#fbb,stroke:#333,stroke-width:2px
    '''
    
    with open('images/git-workspace.mmd', 'w', encoding='utf-8') as f:
        f.write(mermaid_code)

def main():
    generate_mermaid_commit_process()
    generate_mermaid_branch_workflow()
    generate_mermaid_workspace()
    print('Mermaid 图表代码已生成，请使用 Mermaid Live Editor 或其他支持 Mermaid 的工具来渲染图表。')

if __name__ == '__main__':
    main()