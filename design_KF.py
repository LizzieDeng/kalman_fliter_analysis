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
import numpy as np
# ### 水箱实例代码实现


def plot_result(t, y_list, y_label):
    fig = go.Figure(layout=dict(width=600, height=600))
    for y, y_name in zip(y_list, y_label):
        fig.add_trace(go.Scatter(x=t, y=y, mode='markers+lines', name=y_name, marker=dict(size=5)))
    fig.show()


def KF_process_static_model(y_list):
    # ############################## 预测过程初始化
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
    # fig = go.Figure(layout=dict(width=600, height=600))
    # fig.add_trace(go.Scatter(x=t, y=x_state_list, mode='markers+lines', name='Estimated', marker=dict(size=5)))
    # fig.add_trace(go.Scatter(x=t, y=y_list,  mode='markers+lines', name='measured', marker=dict(size=5)))
    # fig.add_trace(go.Scatter(x=t, y=true_list,  mode='markers+lines', name='true value', marker=dict(size=5)))
    # fig.show()
    y_list = [x_state_list, y_list, true_list]
    y_label = ['Estimated', 'measured', 'true value']
    plot_result(t, y_list, y_label)


def KF_process_filling_model(y_list):
    # ############################## 预测过程初始化
    # 初始化状态量和状态方差矩阵
    x_state = np.array([0, 0]).reshape((2, 1))  # 【水位线， 水位上升速率】
    print(x_state.shape)
    P_cov = np.eye(2) * 1000    # 状态量方差矩阵

    Q = np.zeros((2, 2))        # 系统噪声阵
    qf = 0.00001
    Q[0, 0] = qf/3
    Q[0, 1] = qf/2
    Q[1, 0] = qf/2
    Q[1, 1] = qf

    #  # 初始化观测量和观测方差矩阵
    H = np.eye(2)
    r = 0.1
    R = np.zeros((2, 2))
    R[0, 0] = r
    time = [i for i in range(21)]
    # ## record start ####
    x_state_record = np.zeros((len(time), 2))
    # end
    for i in range(1, len(time)):
        dt = time[i] - time[i-1]
        #  预测过程处理
        F_t = np.eye(2)  # 状态量更新矩阵
        F_t[0, 1] = dt
        Q_mat = Q.copy() * dt
        Q_mat[0, 0] = Q_mat[0, 0] * dt * dt
        Q_mat[0, 1] = Q_mat[0, 1] * dt
        Q_mat[1, 0] = Q_mat[1, 0] * dt
        P_cov = F_t.dot(P_cov).dot(F_t.T) + Q_mat
        x_state = F_t.dot(x_state)

        # 更新过程
        H_P_H_T_R = H.dot(P_cov).dot(H.T) + R
        try:
            s_invers = np.linalg.inv(H_P_H_T_R)
        except:
            print('ERROR: Matrix inversion!!  ***************************************************************')
        K = P_cov.dot(H.T).dot(s_invers)
        y = np.array([y_list[i], 0]).reshape((2, 1))
        x_state = x_state + K.dot(y - H.dot(x_state))
        P_cov = P_cov - K.dot(H).dot(P_cov)
        x_state_record[i, :] = x_state.reshape(1, 2)
    t = time
    true_list = [0.1*t for t in time]
    yaxis_list = [x_state_record[:, 0], y_list, true_list]
    y_label = ['Estimated', 'measured', 'true value']
    plot_result(t, yaxis_list, y_label)


if __name__ == "__main__":
    # y_list = [0.9, 0.8, 1.05, 1, 0.95, 1.2, 1.1, 0.23, 1.25, 0.76]  # 观测矩阵
    # true_list = [1 for i in range(len(y_list))]
    # y_list = [0.9, 0.8, 1.1, 1, 0.95, 1.05, 1.2, 0.9, 0.85, 1.15]  # 观测矩阵
    # y_list = [0.11, 0.29, 0.32, 0.5, 0.58, 0.54, 0.58, 0.6,  0.83, 1.1, 0.9, 1.4, 1.45, 1.6, 1.45, 1.5, 1.6, 1.85, 1.9, 2.3]
    # KF_process_static_model(y_list)
    y_list = [0, 0.3, 0.4, 0.25, 0.48, 0.7, 0.65, 0.9, 0.85, 0.8, 0.83, 1.38, 1.2, 1.15, 1.3, 1.7, 1.4, 1.8, 2, 2.1, 1.8]
    KF_process_filling_model(y_list)
