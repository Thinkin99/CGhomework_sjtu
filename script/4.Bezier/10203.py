import matplotlib.pyplot as plt
import numpy as np

def cal_Casteljau(t):
    for r in range(1, n):
        for i in range(0, n - r):
            PP[i][r] = (1 - t) * PP[i][r - 1] + t * PP[i + 1][r - 1]
    re.append(PP[0][r].tolist())
    re.append(p[n - 1])

if __name__ == '__main__':
    p = []
    a = int(input("----是否选择自己输入任意数量点的坐标 1.是；0.否----"))
    if a == 1:
        b = int(input("---请输入控制点的数量---"))
        for i in range(b):
            tmpx = float(input("---请输入第" + str(i + 1) + "个点x值--- "))
            tmpy = float(input("---请输入第" + str(i + 1) + "个点y值--- "))
            p.append([tmpx, tmpy])

    else:
        p = [[0, 1],
             [5, 8],
             [13, 19],
             [20, 30],
             [30, 35],
             [45, 40],
             [57, 39],
             [65, 24],
             [70, 18],
             [85, -18],
             [90, -30],
             [98, -35],
             [123, -38],
             [146, 45],
             [167, 36],
             [178, -35],
             [180, -54],
             [200, -44],
             [235, 30],
             [246, 30],
             [267, 27],
             [280, 8],
             ]
    p.append([-1, -1])
    n = len(p) - 1
    # print(p)
    point_control_x = []
    point_control_y = []

    PP = np.array([[[0 for _ in range(2)] for _ in range(n + 1)] for _ in range(n + 1)], dtype=float)
    re = []
    for i in range(0, n):
        PP[i][0] = p[i]
        point_control_x.append(p[i][0])
        point_control_y.append(p[i][1])

    for t in range(0, 500):
        cal_Casteljau(t / 500)

    # print(re)
    plt.plot(point_control_x, point_control_y, "k", linewidth='2')
    for i in range(len(p) - 1):
        plt.plot(p[i][0], p[i][1], "b.", linewidth='3')

    for i in range(len(re)):
        plt.plot(re[i][0], re[i][1], "r.", linewidth='1')
    plt.show()

