# 导入必要的库
import numpy as np
from numerical_methods import solve_ftcs, solve_crank_nicolson
from utils import analytical_solution
from visualization import plot_temperature_distribution, plot_error_distribution
from data_analysis import convergence_analysis

# 参数设置 - 定义模拟参数
L = 1.0  # 棒长度
T = 1.0  # 总时间
alpha = 0.01  # 热扩散系数

# 主程序 - 运行模拟和分析
def main():
    record_times = [0.1, 0.5, 1.0]
    Nx = 100
    Nt = 1000
    dx = L / (Nx - 1)
    dt = T / Nt
    r = alpha * dt / dx**2
    x = np.linspace(0, L, Nx)
    u_init = np.sin(np.pi * x / L)

    # 求解 - 使用FTCS和Crank-Nicolson方法求解
    ftcs_results = solve_ftcs(u_init, r, Nt, record_times, x, L, alpha)
    cn_results = solve_crank_nicolson(u_init, r, Nt, record_times, x, L, alpha)

    # 绘制温度分布 - 可视化温度分布
    plot_temperature_distribution(x, ftcs_results, cn_results, analytical_solution, L, alpha)

    # 绘制误差分布 - 可视化误差分布
    plot_error_distribution(x, ftcs_results, cn_results, analytical_solution, L, alpha)

    # 进行收敛性分析 - 分析方法的收敛性
    convergence_analysis()

if __name__ == "__main__":
    main()
