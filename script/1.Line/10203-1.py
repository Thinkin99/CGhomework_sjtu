import matplotlib.pyplot as plt
#  画直线程序在坐标点起点、终点值过小时会离散成单独的点，
#  原因在于画图的界面大小会自适应的放大 但画出来的点的大小是一样的
#  依赖matplotlib
#  pip install matplotlib
def MidpointLine(x0, y0, x1, y1, color):
    a = y0 - y1
    b = x1 - x0
    d = 2 * a + b
    d1 = 2 * a
    d2 = 2 * (a + b)
    x = x0
    y = y0
    plt.plot(x, y, color)
    while (x < x1):
        if (d < 0):
            x = x + 1
            y = y + 1
            d = d + d2
        else:
            x = x + 1
            d = d + d1
        plt.plot(x, y, color)
    plt.show()


def DDALine(x1, y1, x2, y2, color):
    dx = x2 - x1
    dy = y2 - y1
    steps = 0
    if abs(dx) > abs(dy):
        steps = abs(dx)
    else:
        steps = abs(dy)
    delta_x = float(dx / steps)
    delta_y = float(dy / steps)
    x = x1 + 0.5
    y = y1 + 0.5
    for i in range(0, int(steps + 1)):
        plt.plot(x, y, color)
        x += delta_x
        y += delta_y
    plt.show()


def BresenhamLine(x0, y0, x1, y1, color):
    dx = x1 - x0
    dy = y1 - y0
    k = dy / dx
    e = -0.5
    x = x0
    y = y0
    i = 0
    while (i <= dx):
        plt.plot(x, y, color)
        x = x + 1
        e = e + k
        if (e >= 0):
            y = y + 1
            e = e - 1
        i = i + 1
    plt.show()

if __name__ == '__main__':
    on = int(input("---是否选择自定义输入坐标。1：是。0：否。--- "))
    if on == 1:
        print("----按顺序依次输入x0,y0,xend,yend----")
        x0 = float(input("x0= "))
        y0 = float(input("y0= "))
        xend = float(input("xend= "))
        yend = float(input("yend= "))
    else:
        x0 = 13
        y0 = 25
        xend = 87
        yend = 60

    flag = int(input("---选择直线插补的方式: 1.DDALine 2.MidpointLine 3. BresenhamLine--- :"))
    color = "r."
    if (flag == 1):
        DDALine(x0, y0, xend, yend, color)
    elif (flag == 2):
        MidpointLine(x0, y0, xend, yend, color)
    elif (flag == 3):
        BresenhamLine(x0, y0, xend, yend, color)

    else:
        print("please input the right flag")

