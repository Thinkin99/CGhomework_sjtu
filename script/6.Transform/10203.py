import numpy as np
import matplotlib.pyplot as plt
import math
def T_zc(theta, phi):
    # Rz绕z轴旋转theta
    # Rx绕x轴旋转phi
    # Tv投影到v
    Rz = np.zeros((4, 4), dtype=float)
    Rx = np.zeros((4, 4), dtype=float)
    Tv = np.zeros((4, 4), dtype=float)
    Rz[0][0] = math.cos(theta)
    Rz[1][1] = math.cos(theta)
    Rz[0][1] = math.sin(theta)
    Rz[1][0] = -math.sin(theta)
    Rz[2][2] = 1
    Rz[3][3] = 1
    Rx[0][0] = 1
    Rx[1][1] = math.cos(phi)
    Rx[2][2] = math.cos(phi)
    Rx[3][3] = 1
    Rx[2][1] = math.sin(phi)
    Rx[1][2] = -math.sin(phi)
    Tv[0][0] = 1
    Tv[2][2] = 1
    Tv[3][3] = 1
    temp = np.dot(Rz, Rx)
    Tzc = np.dot(temp, Tv)
    return Tzc

def trivs(n, x, y, z, a, iw, u, v, theta, fi):
    # n: 立体的顶点数；
    # x, y, z: 顶点的坐标；
    # a: 视图间的距离；
    # iw: 取值1到4，分别对应计算主、俯、左、正等轴测视图的坐标
    # u、v: 绘图坐标系中的坐标
    # theta fi 轴测图参数

    # 0初始化cdt矩阵
    c = np.zeros((100, 4), dtype=float)
    d = np.zeros((100, 4), dtype=float)
    t = np.zeros((4, 4), dtype=float)
    # 转换为齐次坐标的形式
    for i in range(n):
        c[i][0] = x[i]
        c[i][1] = y[i]
        c[i][2] = z[i]
        c[i][3] = 1
    t[3][3] = 1
    if iw == 1:
        t[0][0] = 1
        t[2][2] = 1
    if iw == 2:
        t[0][0] = 1
        t[1][2] = -1
        t[3][2] = -a
    if iw == 3:
        t[1][0] = -1
        t[2][2] = 1
        t[3][0] = -a
    if iw == 4:
        t = T_zc(theta, fi)  # 正轴测
    d = np.dot(c, t)
    for i in range(n):
        u[i] = round(-d[i][0])
        v[i] = round(d[i][2])

def read_file(path):
    # 数据读取存成list
    data = []
    with open(path) as f:
        for line in f.readlines():
            temp = line.split()
            temp = [int(i) for i in temp]
            data.append(temp)
    return data

if __name__ == '__main__':
    path = r'./10203.txt'
    data = read_file(path)
    x = np.array(data[0], dtype=int)
    y = np.array(data[1], dtype=int)
    z = np.array(data[2], dtype=int)
    i = len(x)
    n = i
    a = 20  # 间距
    u = np.zeros((n, 4), dtype=float)
    v = np.zeros((n, 4), dtype=float)
    theta = 45 / 180 * np.pi
    phi = 35.26 / 180 * np.pi
    flag = int(input("---请选择程序功能: 0.绘制三视图 1.绘制主视图 2.绘制俯视图 3.绘制左视图 4.绘制正等轴测图 :"))
    if flag != 0:
        trivs(n, x, y, z, a, flag, u, v, theta, phi)
        plt.plot(u, v, 'k')
    else:
        for iw in range(1, 4):
            trivs(n, x, y, z, a, iw, u, v, theta, phi)
            plt.plot(u, v, 'k')
    plt.show()

