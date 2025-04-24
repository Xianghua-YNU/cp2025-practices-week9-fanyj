import numpy as np
import matplotlib.pyplot as plt


def get_fern_params():
    """
    返回巴恩斯利蕨的IFS参数
    每个变换包含6个参数(a,b,c,d,e,f)和概率p
    """
    fern_params = [
        # 第一个变换
        [0, 0, 0, 0.16, 0, 0, 0.01],
        # 第二个变换
        [0.85, 0.04, -0.04, 0.85, 0, 1.6, 0.85],
        # 第三个变换
        [0.2, -0.26, 0.23, 0.22, 0, 1.6, 0.07],
        # 第四个变换
        [-0.15, 0.28, 0.26, 0.24, 0, 0.44, 0.07]
    ]
    return fern_params


def get_tree_params():
    """
    返回概率树的IFS参数
    每个变换包含6个参数(a,b,c,d,e,f)和概率p
    """
    tree_params = [
        # 第一个变换
        [0, 0, 0, 0.5, 0, 0, 0.1],
        # 第二个变换
        [0.42, -0.42, 0.42, 0.42, 0, 1, 0.3],
        # 第三个变换
        [0.42, 0.42, -0.42, 0.42, 0, 1, 0.3],
        # 第四个变换
        [0.1, 0, 0, 0.1, 0, 1, 0.3]
    ]
    return tree_params


def apply_transform(point, params):
    """
    应用单个变换到点
    :param point: 当前点坐标(x,y)
    :param params: 变换参数[a,b,c,d,e,f,p]
    :return: 变换后的新坐标(x',y')
    """
    a, b, c, d, e, f, _ = params
    x, y = point
    new_x = a * x + b * y + e
    new_y = c * x + d * y + f
    return (new_x, new_y)


def run_ifs(ifs_params, num_points=100000, num_skip=100):
    """
    运行IFS迭代生成点集
    :param ifs_params: IFS参数列表
    :param num_points: 总点数
    :param num_skip: 跳过前n个点
    :return: 生成的点坐标数组
    """
    points = []
    current_point = (0, 0)
    probabilities = [param[-1] for param in ifs_params]
    for _ in range(num_points + num_skip):
        # 根据概率选择一个变换
        selected_transform = np.random.choice(len(ifs_params), p=probabilities)
        current_point = apply_transform(current_point, ifs_params[selected_transform])
        if _ >= num_skip:
            points.append(current_point)
    return np.array(points)


def plot_ifs(points, title="IFS Fractal"):
    """
    绘制IFS分形
    :param points: 点坐标数组
    :param title: 图像标题
    """
    x_coords = points[:, 0]
    y_coords = points[:, 1]
    plt.figure()
    plt.scatter(x_coords, y_coords, s=0.1, color='green')
    plt.title(title)
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
    
