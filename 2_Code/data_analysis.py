"""
导入初始数据以及对应物理量值的计算
"""
import numpy as np

class IsingModel:
    def __init__(self, size, temperature, J=1.0, H=0.0):
        """
        初始化伊辛模型

        参数:
        - size: 晶格尺寸 (size x size)
        - temperature: 温度
        - J: 交换相互作用常数 (默认为1.0)
        - H: 外磁场 (默认为0.0)
        """
        self.size = size
        self.T = temperature
        self.J = J
        self.H = H

        # 初始化随机自旋配置 (+1或-1)
        self.spins = np.random.choice([-1, 1], size=(size, size))

        # 记录能量和磁化强度
        self.energy = self.calculate_energy()
        self.magnetization = self.calculate_magnetization()

    def calculate_energy(self):
        """计算系统总能量"""
        energy = 0
        for i in range(self.size):
            for j in range(self.size):
                # 最近邻相互作用
                neighbor_sum = self.spins[(i + 1) % self.size, j] + self.spins[(i - 1) % self.size, j] + \
                               self.spins[i, (j + 1) % self.size] + self.spins[i, (j - 1) % self.size]
                energy += -self.J * self.spins[i, j] * neighbor_sum - self.H * self.spins[i, j]
        return energy / 2  # 除以2避免重复计算

    def calculate_magnetization(self):
        """计算系统总磁化强度"""
        return np.sum(self.spins)
    return data # 暂时返回原始数据

# 可以添加更多数据分析函数
