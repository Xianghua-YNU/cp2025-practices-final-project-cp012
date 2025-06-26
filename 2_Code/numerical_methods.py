"""
核心数值算法模块：包含各种数值方法实现。
"""
import numpy as np

def metropolis_step(self):
    """执行一次Metropolis蒙特卡洛步"""
    # 随机选择一个自旋
    i, j = np.random.randint(0, self.size, 2)
    # 计算翻转前后的能量变化
    neighbor_sum = self.spins[(i + 1) % self.size, j] + self.spins[(i - 1) % self.size, j] + \
                    self.spins[i, (j + 1) % self.size] + self.spins[i, (j - 1) % self.size]
    delta_E = 2 * self.J * self.spins[i, j] * neighbor_sum + 2 * self.H * self.spins[i, j]
    # 判断是否接受翻转
    if delta_E < 0 or np.random.rand() < np.exp(-delta_E / self.T):
        self.spins[i, j] *= -1
        self.energy += delta_E
        self.magnetization += 2 * self.spins[i, j]
    return solution

# 可以添加更多数值方法，如积分、求根、矩阵运算等
