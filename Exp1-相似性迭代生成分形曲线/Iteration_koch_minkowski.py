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
    if level == 0:
        return u
    else:
        new_points = []
        for i in range(len(u) - 1):
            a = u[i]
            b = u[i + 1]
            d = (b - a) / 3
            p1 = a
            p2 = a + d
            p3 = p2 + d * np.exp(1j * np.pi / 3)
            p4 = b - d
            p5 = b
            new_points.extend([p1, p2, p3, p4])
        new_points.append(u[-1])
        return koch_generator(np.array(new_points), level - 1)


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
    new_points = []
    for i in range(len(u) - 1):
        a = u[i]
        b = u[i + 1]
        d = (b - a) / 4
        p1 = a
        p2 = a + d
        p3 = p2 + 1j * d
        p4 = p3 + d
        p5 = p4 - 1j * d
        p6 = p5 + d
        p7 = b
        new_points.extend([p1, p2, p3, p4, p5, p6])
    new_points.append(u[-1])
    return minkowski_generator(np.array(new_points), level - 1)


if __name__ == "__main__":
    # 初始线段
    init_u = np.array([0, 1])

    # 绘制不同层级的科赫曲线
    fig, axs = plt.subplots(2, 2, figsize=(10, 10))
    for i in range(4):
        # 调用koch_generator生成点
        koch_points = koch_generator(init_u, i + 1)
        axs[i // 2, i % 2].plot(
            np.real(koch_points), np.imag(koch_points), 'k-', lw=1
        )
        axs[i // 2, i % 2].set_title(f"Koch Curve Level {i + 1}")
        axs[i // 2, i % 2].axis('equal')
        axs[i // 2, i % 2].axis('off')
    plt.tight_layout()
    plt.show()

    # 绘制不同层级的闵可夫斯基香肠曲线
    fig, axs = plt.subplots(2, 2, figsize=(10, 10))
    for i in range(4):
        # 调用minkowski_generator生成点
        minkowski_points = minkowski_generator(init_u, i + 1)
        axs[i // 2, i % 2].plot(
            np.real(minkowski_points), np.imag(minkowski_points), 'k-', lw=1
        )
        axs[i // 2, i % 2].set_title(f"Minkowski Sausage Level {i + 1}")
        axs[i // 2, i % 2].axis('equal')
        axs[i // 2, i % 2].axis('off')
    plt.tight_layout()
    plt.show()
    
