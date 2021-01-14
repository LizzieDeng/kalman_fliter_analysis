# this is for matplotlib
import matplotlib.pyplot as plt
import matplotlib as mpl
import numpy as np
from plotly.subplots import make_subplots
import plotly.graph_objects as go

mpl.rcParams['font.sans-serif'] = ['SimHei']  # 设置简黑字体
mpl.rcParams['axes.unicode_minus'] = False  # 解决‘-’bug
R2D = 180.0 / np.pi


def subplot_graph(title, col_row_list, label, time, data_list):
    """
    相同采样时间，不同类型的信号对比，根据接受的数据将其用matplotlib渲染画图
    :param title: 画图的标题
    :param col_row_list: 需要生成的子图数量
    :param label: 生成的线的名称
    :param data_list: 生成地图的数据
    :return:
    """
    if len(label) == len(data_list):
        col = col_row_list[0]
        row = col_row_list[1]
        a = col * row
        if len(data_list) % a == 0:
            y_count = len(data_list) / a
            plt.figure()
            plt.suptitle(title, size=16)
            for i in range(a):
                index = i + 1
                plt.subplot(col, row, index)
                for j in range(int(y_count)):
                    p = j + i * int(y_count)
                    # plt.plot(time, data_list[p],  label=label[p])
                    plt.scatter(time, data_list[p], s=1, label=label[p])
                    plt.legend()
            plt.show()
        else:
            print("data not match the subplot{}".format(title))
    else:
        print("the label not match the data{}, {}".format(len(label), len(data_list)))


def grid_lines(lon, lat, step1, step2, rang):
    """
    将接受的数据用matplotlib渲染画图成网格图
    :param lon: 经度
    :param lat: 纬度
    :param step: 网格线等距离间隔长度
    :return:
    """
    tickle_x = np.arange(np.min(lon), np.max(lon), step1)  # 经度
    tickle_y = np.arange(np.min(lat), np.max(lat), step2)  # 纬度
    x_label = []
    y_label = []
    for i in range(len(tickle_x)):
        if i % rang == 0:
            x_label.append(tickle_x[i])
        else:
            x_label.append(" ")
    for i in range(len(tickle_y)):
        if i % rang == 0:
            y_label.append(tickle_y[i])
        else:
            y_label.append(" ")
    plt.figure()
    plt.title('川沙精工园地库5圈测试', fontsize=20)
    plt.scatter(lon, lat, s=1, c='green',
                label='车辆运动学模型演算')
    plt.xticks(tickle_x, x_label, rotation=45)
    plt.yticks(tickle_y, y_label)
    plt.tick_params(direction='in', labelsize='small')
    plt.legend()
    plt.grid(True)
    plt.show()


def plot_3d_graph(lon_list, lat_list, height_list, title, label_list):
    """
    将接受的数据用matplotlib渲染成3d图形展示
    :param lon_list: 经度列表 [gps, algorithm] 可以只传一个
    :param lat_list: 纬度列表 [gps, algorithm]
    :param height_list: 高度列表 [gps, algorithm]
    :param title: 图像标题
    :param label_list: 每个图形的名称
    :return:
    """
    plt.figure()
    ax = plt.axes(projection='3d')
    for index in range(len(lon_list)):
        ax.plot(lon_list[index], lat_list[index], height_list[index], label=label_list[index])
    ax.set_title(title)
    ax.legend()
    plt.show()


def x_axis_y_axis_plot_graph(x_list, y_list, title, label_list, step1, step2, rg ):
    """
    x轴和y轴都是可变的，通过matplotlib渲染，比较两张图数据的变化误差
    :param x_list: x轴坐标的数据
    :param y_list: y轴坐标的数据
    :param title: 图像标题
    :param label_list: 每条数据名称
    :return:
    """
    markerlist = [None, None, None, '*']
    size_list = [2, 2, 2, 5]
    if len(x_list) == len(y_list) == len(label_list):
        plt.figure()
        plt.title(title, fontsize=20)
        tickle_x = np.arange(np.min(x_list[0]), np.max(x_list[0]), step1)  # 经度
        tickle_y = np.arange(np.min(y_list[0]), np.max(y_list[0]), step2)  # 纬度
        x_label = []
        y_label = []
        for i in range(len(tickle_x)):
            if i % rg == 0:
                x_label.append(tickle_x[i])
            else:
                x_label.append(" ")
        for i in range(len(tickle_y)):
            if i % rg == 0:
                y_label.append(tickle_y[i])
            else:
                y_label.append(" ")
        plt.xticks(tickle_x, x_label, rotation=45)
        plt.yticks(tickle_y, y_label)
        plt.tick_params(direction='in', labelsize='small')  # labelcolor='r',
        for index in range(len(x_list)):
            plt.scatter(x_list[index], y_list[index], s=size_list[index], label=label_list[index], marker=markerlist[index])
        plt.grid(True)
        plt.legend()
        plt.axis('equal')
        plt.show()


