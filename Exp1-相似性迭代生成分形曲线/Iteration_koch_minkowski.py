import numpy as np
import matplotlib.pyplot as plt

def koch_generator(u, level):
    """
    递归/迭代生成科赫曲线的点序列。

    参数:
        u: 初始线段的端点数组（复数表示）
        level: 迭代层数

    返回:
        numpy.ndarray: 生成的所有点（复数数组）
    """
    # TODO: 实现科赫曲线生成算法
    if level == 0:
        return u
    
    # 将线段分成三等分，并在中间插入一个等边三角形的两边
    p1 = u[0]
    p2 = u[-1]
    
    # 计算四个关键点
    a = p1 + (p2 - p1) / 3
    b = p1 + 2 * (p2 - p1) / 3
    c = a + (b - a) * np.exp(1j * np.pi / 3)  # 旋转60度
    
    # 递归处理四个子线段
    left = koch_generator(np.array([p1, a]), level - 1)
    middle_left = koch_generator(np.array([a, c]), level - 1)
    middle_right = koch_generator(np.array([c, b]), level - 1)
    right = koch_generator(np.array([b, p2]), level - 1)
    
    # 合并结果（避免重复点）
    return np.concatenate([left[:-1], middle_left[:-1], middle_right[:-1], right])
        
def minkowski_generator(u, level):
    """
    递归/迭代生成闵可夫斯基香肠曲线的点序列。

    参数:
        u: 初始线段的端点数组（复数表示）
        level: 迭代层数

    返回:
        numpy.ndarray: 生成的所有点（复数数组）
    """
    if level == 0:
        return u
    
    p1 = u[0]
    p2 = u[-1]
    
    # 将线段分成四等分，并在中间插入一个“盒子”
    a = p1 + (p2 - p1) / 4
    b = p1 + 2 * (p2 - p1) / 4
    c = p1 + 3 * (p2 - p1) / 4
    
    # 计算“盒子”的四个顶点
    d = a + (b - a) * 1j  # 向上
    e = b + (b - a) * 1j  # 向上
    
    # 递归处理所有子线段
    left = minkowski_generator(np.array([p1, a]), level - 1)
    middle1 = minkowski_generator(np.array([a, d]), level - 1)
    middle2 = minkowski_generator(np.array([d, e]), level - 1)
    middle3 = minkowski_generator(np.array([e, c]), level - 1)
    right = minkowski_generator(np.array([c, p2]), level - 1)
    
    # 合并结果（避免重复点）
    return np.concatenate([left[:-1], middle1[:-1], middle2[:-1], middle3[:-1], right])


if __name__ == "__main__":
    # 初始线段
    init_u = np.array([0, 1])

    # 绘制不同层级的科赫曲线
    fig, axs = plt.subplots(2, 2, figsize=(10, 10))
    for i in range(4):
        # TODO: 调用koch_generator生成点
        koch_points = None  # 替换为实际生成的点
        axs[i//2, i%2].plot(
            np.real(koch_points), np.imag(koch_points), 'k-', lw=1
        )
        axs[i//2, i%2].set_title(f"Koch Curve Level {i+1}")
        axs[i//2, i%2].axis('equal')
        axs[i//2, i%2].axis('off')
    plt.tight_layout()
    plt.show()

    # 绘制不同层级的闵可夫斯基香肠曲线
    fig, axs = plt.subplots(2, 2, figsize=(10, 10))
    for i in range(4):
        # TODO: 调用minkowski_generator生成点
        minkowski_points = None  # 替换为实际生成的点
        axs[i//2, i%2].plot(
            np.real(minkowski_points), np.imag(minkowski_points), 'k-', lw=1
        )
        axs[i//2, i%2].set_title(f"Minkowski Sausage Level {i+1}")
        axs[i//2, i%2].axis('equal')
        axs[i//2, i%2].axis('off')
    plt.tight_layout()
    plt.show()
