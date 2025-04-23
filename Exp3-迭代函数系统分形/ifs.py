import numpy as np
import matplotlib.pyplot as plt

def get_fern_params():
    """
    返回巴恩斯利蕨的IFS参数
    每个变换包含6个参数(a,b,c,d,e,f)和概率p
    """
    # TODO: 实现巴恩斯利蕨的参数
    return [
        [0.00, 0.00, 0.00, 0.16, 0.00, 0.00, 0.01],  # 茎
        [0.85, 0.04, -0.04, 0.85, 0.00, 1.60, 0.85],  # 小叶子
        [0.20, -0.26, 0.23, 0.22, 0.00, 1.60, 0.07],  # 左叶子
        [-0.15, 0.28, 0.26, 0.24, 0.00, 0.44, 0.07]   # 右叶子
    ]

def get_tree_params():
    """
    返回概率树的IFS参数
    每个变换包含6个参数(a,b,c,d,e,f)和概率p
    """
    # TODO: 实现概率树的参数 
    return [
        [0.05, 0.00, 0.00, 0.60, 0.00, 0.00, 0.05],  # 树干
        [0.05, 0.00, 0.00, 0.50, 0.00, 1.00, 0.15],  # 左分支
        [0.46, -0.32, 0.39, 0.38, 0.00, 0.60, 0.40],  # 左叶子
        [0.47, 0.17, -0.25, 0.42, 0.00, 1.10, 0.40]   # 右叶子
    ]

def apply_transform(point, params):
    """
    应用单个变换到点
    :param point: 当前点坐标(x,y)
    :param params: 变换参数[a,b,c,d,e,f,p]
    :return: 变换后的新坐标(x',y')
    """
    # TODO: 实现变换公式
    x, y = point
    a, b, c, d, e, f, _ = params
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
    # TODO: 实现混沌游戏算法
    # 提取概率并归一化
    probs = [param[-1] for param in ifs_params]
    probs = np.cumsum(probs) / sum(probs)  # 累积概率
    
    points = np.zeros((num_points, 2))
    point = (0, 0)  # 初始点
    
    for i in range(num_points + num_skip):
        # 根据概率随机选择变换
        r = random.random()
        for idx, prob in enumerate(probs):
            if r <= prob:
                point = apply_transform(point, ifs_params[idx])
                break
        
        # 跳过前num_skip个点
        if i >= num_skip:
            points[i - num_skip] = point
    
    return points

def plot_ifs(points, title="IFS Fractal"):
    """
    绘制IFS分形
    :param points: 点坐标数组
    :param title: 图像标题
    """
    # TODO: 实现分形绘制
    plt.figure(figsize=(10, 10))
    plt.scatter(points[:, 0], points[:, 1], s=0.1, c='green', alpha=0.5)
    plt.title(title, fontsize=16)
    plt.axis('equal')
    plt.axis('off')
    plt.show()

if __name__ == "__main__":
    # 生成并绘制巴恩斯利蕨
    fern_params = get_fern_params()
    fern_points = run_ifs(fern_params)
    plot_ifs(fern_points, "Barnsley Fern")
    
    # 生成并绘制概率树
    tree_params = get_tree_params()
    tree_points = run_ifs(tree_params)
    plot_ifs(tree_points, "Probability Tree")
