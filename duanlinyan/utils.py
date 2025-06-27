# 导入必要的库
import numpy as np

# 解析解 - 计算热方程的解析解
def analytical_solution(x, t, L, alpha):
    return np.sin(np.pi * x / L) * np.exp(-np.pi**2 * alpha * t / L**2)

# 计算 L2 范数误差 - 计算数值解与解析解之间的L2误差
def compute_l2_error(u_num, u_ana, dx):
    return np.sqrt(np.sum((u_num - u_ana)**2) * dx)