# ############################################################################
#  this is for plotly graph plot
# ############################################################################
def show_grid_plot(x_list, y_list, name_list, mode='markers', gest_file=None, color_list=None, col_row_list=None, title=None, subplot_title=None):
    """
    subplot图
    利用plotly画图
    :param gest_file:
    :param x_list: x轴需要的数据   类型：[[a, b, c], [], []]  每个子列表的数据渲染同一张图
    :param y_list: y轴需要数据   类型：[[a, b, c], [], []]  每个子列表的数据渲染同一张图
    :param name_list: 每条数据的label  类型：[[a, b, c], [], []]
    :param mode: 需要画出什么风格的数据 默认是 markers 点
    :param color_list: 默认是系统自动匹配  每条数据想要渲染的颜色 类型：[[a, b, c], [], []]
    :param col_row_list: 需要画子图时传参  类型如 [4, 5]
    :param title: 渲染的每张图的标题
    :param subplot_title: 渲染子图时，给所有子图的一个大标题
    :return:
    """
    # 判断是否是画子图
    if col_row_list:
        # 画子图
        rows = col_row_list[0]
        cols = col_row_list[1]
        i = 0
        fig = make_subplots(rows=rows, cols=cols, subplot_titles=title)
        for row in range(1, rows + 1):
            for col in range(1, cols + 1):
                x = x_list[i]
                y = y_list[i]
                name = name_list[i]
                for j in range(len(x)):
                    if color_list:
                        color = color_list[i]
                        fig.add_trace(go.Scattergl(x=x[j], y=y[j], name=name[j], marker=dict(color=color[j]), mode=mode), row=row, col=col)
                    else:
                        fig.add_trace(go.Scattergl(x=x[j], y=y[j], name=name[j], mode=mode), row=row, col=col)
                i += 1
        if subplot_title:
            fig.update_layout(title=dict(text=subplot_title, y=0.98, x=0.48, xanchor='center', yanchor='top'), title_font=dict(size=18))
        fig.write_html(gest_file)
        # fig.show()
    else:
        for i in range(len(x_list)):
            layout = go.Layout(title=dict(text=title[i], y=0.9, x=0.5, xanchor='center', yanchor='top'))
            fig = go.Figure(layout=layout)
            for j in range(len(x_list[i])):
                fig.add_trace(go.Scattergl(x=x_list[i][j], y=y_list[i][j], name=name_list[i][j], mode=mode))
            fig.write_html(gest_file)
            # fig.show()


def plot_grid(gps_lon, gps_lat, alg_lon, alg_lat, KF_lon, KF_lat, time, step_x, step_y, out_file):
    """
    画出完整的路径图带有网格线和时间标签
    :param gps_lon:
    :param gps_lat:
    :param alg_lon:
    :param alg_lat:
    :param time:
    :param step:
    :return:
    """
    tick_label_len = 60
    x_tickvals = np.arange(np.min(alg_lon), np.max(alg_lon), step_x)  # 经度
    y_tickvals = np.arange(np.min(alg_lat), np.max(alg_lat), step_y)  # 纬度
    x_ticktext = []
    y_ticktext = []
    for i in range(len(x_tickvals)):
        if i % tick_label_len == 0:
            x_ticktext.append(x_tickvals[i])
        else:
            x_ticktext.append(" ")
    for i in range(len(y_tickvals)):
        if i % tick_label_len == 0:
            y_ticktext.append(y_tickvals[i])
        else:
            y_ticktext.append(" ")

    layout = go.Layout(template='plotly_dark',
                       title=dict(text='gps-algorithm-path', ), # y=0.9, x=0.5, xanchor='center', yanchor='top'
                       xaxis=dict(tickvals=x_tickvals, ticktext=x_ticktext,
                                  range=(np.min(alg_lon), np.max(alg_lon)),
                                  showgrid=True, dtick=1 / 6383859.769207644 * R2D),
                       yaxis=dict(tickvals=y_tickvals, ticktext=y_ticktext, scaleanchor="x", scaleratio=1,
                                  range=(np.min(alg_lat), np.max(alg_lat)), showgrid=True,
                                  dtick=1 / 6383859.769207644 * R2D))

    text_list = ["t=" + str(t) + "\nid=" + str(idx) for t, idx in zip(time, range(len(time)))]
    text_list_gps = ["t=" + str(t) + "\nid=" + str(idx) for t, idx in zip(time, range(len(time)))]

    fig = go.Figure(layout=layout)
    fig.add_trace(go.Scattergl(x=alg_lon, y=alg_lat, text=text_list, mode='markers', name='riss-path', marker=dict(size=3)))
    fig.add_trace(go.Scattergl(x=gps_lon, y=gps_lat, text=text_list_gps, mode='markers', name='gps-path', marker=dict(size=3)))
    fig.add_trace(go.Scattergl(x=KF_lon, y=KF_lat, mode='markers', name='KF-update', marker=dict(size=5)))
    fig.write_html(out_file)
    # fig.show()


