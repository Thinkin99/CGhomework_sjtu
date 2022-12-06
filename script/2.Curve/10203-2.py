import matplotlib.pyplot as plt
# pip install matplotlib
def Bresenham_Circle(x0, y0, r):
    plt.plot(x0, y0, "r.", linewidth='3')
    plt.text(x0 - 1, y0 - 1, str([x0, y0]), color="k")
    x = 0
    y = r
    d = 2 * (1 - r)
    while y >= 0:
        plt.plot(x + x0, y + y0, "r.")
        plt.plot(y + x0, -x + y0, "r.")
        plt.plot(-x + x0, -y + y0, "r.")
        plt.plot(-y + x0, x + y0, "r.")
        if d < 0:
            delta1 = ((d + y) << 1) - 1
            if delta1 <= 0:
                flag = 1
            else:
                flag = 2
        elif d > 0:
            d2 = ((d - x) << 1) - 1
            if d2 <= 0:
                flag = 2
            else:
                flag = 3
        else:
            flag = 2

        if flag == 1:
            x += 1
            d += (x << 1) + 1
        elif flag == 2:
            x += 1
            y -= 1
            d += ((x - y) << 1) + 2
        else:
            y -= 1
            d += 1 - (y << 1)

if __name__ == '__main__':
    on = int(input("---是否选择自定义输入坐标。1：是。0：否。--- "))
    if on == 1:
        print("----按顺序依次输入圆心坐标+半径 x,y,radius----")
        x = int(input("x= "))
        y = int(input("y= "))
        radius = int(input("radius= "))
    else:
        x = 40
        y = 50
        radius = 35

    Bresenham_Circle(x, y, radius)
    plt.axis("equal")
    plt.grid(linestyle='--')
    plt.show()

