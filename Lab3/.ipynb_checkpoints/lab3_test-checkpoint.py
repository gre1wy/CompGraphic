import turtle
import numpy as np
import time

def test():
    axiom = "F"
    rule = "F+F--F+F"
    max_iter = 5
    for _ in range(max_iter):
        newaxiom = ""
        for el in axiom:
            if el == "F":
                newaxiom = newaxiom + rule
            else:
                newaxiom = newaxiom + el
        axiom = newaxiom

    return axiom

def vis_axiom(axiom):
    fi = 0
    dfi = np.pi/3
    N = len(axiom)
    L = 0.1

    turtle.speed(0)  
    turtle.setworldcoordinates(0, 0, 200, 200)
    turtle.tracer(False)
    start_time = time.time()

    for i in range(N):
        if axiom[i] == "F":
            turtle.forward(L)
        elif axiom[i] == "+":
            fi += dfi
            turtle.left(np.degrees(dfi))
        elif axiom[i] == "-":
            fi -= dfi
            turtle.right(np.degrees(dfi))

    end_time = time.time()
    elapsed_time = end_time - start_time
    print(f"Час виконання: {elapsed_time:.5f} секунд")

    turtle.done()

if __name__ == "__main__":
    axiom_result = test()
    vis_axiom(axiom_result)
