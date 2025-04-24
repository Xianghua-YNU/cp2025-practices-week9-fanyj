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
    
    # 将当前线段分成三等分，并在中间部分构建等边三角形
    points = []
    for i in range(len(u)-1):
        start = u[i]
        end = u[i+1]
        
        # 计算四个关键点
        p1 = start
        p2 = start + (end - start) / 3
        p3 = p2 + (end - start) / 3 * np.exp(1j * np.pi/3)
        p4 = start + 2 * (end - start) / 3
        p5 = end
        
        # 递归处理每个新线段
        segment = koch_generator(np.array([p1, p2, p3, p4, p5]), level-1)
        points.extend(segment[:-1])
    
    points.append(u[-1])  # 添加最后一个点
    return np.array(points)
        
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
    
    points = []
    for i in range(len(u)-1):
        start = u[i]
        end = u[i+1]
        vec = (end - start) / 4  # 将线段分成四份
        
        # 计算八个关键点形成"香肠"形状
        p1 = start
        p2 = start + vec
        p3 = p2 + vec * (1 + 1j)  # 右上
        p4 = p3 + vec
        p5 = p4 + vec * (1 - 1j)  # 右下
        p6 = p5 + vec
        p7 = p6 + vec * (-1 - 1j) # 左下
        p8 = p7 + vec
        p9 = end
        
        # 递归处理每个新线段
        segment = minkowski_generator(np.array([p1, p2, p3, p4, p5, p6, p7, p8, p9]), level-1)
        points.extend(segment[:-1])
    
    points.append(u[-1])  # 添加最后一个点
    return np.array(points)

if __name__ == "__main__":
    # 初始线段
    init_u = np.array([0 + 0j, 1 + 0j])

    # 绘制不同层级的科赫曲线
    fig, axs = plt.subplots(2, 2, figsize=(10, 10))
    for i in range(4):
        koch_points = koch_generator(init_u, i+1)
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
        minkowski_points = minkowski_generator(init_u, i+1)
        axs[i//2, i%2].plot(
            np.real(minkowski_points), np.imag(minkowski_points), 'k-', lw=1
        )
        axs[i//2, i%2].set_title(f"Minkowski Sausage Level {i+1}")
        axs[i//2, i%2].axis('equal')
        axs[i//2, i%2].axis('off')
    plt.tight_layout()
    plt.show()
