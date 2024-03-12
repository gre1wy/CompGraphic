import turtle 
import numpy as np
import matplotlib.pyplot as plt


def test():
    axiom = "F"
    rule = "F+F--F+F"
    max_iter = 10
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
    dfi = np.pi/3
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
    print(x)
    print(y)
    return x, y


if __name__ == "__main__":
    axiom_result = test()
    x,y = vis_axiom(axiom_result)
    fig, ax = plt.subplots()
    ax.plot(x, y, linewidth=2.0)
    plt.show()


