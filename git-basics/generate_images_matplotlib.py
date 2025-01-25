import matplotlib.pyplot as plt
import networkx as nx
from pathlib import Path
import matplotlib

# 设置中文字体
matplotlib.rcParams['font.sans-serif'] = ['Arial Unicode MS']
matplotlib.rcParams['axes.unicode_minus'] = False

def create_commit_process():
    plt.figure(figsize=(12, 6))
    G = nx.DiGraph()
    nodes = ['工作区', '暂存区', '本地仓库', '完成提交']
    edges = [
        ('工作区', '暂存区', '修改文件'),
        ('暂存区', '本地仓库', 'git add'),
        ('本地仓库', '完成提交', 'git commit')
    ]
    
    # 添加节点和边
    G.add_nodes_from(nodes)
    G.add_edges_from([(u, v) for u, v, _ in edges])
    
    # 设置布局
    pos = nx.spring_layout(G, k=1, iterations=50)
    
    # 绘制节点
    colors = ['#ff99ff', '#bbbbff', '#bbffbb', '#ffbbbb']
    nx.draw_networkx_nodes(G, pos, node_color=colors, node_size=2000)
    
    # 绘制边和标签
    nx.draw_networkx_edges(G, pos, edge_color='gray', arrows=True, arrowsize=20)
    nx.draw_networkx_labels(G, pos, font_size=10)
    edge_labels = {(u, v): l for u, v, l in edges}
    nx.draw_networkx_edge_labels(G, pos, edge_labels, font_size=8)
    
    plt.title('Git 提交流程')
    plt.axis('off')
    plt.savefig('git-basics/images/git-commit-process.png', dpi=300, bbox_inches='tight')
    plt.close()

def create_workspace_diagram():
    plt.figure(figsize=(10, 8))
    G = nx.DiGraph()
    nodes = ['工作区', '暂存区', '本地仓库', '远程仓库']
    edges = [
        ('工作区', '暂存区', 'git add'),
        ('暂存区', '本地仓库', 'git commit'),
        ('本地仓库', '远程仓库', 'git push'),
        ('远程仓库', '本地仓库', 'git pull'),
        ('本地仓库', '工作区', 'git checkout')
    ]
    
    # 添加节点和边
    G.add_nodes_from(nodes)
    G.add_edges_from([(u, v) for u, v, _ in edges])
    
    # 设置布局
    pos = nx.spring_layout(G)
    
    # 绘制节点
    colors = ['#ff99ff', '#bbbbff', '#bbffbb', '#ffbbbb']
    nx.draw_networkx_nodes(G, pos, node_color=colors, node_size=2000)
    
    # 绘制边和标签
    nx.draw_networkx_edges(G, pos, edge_color='gray', arrows=True, arrowsize=20)
    nx.draw_networkx_labels(G, pos, font_size=10)
    edge_labels = {(u, v): l for u, v, l in edges}
    nx.draw_networkx_edge_labels(G, pos, edge_labels, font_size=8)
    
    plt.title('Git 工作区状态图')
    plt.axis('off')
    plt.savefig('git-basics/images/git-workspace.png', dpi=300, bbox_inches='tight')
    plt.close()

def create_branch_workflow():
    plt.figure(figsize=(12, 6))
    
    # 创建时间线
    commits = ['main', 'develop分支', 'feature分支']
    y_positions = [0, 1, 2]
    
    # 绘制主分支
    plt.plot([0, 5], [0, 0], 'b-', linewidth=2, label='main')
    
    # 绘制develop分支
    plt.plot([1, 3], [1, 1], 'g-', linewidth=2, label='develop')
    plt.plot([1, 1], [0, 1], 'g--')
    plt.plot([3, 3], [1, 0], 'g--')
    
    # 绘制feature分支
    plt.plot([3.5, 4], [2, 2], 'r-', linewidth=2, label='feature')
    plt.plot([3.5, 3.5], [0, 2], 'r--')
    plt.plot([4, 4], [2, 0], 'r--')
    
    # 添加提交点
    plt.plot([0, 1, 2, 3, 3.5, 4, 5], [0, 0, 1, 0, 0, 0, 0], 'ko')
    
    plt.title('Git 分支操作流程图')
    plt.legend()
    plt.grid(True)
    plt.axis('off')
    
    plt.savefig('git-basics/images/git-branch.png', dpi=300, bbox_inches='tight')
    plt.close()

def main():
    # 确保输出目录存在
    output_dir = Path('git-basics/images')
    output_dir.mkdir(exist_ok=True)
    
    # 生成所有图表
    create_commit_process()
    create_workspace_diagram()
    create_branch_workflow()
    print('已使用 Matplotlib 生成所有 Git 教程图表。')

if __name__ == '__main__':
    main()