def plot_grid_3_path(gps_lon, gps_lat, alg_lon, alg_lat, alg_time, time, KF_lon, KF_lat, step_x, step_y):
    """
    画出完整的路径图带有网格线和时间标签
    :param gps_lon:
    :param gps_lat:
    :param alg_lon:
    :param alg_lat:
    :param time:
    :param step:
    :return:
    """
    x_tickvals = np.arange(np.min(alg_lon), np.max(alg_lon), step_x)  # 经度
    y_tickvals = np.arange(np.min(alg_lat), np.max(alg_lat), step_y)  # 纬度
    x_ticktext = []
    y_ticktext = []
    for i in range(len(x_tickvals)):
        if i % 30 == 0:
            x_ticktext.append(x_tickvals[i])
        else:
            x_ticktext.append(" ")
    for i in range(len(y_tickvals)):
        if i % 30 == 0:
            y_ticktext.append(y_tickvals[i])
        else:
            y_ticktext.append(" ")

    layout = go.Layout(template='plotly_dark',
                       title=dict(text='gps-algorithm-path', ), # y=0.9, x=0.5, xanchor='center', yanchor='top'
                       xaxis=dict(tickvals=x_tickvals, ticktext=x_ticktext,
                                  range=(np.min(alg_lon), np.max(alg_lon)),
                                  showgrid=True, dtick=1 / 6383859.769207644 * R2D),
                       yaxis=dict(tickvals=y_tickvals, ticktext=y_ticktext, scaleanchor="x", scaleratio=1,
                                  range=(np.min(alg_lat), np.max(alg_lat)), showgrid=True,
                                  dtick=1 / 6383859.769207644 * R2D))

    text_list = ["t=" + str(t) + "\nid=" + str(idx) for t, idx in zip(alg_time, range(len(alg_time)))]
    text_list_gps = ["t=" + str(t) + "\nid=" + str(idx) for t, idx in zip(time, range(len(time)))]

    fig = go.Figure(layout=layout)
    fig.add_trace(go.Scattergl(x=alg_lon, y=alg_lat, text=text_list, mode='markers', name='riss-path', marker=dict(size=3)))
    fig.add_trace(go.Scattergl(x=gps_lon, y=gps_lat, text=text_list_gps, mode='markers', name='gps-path', marker=dict(size=3)))
    fig.add_trace(go.Scattergl(x=KF_lon, y=KF_lat, mode='markers', name='KF-update', marker=dict(size=5)))
    fig.show()


def index_to_graph1(time_left_list, time_right_list, gps_lon, gps_lat, alg_lon, alg_lat, KF_lon, KF_lat,  time, step_x, step_y):
    """
    根据时间获取对应位置的路径图
    :param time_left_list: [] 填入希望获取的位置路径图对应的时间起始位置
    :param time_right_list: [] 填入希望获取的位置路径图对应的时间结束位置
    :param gps_lon:
    :param gps_lat:
    :param alg_lon:
    :param alg_lat:
    :param time:
    :param step:
    :return:
    """
    # time = time.to_numpy()
    gps_lon_list = []
    gps_lat_list = []
    alg_lon_list = []
    alg_lat_list = []
    time_list = []
    for time_left, time_right in zip(time_left_list, time_right_list):
        # index_left = np.where(time == time_left)[0][0]
        # index_right = np.where(time == time_right)[0][0]
        gps_lon1 = gps_lon[time_left:time_right]
        gps_lat1 = gps_lat[time_left:time_right]
        alg_lon1 = alg_lon[time_left:time_right]
        alg_lat1 = alg_lat[time_left:time_right]
        gps_lon_list.extend(gps_lon1)
        gps_lat_list.extend(gps_lat1)
        alg_lon_list.extend(alg_lon1)
        alg_lat_list.extend(alg_lat1)
        time_list.extend(time[time_left:time_right])
    plot_grid(gps_lon_list, gps_lat_list, alg_lon_list, alg_lat_list, KF_lon, KF_lat, time_list, step_x, step_y)

