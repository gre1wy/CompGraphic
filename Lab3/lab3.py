from matplotlib.animation import FuncAnimation, PillowWriter
import numpy as np
import matplotlib.pyplot as plt

def moves(axiom, rules: dict, max_iter):
    for _ in range(max_iter):
        newaxiom = ""
        for el in axiom:
            if el in rules.keys():
                newaxiom += str(rules[el])
            else:
                newaxiom += el
        axiom = newaxiom
    return axiom

def data_fractal(axiom, rules, max_iter, fi, dfi):
    if type(dfi) != float:
        dfi = np.radians(dfi)
    fractal = moves(axiom, rules, max_iter)
    N = len(fractal)
    x = np.zeros(N + 1)
    y = np.zeros(N + 1)
    L = 2
    for i in range(N):
        x[i + 1] = x[i]
        y[i + 1] = y[i]
        if fractal[i] == "F":
            x[i + 1] += L * np.cos(fi)
            y[i + 1] += L * np.sin(fi)
        elif fractal[i] == "+":
            fi += dfi
        elif fractal[i] == "-":
            fi -= dfi
    return x, y

# Дані фрактала
axiom8 = "FX"
rules8 = {"F": "-F++F-"}
max_iter8 = 15
fi8 = 0
dfi8 = np.pi / 2

# Функція апдейту фрактала
def update(frame):
    ax.clear()
    ax.plot(x_data[frame], y_data[frame], linewidth=0.4)
    ax.set_title(f'dfi = {dfi_values[frame]}')
    #ax.set_aspect('equal', adjustable='box')
    ax.grid(True)

# Генерація данних для кожного dfi
dfi_values = np.arange(-180, 180)
x_data = []
y_data = []
for dfi_data in dfi_values:
    x, y = data_fractal(axiom8, rules8, max_iter8, fi8, dfi_data)
    x_data.append(x)
    y_data.append(y)

# Створення анімації
fig, ax = plt.subplots(figsize=(10, 8))
anim = FuncAnimation(fig, update, frames=len(dfi_values), interval=200)

# Створення гіфки
writer = PillowWriter(fps=10) 
anim.save('CompGraphic/Lab3/fractal_animation4.gif', writer=writer)

