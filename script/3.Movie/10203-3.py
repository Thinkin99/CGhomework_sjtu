import matplotlib.pyplot as plt
import numpy as np
import keyboard
# 需要依赖三个库 matplotlib numpy keyboard
# pip install matplotlib
# pip install numpy
# pip install keyboard

flag = False
def key_press(key):
    global flag
    if key.name:
        flag = True

def draw_circle(x, y, r):
    theta = np.linspace(0, 2 * np.pi, 100)
    a = x + r * np.cos(theta)
    b = y + r * np.sin(theta)
    plt.plot(a, b)
    plt.show()
def draw_other():
    x = [-22, -22, 200 + 22, 222, -22]
    y = [-22, 100 + 22, 100 + 22, -22, -22]
    plt.plot(x, y, linewidth='2', color='k')
    x = [0, 0, 200, 200, 0]
    y = [0, 100, 100, 0, 0]
    plt.plot(x, y)
    x = [0, 100, 200, 100, 0]
    y = [50, 100, 50, 0, 50]
    plt.plot(x, y)
if __name__ == '__main__':
    R = 5
    x1 = float(R * pow(R, 0.5))
    y1 = 50
    x2 = 100
    y2 = 100 - 0.5 * x1
    x3 = 200 - x1
    y3 = 50
    x4 = 100
    y4 = 0.5 * x1
    x12 = np.linspace(x1, x2, 20)
    y12 = 0.5 * x12 + 50 - 0.5 * 5 * pow(5, 0.5)
    x23 = np.linspace(x2, x3, 20)
    y23 = - 0.5 * x23 + 150 - 0.5 * 5 * pow(5, 0.5)
    x34 = np.linspace(x3, x4, 20)
    y34 = 100 - y23
    y34 = y34[::-1]
    x41 = np.linspace(x4, x1, 20)
    y41 = 100 - y12
    y41 = y41[::-1]
    clock_x = np.append(x12, x23)
    clock_x = np.append(clock_x, x34)
    clock_x = np.append(clock_x, x41)
    clock_y = np.append(y12, y23)
    clock_y = np.append(clock_y, y34)
    clock_y = np.append(clock_y, y41)
    anti_clock_x = clock_x[::-1]
    anti_clock_y = clock_y[::-1]
    keyboard.on_press(key_press)
    while (1):
        for i in range(len(clock_x)):
            plt.ion()
            plt.cla()
            draw_other()
            draw_circle(clock_x[i], clock_y[i], R)
            plt.pause(0.01)
            plt.ioff()
            if flag:
                break
        if flag:
            break
        for j in range(len(anti_clock_x)):
            plt.ion()
            plt.cla()
            draw_other()
            draw_circle(anti_clock_x[j], anti_clock_y[j], R)
            plt.pause(0.01)
            plt.ioff()
            if flag:
                break
        if flag:
            break
    plt.close()


