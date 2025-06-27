# 导入必要的库
import matplotlib.pyplot as plt

# 绘制温度分布 - 在不同时间点绘制温度分布图
def plot_temperature_distribution(x, ftcs_results, cn_results, analytical_solution, L, alpha):
    plt.figure(figsize=(12, 8))
    for t in sorted(ftcs_results.keys()):
        u_ana = analytical_solution(x, t, L, alpha)
        plt.plot(x, ftcs_results[t], label=f'FTCS t={t:.1f}')
        plt.plot(x, cn_results[t], '--', label=f'Crank-Nicolson t={t:.1f}')
        plt.plot(x, u_ana, 'k:', label=f'Analytical Solution t={t:.1f}')
    plt.title('Temperature Distribution at Different Times')
    plt.xlabel('x')
    plt.ylabel('Temperature')
    plt.legend()
    plt.show()

# 绘制误差分布 - 在不同时间点绘制误差分布图
def plot_error_distribution(x, ftcs_results, cn_results, analytical_solution, L, alpha):
    plt.figure(figsize=(12, 8))
    for t in sorted(ftcs_results.keys()):
        u_ana = analytical_solution(x, t, L, alpha)
        plt.plot(x, ftcs_results[t] - u_ana, label=f'FTCS Error t={t:.1f}')
        plt.plot(x, cn_results[t] - u_ana, '--', label=f'Crank-Nicolson Error t={t:.1f}')
    plt.title('Error Distribution at Different Times')
    plt.xlabel('x')
    plt.ylabel('Error')
    plt.legend()
    plt.show()

# 绘制收敛曲线 - 绘制收敛性分析的对数图
def plot_convergence(dx_list, errors_ftcs, errors_cn):
    plt.figure()
    plt.loglog(dx_list, errors_ftcs, 'o-', label='FTCS')
    plt.loglog(dx_list, errors_cn, 's-', label='Crank-Nicolson')
    plt.xlabel('Δx')
    plt.ylabel('L2 Error')
    plt.title('Convergence Analysis')
    plt.legend()
    plt.grid(True, which="both", ls="--")
    plt.show()
