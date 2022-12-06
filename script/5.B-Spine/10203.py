import matplotlib.pyplot as plt
import numpy as np
def draw_b_spline(n, k, nodeVector, X, Y):
    plt.figure()
    basis_i = np.zeros(100)
    rx = np.zeros(100)
    ry = np.zeros(100)
    for i in range(n + 1):
        U = np.linspace(nodeVector[k], nodeVector[n + 1], 100)
        j = 0
        for u in U:
            nodeVector = np.array(nodeVector)
            basis_i[j] = b_spline_basis(i, k, u, nodeVector)
            j = j + 1
        rx = rx + X[i] * basis_i
        ry = ry + Y[i] * basis_i
    rx[0] = X[0]
    ry[0] = Y[0]
    plt.plot(X, Y)
    plt.plot(rx, ry, "r", linewidth='2')
    plt.show()
def b_spline_basis(i, k, u, nodeVector):
    if k == 0:
        if (nodeVector[i] < u) & (u <= nodeVector[i + 1]):
            result = 1
        else:
            result = 0
    else:
        length1 = nodeVector[i + k] - nodeVector[i]
        length2 = nodeVector[i + k + 1] - nodeVector[i + 1]
        if length1 == 0:
            a = 0
        else:
            a = (u - nodeVector[i]) / length1
        if length2 == 0:
            b = 0
        else:
            b = (nodeVector[i + k + 1] - u) / length2
        result = a * b_spline_basis(i, k - 1, u, nodeVector) + b * b_spline_basis(i + 1, k - 1, u, nodeVector)
    return result

if __name__ == '__main__':
    p = []
    print("---De Boor分割算法画B-spine---")
    print("----1.选择自己输入坐标可以实现任意控制顶点的3次B-spine的绘制。----")
    print("----0.不选择输入则进行25个控制点的3次B-spine的绘制。----")
    a = int(input("---是否选择自己输入任意数量点的坐标 1.是；0.否---"))

    if a == 1:
        b = int(input("---请输入控制点的数量---"))
        for i in range(b):
            tmpx = float(input("---请输入第" + str(i + 1) + "个点x值--- "))
            tmpy = float(input("---请输入第" + str(i + 1) + "个点y值--- "))
            p.append([tmpx, tmpy])
    else:
        p = [[5, 5],
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
             [300, -10],
             [320, 10],
             [330, 30]
             ]
    n = len(p)-1  #n+1=25
    k = 3

    nodeVector = [0,0,0]
    X = []
    Y = []
    for i in range(0, len(p)):
        X.append(p[i][0])
        Y.append(p[i][1])
    for i in range(0, n+2-k):
        nodeVector.append(i)
    nodeVector.append(n-k+1)
    nodeVector.append(n-k+1)
    nodeVector.append(n-k+1)
    print(nodeVector)
    print(len(nodeVector))
    draw_b_spline(n, k, nodeVector, X, Y)







