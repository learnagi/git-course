import os
import matplotlib.pyplot as plt
import networkx as nx
from PIL import Image, ImageDraw, ImageFont

def ensure_dir(directory):
    if not os.path.exists(directory):
        os.makedirs(directory)

def create_workspace_diagram():
    img = Image.new('RGB', (1600, 1200), 'white')
    draw = ImageDraw.Draw(img)
    
    # 绘制三个主要区域
    boxes = [
        ((200, 200, 600, 800), '工作区\nWorking Directory'),
        ((700, 200, 1100, 800), '暂存区\nStaging Area'),
        ((1200, 200, 1400, 800), '版本库\nRepository')
    ]
    
    for box, label in boxes:
        draw.rectangle(box, outline='#2E86C1', width=4)
        # 在框中添加文字
        draw.text((box[0] + 40, box[1] + 40), label, fill='#2E86C1', font=ImageFont.load_default())
    
    # 添加箭头
    draw.line([(600, 500), (700, 500)], fill='#27AE60', width=4)
    draw.line([(1100, 500), (1200, 500)], fill='#27AE60', width=4)
    
    img.save('git-basics/images/git-workspace.png', quality=95)

def create_workflow_diagram():
    G = nx.DiGraph()
    G.add_edges_from([
        ('修改文件', '暂存更改'),
        ('暂存更改', '提交更改'),
        ('提交更改', '推送到远程')
    ])
    
    plt.figure(figsize=(20, 12), dpi=300)
    pos = nx.spring_layout(G)
    nx.draw(G, pos, with_labels=True, node_color='#AED6F1',
            node_size=6000, font_size=16, font_weight='bold',
            arrows=True, edge_color='#2E86C1', width=2)
    
    plt.savefig('git-basics/images/git-workflow.png', bbox_inches='tight')
    plt.close()

def create_commit_process_diagram():
    img = Image.new('RGB', (1600, 800), 'white')
    draw = ImageDraw.Draw(img)
    
    # 绘制提交过程
    stages = [
        (200, 400, '修改文件'),
        (600, 400, 'git add'),
        (1000, 400, 'git commit'),
        (1400, 400, '完成提交')
    ]
    
    for i in range(len(stages)-1):
        x1, y, label1 = stages[i]
        x2, _, _ = stages[i+1]
        draw.line([(x1, y), (x2, y)], fill='#2E86C1', width=4)
        draw.text((x1-60, y-60), label1, fill='#2E86C1', font=ImageFont.load_default())
    
    draw.text((stages[-1][0]-60, stages[-1][1]-60), stages[-1][2], fill='#2E86C1', font=ImageFont.load_default())
    
    img.save('git-basics/images/git-commit-process.png', quality=95)

def create_branch_diagram():
    G = nx.DiGraph()
    commits = ['main', 'feature1', 'feature2']
    edges = [('main', 'feature1'), ('main', 'feature2')]
    G.add_edges_from(edges)
    
    plt.figure(figsize=(20, 12), dpi=300)
    pos = nx.spring_layout(G)
    nx.draw(G, pos, with_labels=True, node_color='#AED6F1',
            node_size=4000, font_size=16, font_weight='bold',
            edge_color='#2E86C1', width=2)
    
    plt.savefig('git-basics/images/git-branch.png', bbox_inches='tight')
    plt.close()

def main():
    # 确保目录存在
    ensure_dir('git-basics/images')
    
    # 生成高清图片
    create_workspace_diagram()
    create_workflow_diagram()
    create_commit_process_diagram()
    create_branch_diagram()

if __name__ == '__main__':
    main()