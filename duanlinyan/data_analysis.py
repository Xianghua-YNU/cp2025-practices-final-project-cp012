
# 导入必要的库
import numpy as np
import time
from numerical_methods import solve_ftcs, solve_crank_nicolson
from utils import analytical_solution, compute_l2_error
from visualization import plot_convergence

# 收敛性分析 - 分析FTCS和Crank-Nicolson方法的收敛性
def convergence_analysis():
    Nx_list = [20, 40, 80, 160]
    Nt_list = [200, 800, 3200, 12800]  # 保持 r 恒定
    errors_ftcs = []
    errors_cn = []
    times_ftcs = []
    times_cn = []
    dx_list = []
    L = 1.0  # 棒长度
    T = 1.0  # 总时间
    alpha = 0.01  # 热扩散系数

    for Nx, Nt in zip(Nx_list, Nt_list):
        dx = L / (Nx - 1)
        dt = T / Nt
        r = alpha * dt / dx**2
        x = np.linspace(0, L, Nx)
        u_init = np.sin(np.pi * x / L)

        # FTCS
        start_time = time.time()
        u_ftcs = solve_ftcs(u_init, r, Nt, [T], x, L, alpha)
        times_ftcs.append(time.time() - start_time)
        u_ana = analytical_solution(x, T, L, alpha)
        errors_ftcs.append(compute_l2_error(u_ftcs[T], u_ana, dx))  # 直接使用 t = T 的结果

        # Crank-Nicolson
        start_time = time.time()
        u_cn = solve_crank_nicolson(u_init, r, Nt, [T], x, L, alpha)
        times_cn.append(time.time() - start_time)
        errors_cn.append(compute_l2_error(u_cn[T], u_ana, dx))  # 直接使用 t = T 的结果

        dx_list.append(dx)

    # 绘制收敛曲线
    plot_convergence(dx_list, errors_ftcs, errors_cn)

    # 打印误差表格
    print("Δx\t\tΔt\t\tFTCS Error\tCN Error\tFTCS Time\tCN Time")
    for dx, dt, err_ftcs, err_cn, t_ftcs, t_cn in zip(dx_list, [T/Nt for Nt in Nt_list], errors_ftcs, errors_cn, times_ftcs, times_cn):
        print(f"{dx:.4f}\t\t{dt:.4f}\t\t{err_ftcs:.6f}\t{err_cn:.6f}\t{t_ftcs:.4f}\t{t_cn:.4f}")
