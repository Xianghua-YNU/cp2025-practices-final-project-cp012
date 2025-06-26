"""
可视化函数模块：用于绘制模拟结果和分析数据。
"""
import matplotlib.pyplot as plt
import numpy as np

def plot_results(temperatures, avg_magnetizations, susceptibilities, avg_energies, heat_capacities):
    """绘制结果"""
    plt.figure(figsize=(14, 10))
    # 磁化强度
    plt.subplot(2, 2, 1)
    plt.plot(temperatures, np.abs(avg_magnetizations), 'o-')
    plt.xlabel("Temperature")
    plt.ylabel("Average Magnetization per spin")
    plt.title("Magnetization vs Temperature")
    # 磁化率
    plt.subplot(2, 2, 2)
    plt.plot(temperatures, susceptibilities, 'o-')
    plt.xlabel("Temperature")
    plt.ylabel("Magnetic Susceptibility")
    plt.title("Susceptibility vs Temperature")
    # 能量
    plt.subplot(2, 2, 3)
    plt.plot(temperatures, avg_energies, 'o-')
    plt.xlabel("Temperature")
    plt.ylabel("Average Energy per spin")
    plt.title("Energy vs Temperature")
    # 热容
    plt.subplot(2, 2, 4)
    plt.plot(temperatures, heat_capacities, 'o-')
    plt.xlabel("Temperature")
    plt.ylabel("Heat Capacity")
    plt.title("Heat Capacity vs Temperature")
    plt.tight_layout()
    plt.show()

# 可以添加更多绘图函数，如散点图、三维图等
