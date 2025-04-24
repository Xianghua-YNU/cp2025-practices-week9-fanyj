import numpy as np
import matplotlib.pyplot as plt
import random

def get_fern_params():
    """
    返回巴恩斯利蕨的IFS参数
    每个变换包含6个参数(a,b,c,d,e,f)和概率p
    """
    return [
        [0.00, 0.00, 0.00, 0.16, 0.00, 0.00, 0.01],  # Stem
        [0.85, 0.04, -0.04, 0.85, 0.00, 1.60, 0.85],  # Successively smaller leaflets
        [0.20, -0.26, 0.23, 0.22, 0.00, 1.60, 0.07],  # Largest left leaflet
        [-0.15, 0.28, 0.26, 0.24, 0.00, 0.44, 0.07]   # Largest right leaflet
    ]

def get_tree_params():
    """
    返回概率树的IFS参数
    每个变换包含6个参数(a,b,c,d,e,f)和概率p
    修改为只返回3个变换以满足测试要求
    """
    return [
        [0.05, 0.00, 0.00, 0.60, 0.00, 0.00, 0.25],  # Trunk
        [0.42, -0.42, 0.42, 0.42, 0.00, 0.40, 0.40],  # Left branch
        [0.42, 0.42, -0.42, 0.42, 0.00, 0.40, 0.35]   # Right branch
    ]

def apply_transform(point, params):
    """
    应用单个变换到点
    :param point: 当前点坐标(x,y)
    :param params: 变换参数[a,b,c,d,e,f,p]
    :return: 变换后的新坐标(x',y')
    """
    a, b, c, d, e, f, _ = params
    x, y = point
    x_new = a * x + b * y + e
    y_new = c * x + d * y + f
    return (x_new, y_new)

def run_ifs(ifs_params, num_points=100000, num_skip=100):
    """
    运行IFS迭代生成点集
    :param ifs_params: IFS参数列表
    :param num_points: 总点数
    :param num_skip: 跳过前n个点
    :return: 生成的点坐标数组
    """
    # 提取概率并归一化
    probs = [param[6] for param in ifs_params]
    probs = np.cumsum(probs) / np.sum(probs)
    
    points = []
    point = (0, 0)  # 初始点
    
    for i in range(num_points + num_skip):
        # 根据概率选择变换
        r = random.random()
        for idx, prob in enumerate(probs):
            if r <= prob:
                point = apply_transform(point, ifs_params[idx])
                break
        
        # 跳过前num_skip个点
        if i >= num_skip:
            points.append(point)
    
    return np.array(points)

def plot_ifs(points, title="IFS Fractal", color='green', figsize=(8, 10)):
    """
    绘制IFS分形
    :param points: 点坐标数组
    :param title: 图像标题
    :param color: 分形颜色
    :param figsize: 图像大小
    """
    plt.figure(figsize=figsize)
    plt.scatter(points[:, 0], points[:, 1], s=0.1, c=color, marker='.')
    plt.title(title)
    plt.axis('equal')
    plt.axis('off')
    plt.show()

if __name__ == "__main__":
    # 生成并绘制巴恩斯利蕨
    fern_params = get_fern_params()
    fern_points = run_ifs(fern_params, num_points=100000)
    plot_ifs(fern_points, "Barnsley Fern", color='darkgreen')
    
    # 生成并绘制概率树
    tree_params = get_tree_params()
    tree_points = run_ifs(tree_params, num_points=100000)
    plot_ifs(tree_points, "Probability Tree", color='saddlebrown', figsize=(8, 8))
