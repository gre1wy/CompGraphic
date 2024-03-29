from matplotlib.animation import ArtistAnimation
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.lines import Line2D
# Определение функций 'moves' и 'data_fractal'
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

# Инициализация переменных
axiom8 = "FX"
rules8 = {"F": "-F++F-"}
max_iter8 = 15
fi8 = 0
dfi8 = np.pi / 2

# Создание данных для каждого dfi
dfi_values = np.arange(-30, 30)
frames = []
for dfi_data in dfi_values:
    x, y = data_fractal(axiom8, rules8, max_iter8, fi8, dfi_data)
    line = Line2D(x, y, linewidth=0.4)
    frames.append(line)  # Здесь каждый элемент frames является списком объектов Line2D

# Создание анимации с использованием ArtistAnimation
fig, ax = plt.subplots(figsize=(10, 8))
ax.set_aspect('equal', adjustable='box')
ax.grid(True)

# Используйте ArtistAnimation с передачей списка списков объектов Line2D
anim = ArtistAnimation(fig, frames, interval=30)

plt.show()

