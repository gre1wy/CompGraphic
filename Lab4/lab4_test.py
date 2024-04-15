import matplotlib.pyplot as plt
import numpy as np

def generate_fractal(rules: dict, iterations: int):
    x, y, colors = [0], [0], []
    for _ in range(iterations):
        rule = np.random.choice(rules, p=[rule['p'] for rule in rules])
        x1 = rule['a'] * x[-1] + rule['b'] * y[-1] + rule['e']
        y1 = rule['c'] * x[-1] + rule['d'] * y[-1] + rule['f']
        color = rule['color']
        x.append(x1)
        y.append(y1)
        colors.append(color)
    return x, y, colors

def display_fractal(rules: dict, iterations: int, delay: float, pixels: int):
    x, y, colors = generate_fractal(rules, iterations)
    plt.figure()  
    plt.ion() 
    annotation = None 
    for i in range(0, iterations, pixels):
        if annotation is not None:
            annotation.remove()
        plt.scatter(x[i:i+pixels], y[i:i+pixels], c=colors[i:i+pixels], s=10, alpha=0.5)
        plt.title('Fractal')
        annotation = plt.annotate(f'Pixels drawn: {i}', xy=(0, 0), fontsize=10, color='red')
        plt.draw()
        plt.pause(delay)
    plt.ioff()  
    plt.show()

rules = [
    {'a': 0.0, 'b': -0.5, 'c': 0.5, 'd': 0.0, 'e': 0.5, 'f': 0.0, 'p': 1/3, 'color':'red'},
    {'a': 0.0, 'b': 0.5, 'c': -0.5, 'd': 0.0, 'e': 0.5, 'f': 0.5, 'p': 1/3, 'color':'green'},
    {'a': 0.5, 'b': 0.0, 'c': 0.0, 'd': 0.5, 'e': 0.25, 'f': 0.5, 'p': 1/3, 'color':'blue'}
]

display_fractal(rules, iterations=100000, delay=0.01, pixels=1000)
