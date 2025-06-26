"""
主程序入口：用于运行主要的物理模拟。
"""
import numpy as np
# from .numerical_methods import solve_ode
# from .data_analysis import analyze_data
# from .visualization import plot_results

def run_temperature_sweep(size=20, min_T=0.1, max_T=4.0, num_T=20, mc_steps=5000):
    """
    运行温度扫描模拟

    参数:
    - size: 晶格尺寸
    - min_T: 最低温度
    - max_T: 最高温度
    - num_T: 温度点数
    - mc_steps: 每个温度点的蒙特卡洛步数

    返回:
    - temperatures: 温度数组
    - avg_magnetizations: 平均磁化强度数组
    - susceptibilities: 磁化率数组
    - avg_energies: 平均能量数组
    - heat_capacities: 热容数组
    """
    temperatures = np.linspace(min_T, max_T, num_T)
    avg_magnetizations = []
    susceptibilities = []
    avg_energies = []
    heat_capacities = []

    for T in temperatures:
        model = IsingModel(size, T)
        mags, energies = model.simulate(mc_steps)

        # 计算平均磁化强度和磁化率
        avg_mag = np.mean(mags) / (size ** 2)
        avg_magnetizations.append(avg_mag)
        susceptibilities.append((np.mean(mags ** 2) - np.mean(mags) ** 2) / (T * size ** 2))

        # 计算平均能量和热容
        avg_energy = np.mean(energies) / (size ** 2)
        avg_energies.append(avg_energy)
        heat_capacities.append((np.mean(energies ** 2) - np.mean(energies) ** 2) / (T ** 2 * size ** 2))

    return temperatures, avg_magnetizations, susceptibilities, avg_energies, heat_capacities
if __name__ == "__main__":
    size = 20  # 晶格尺寸
    min_T = 0.1  # 最低温度
    max_T = 4.0  # 最高温度
    num_T = 30  # 温度点数
    mc_steps = 10000  # 每个温度点的蒙特卡洛步数

    # 运行温度扫描
    results = run_temperature_sweep(size, min_T, max_T, num_T, mc_steps)

    # 绘制结果
    plot_results(*results)
