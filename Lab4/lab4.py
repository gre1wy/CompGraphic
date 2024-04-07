import matplotlib.pyplot as plt
import numpy as np

def generate_fractal(rules: dict, iterations: int):
    # Початкові координати
    x, y = [0], [0]

    # Генерація фракталу
    for _ in range(iterations):
        rule = np.random.choice(rules)
        x1 = rule['a'] * x[-1] + rule['b'] * y[-1] + rule['e']
        y1 = rule['c'] * x[-1] + rule['d'] * y[-1] + rule['f']
        x.append(x1)
        y.append(y1)
    return x, y

def display_fractal(rules: dict, iterations: int, delay: float, pixels: int):
    x, y = generate_fractal(rules, iterations)
    plt.figure()  
    plt.ion() 
    annotation = None 
    for i in range(iterations+1):
        if i % pixels == 0:
            if annotation is not None:
                annotation.remove()
            plt.plot(x[i:i+pixels], y[i:i+pixels], '*', color='green', markersize=0.5)
            plt.title('Fractal')
            annotation = plt.annotate(f'Pixels drawn: {i}', xy=(0, 0), fontsize=10, color='red')
            plt.draw()
            plt.pause(delay)
    plt.ioff()  
    plt.show()

rules = [
    {'a': 0.1950, 'b': -0.4880, 'c': 0.3440, 'd': 0.4430, 'e': 0.4431, 'f': 0.2452},
    {'a': 0.4620, 'b': 0.4140, 'c': -0.2520, 'd': 0.3610, 'e': 0.2511, 'f': 0.5692},
    {'a': -0.6370, 'b': 0.0000, 'c': 0.0000, 'd': 0.5010, 'e': 0.8562, 'f': 0.2512},
    {'a': -0.0350, 'b': 0.0700, 'c': -0.4690, 'd': 0.0220, 'e': 0.4884, 'f': 0.5069},
    {'a': -0.0580, 'b': -0.0700, 'c': 0.4530, 'd': -0.1110, 'e': 0.5976, 'f': 0.0969}
]
# Первый вызов функции display_fractal
display_fractal(rules, iterations=10000, delay=0.01, pixels=100)


