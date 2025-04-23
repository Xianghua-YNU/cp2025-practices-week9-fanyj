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
    else:
        a = u[0]
        b = u[1]
        v = (b - a) / 3
        points = [
            a,
            a + v,
            a + v + v * (np.cos(np.pi / 3) + 1j * np.sin(np.pi / 3)),
            a + 2 * v,
            b
        ]
        result = []
        for i in range(len(points) - 1):
            sub_points = koch_generator(np.array([points[i], points[i + 1]]), level - 1)
            if i > 0:
                sub_points = sub_points[1:]
            result.extend(sub_points)
        return np.array(result)
        
def minkowski_generator(u, level):
    """
    递归/迭代生成闵可夫斯基香肠曲线的点序列。

    参数:
        u: 初始线段的端点数组（复数表示）
        level: 迭代层数

    返回:
        numpy.ndarray: 生成的所有点（复数数组）
    """
    # TODO: 实现闵可夫斯基香肠曲线生成算法
    if level == 0:
        return u
    else:
        a = u[0]
        b = u[1]
        v = (b - a) / 4
        points = [
            a,
            a + v,
            a + v + 1j * v,
            a + 2 * v + 1j * v,
            a + 2 * v,
            a + 3 * v,
            b
        ]
        result = []
        for i in range(len(points) - 1):
            sub_points = minkowski_generator(np.array([points[i], points[i + 1]]), level - 1)
            if i > 0:
                sub_points = sub_points[1:]
            result.extend(sub_points)
        return np.array(result)

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
