import turtle 
import numpy as np
import matplotlib.pyplot as plt


def moves():
    axiom = "F-F-F-F"
    rule = "F+FF-FF-F-F+F+FF-F-F+F+FF+FF-F"
    max_iter = 5
    for _ in range(max_iter-1):
        newaxiom = ""
        for el in axiom:
            if el == "F":
                newaxiom += rule
            else:
                newaxiom += el
        axiom = newaxiom

    return axiom

def vis_axiom(str):
    fi = 0
    dfi = np.pi/2
    N=len(str)
    x = np.zeros(N+1)
    y = np.zeros(N+1)
    L = 2
    for i in range(N):
        x[i+1]=x[i]
        y[i+1]=y[i]
        if str[i]=="F":
            x[i+1] += L*np.cos(fi)
            y[i+1] += L*np.sin(fi)
        elif str[i]=="+":
            fi+=dfi
        elif str[i]=="-":
            fi-=dfi
    return x, y


if __name__ == "__main__":
    result_axiom = moves()
    x, y = vis_axiom(result_axiom)
    fig, ax = plt.subplots()
    ax.plot(x, y, linewidth=0.4)
    plt.show()


