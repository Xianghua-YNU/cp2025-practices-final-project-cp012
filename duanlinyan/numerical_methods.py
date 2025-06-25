# 导入必要的库
import numpy as np
from scipy import linalg

# FTCS 方案 - 实现前向时间中心空间差分方法
def solve_ftcs(u, r, Nt, record_times, x, L, alpha):
    dt = T / Nt  # 定义时间步长
    u_ftcs = u.copy()
    results = {}
    for n in range(Nt):
        t = (n + 1) * dt
        u_new = u_ftcs[1:-1] + r * (u_ftcs[2:] - 2 * u_ftcs[1:-1] + u_ftcs[:-2])
        u_ftcs[1:-1] = u_new
        u_ftcs[0] = u_ftcs[-1] = 0  # 边界条件
        if any(abs(t - rt) <= dt for rt in record_times):  # 放宽匹配条件
            results[t] = u_ftcs.copy()
    # 强制记录 t = T
    if T not in results:
        results[T] = u_ftcs.copy()
    return results

# Crank-Nicolson 方案 - 实现Crank-Nicolson隐式差分方法
def solve_crank_nicolson(u, r, Nt, record_times, x, L, alpha):
    dt = T / Nt  # 定义时间步长
    u_cn = u.copy()
    N = len(u) - 2  # 内部点数
    A = np.zeros((N, N))  # 三对角矩阵
    for i in range(N):
        A[i, i] = 1 + r  # 主对角线
        if i > 0:
            A[i, i-1] = -r / 2  # 下对角线
        if i < N-1:
            A[i, i+1] = -r / 2  # 上对角线
    results = {}
    for n in range(Nt):
        t = (n + 1) * dt
        b = u_cn[1:-1] + (r / 2) * (u_cn[2:] - 2 * u_cn[1:-1] + u_cn[:-2])
        b[0] += r / 2 * u_cn[0]  # 边界条件调整
        b[-1] += r / 2 * u_cn[-1]
        u_cn[1:-1] = linalg.solve(A, b)
        u_cn[0] = u_cn[-1] = 0
        if any(abs(t - rt) <= dt for rt in record_times):  # 放宽匹配条件
            results[t] = u_cn.copy()
    # 强制记录 t = T
    if T not in results:
        results[T] = u_cn.copy()
    return results
