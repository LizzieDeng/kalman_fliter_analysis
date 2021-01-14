# -*- coding: utf-8 -*-
"""
@Time: 2021/1/14 12:28
@Author: LizzieDeng
@File: design_KF.py
@Description:
"""
import matplotlib.pyplot as plt
from plotGraph import plotgraph
import plotly.graph_objects as go

# ### 水箱实例代码实现
# ############################## 预测过程初始化


def KF_process_static_model(y_list):
    # 初始化状态量和状态方差矩阵
    x_state = 0
    Fx = 1
    Fx_T = 1
    p_cov = 1000
    Q = 0.0001 #1 #  0.01  # 0.0001  # 系统噪声 --> 增大系统噪声

    # 初始化观测量和观测方差矩阵
    # y_list         # 观测矩阵
    H = 1  # 观测矩阵（匹配观测量和状态量）
    H_T = 1
    R = 0.1  # 观测量噪音
    x_state_list = []
    true_list = []
    true_value = 0
    for y in y_list:
        # 预测
        x_state = Fx * x_state
        p_cov = Fx * p_cov * Fx_T + Q
        # 更新
        k = p_cov * H_T / (H * p_cov * H_T + R)
        x_state = x_state + k * (y - H * x_state)
        p_cov = (1 - k * H) * p_cov
        true_value = 1 #true_value + 0.1
        true_list.append(true_value)
        # 记录数据
        x_state_list.append(x_state)

    t = list(range(len(y_list)))
    fig = go.Figure(layout=dict(width=600, height=600))
    fig.add_trace(go.Scatter(x=t, y=x_state_list, mode='markers+lines', name='Estimated', marker=dict(size=5)))
    fig.add_trace(go.Scatter(x=t, y=y_list,  mode='markers+lines', name='measured', marker=dict(size=5)))
    fig.add_trace(go.Scatter(x=t, y=true_list,  mode='markers+lines', name='true value', marker=dict(size=5)))
    fig.show()


if __name__ == "__main__":
    # y_list = [0.9, 0.8, 1.05, 1, 0.95, 1.2, 1.1, 0.23, 1.25, 0.76]  # 观测矩阵
    # true_list = [1 for i in range(len(y_list))]
    # y_list = [0.9, 0.8, 1.1, 1, 0.95, 1.05, 1.2, 0.9, 0.85, 1.15]  # 观测矩阵
    y_list = [0.11, 0.29, 0.32, 0.5, 0.58, 0.54, 0.58, 0.6,  0.83, 1.1, 0.9, 1.4, 1.45, 1.6, 1.45, 1.5, 1.6, 1.85, 1.9, 2.3]
    KF_process_static_model(y_list)
