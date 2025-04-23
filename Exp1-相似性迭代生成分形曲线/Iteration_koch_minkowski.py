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
    
    # 将每条线段转换为4个线段
    new_u = []
    for i in range(len(u)-1):
        start = u[i]
        end = u[i+1]
        
        # 计算四个分割点
        segment = end - start
        p1 = start
        p2 = start + segment / 3
        p4 = start + 2 * segment / 3
        p5 = end
        
        # 计算三角形顶点
        angle = np.pi / 3  # 60度
        rotation = np.exp(1j * angle)
        p3 = p2 + (p4 - p2) * rotation
        
        # 添加新点
        new_u.extend([p1, p2, p3, p4])
    
    new_u.append(u[-1])  # 添加最后一个点
    
    return koch_generator(np.array(new_u), level-1)
        
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
    
    # 将每条线段转换为8个线段
    new_u = []
    for i in range(len(u)-1):
        start = u[i]
        end = u[i+1]
        segment = end - start
        
        # 计算所有分割点
        p1 = start
        p2 = start + segment / 4
        p3 = p2 + segment / 4 * 1j  # 向上
        p4 = p3 + segment / 4
        p5 = p4 - segment / 4 * 1j  # 向下
        p6 = p5 - segment / 4 * 1j  # 继续向下
        p7 = p6 + segment / 4
        p8 = p7 + segment / 4 * 1j  # 向上
        
        # 添加新点
        new_u.extend([p1, p2, p3, p4, p5, p6, p7, p8])
    
    new_u.append(u[-1])  # 添加最后一个点
    
    return minkowski_generator(np.array(new_u), level-1)

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
