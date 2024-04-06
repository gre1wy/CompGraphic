import matplotlib.pyplot as plt
import numpy as np

def generate_barnsley_fern(rules, iterations=1000, delay=0.01):
    # Початкові координати
    x, y = [0], [0]

    # Створення графіку
    fig, ax = plt.subplots()
    ax.set_aspect('equal')
    ax.set_xlim(-3, 3)
    ax.set_ylim(0, 10)
    plt.title('Dynamic Barnsley Fern')

    # Додавання точок поступово
    for _ in range(iterations):
        rule = np.random.choice(rules)
        x1 = rule['a'] * x[-1] + rule['b'] * y[-1] + rule['e']
        y1 = rule['c'] * x[-1] + rule['d'] * y[-1] + rule['f']
        x.append(x1)
        y.append(y1)
        ax.plot(x1, y1, '.', color='green', markersize=0.5)
        plt.draw()
        plt.pause(delay)
        plt.show()

# Виклик функції з вашими наборами правил
rules = [
    {'a': 0.2020, 'b': -0.8050, 'c': -0.6890, 'd': -0.3420, 'e': -0.3730, 'f': -0.6530},
    {'a': 0.1380, 'b': 0.6650, 'c': -0.5020, 'd': -0.2220, 'e': 0.6600, 'f': -0.2770}
]

generate_barnsley_fern(rules)
