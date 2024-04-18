import matplotlib.pyplot as plt
import numpy as np

def generate_fractal(rules: dict, iterations: int):
    x, y = [0], [0]
    if 'a' in rules[0]:
        if 'p' in rules[0]:
            for _ in range(iterations):
                rule = np.random.choice(rules, p=[rule['p'] for rule in rules])
                x1 = rule['a'] * x[-1] + rule['b'] * y[-1] + rule['e']
                y1 = rule['c'] * x[-1] + rule['d'] * y[-1] + rule['f']
                x.append(x1)
                y.append(y1)
        else:
            for _ in range(iterations):
                rule = np.random.choice(rules)
                x1 = rule['a'] * x[-1] + rule['b'] * y[-1] + rule['e']
                y1 = rule['c'] * x[-1] + rule['d'] * y[-1] + rule['f']
                x.append(x1)
                y.append(y1)
    else:
        if 'p' in rules[0]:
            for _ in range(iterations):
                rule = np.random.choice(rules, p=[rule['p'] for rule in rules])
                x1 = rule['r'] *np.cos(rule['theta'])* x[-1] - rule['s']*np.sin(rule['phi'])*y[-1] + rule['e']
                y1 = -rule['r']*np.sin(rule['theta']) * x[-1] + rule['s']*np.cos(rule['phi'])* y[-1] + rule['f']
                x.append(x1)
                y.append(y1)
        else:
            for _ in range(iterations):
                rule = np.random.choice(rules)
                x1 = rule['r'] *np.cos(rule['theta'])* x[-1] - rule['s']*np.sin(rule['phi'])*y[-1] + rule['e']
                y1 = -rule['r']*np.sin(rule['theta']) * x[-1] + rule['s']*np.cos(rule['phi'])* y[-1] + rule['f']
                x.append(x1)
                y.append(y1)

    return x, y



def display_fractal(rules: dict, iterations: int, delay: float, pixels: int, name='fractal'):
    x, y = generate_fractal(rules, iterations)
    plt.figure()  
    plt.ion() 
    annotation = None 
    for i in range(iterations+1):
        if i % pixels == 0:
            if annotation is not None:
                annotation.remove()
            plt.plot(x[i:i+pixels], y[i:i+pixels], '*', color='green', markersize=0.5)
            plt.title(name)
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
rules = [
    {'a': 0.05,'b': 0,'c': 0,'d': 0.6,'e': 0,'f': 0,'p': 0.17},
    {'a': 0.05,'b': 0,'c': 0,'d': -0.5,'e': 0,'f': 1,'p': 0.17},
    {'a': 0.46,'b': -0.321,'c': 0.386,'d': 0.383,'e': 0,'f': 0.6,'p': 0.17},
    {'a': 0.47,'b': -0.154,'c': 0.171,'d': 0.423,'e': 0,'f': 1.1,'p': 0.17},
    {'a': 0.433,'b': 0.275,'c': -0.25,'d': 0.476,'e': 0,'f': 1,'p': 0.16},
    {'a': 0.421,'b': 0.257,'c': -0.353,'d': 0.306,'e': 0,'f': 0.7,'p': 0.16}
]
rules = [
    {'r': 0.0500, 's': 0.6000, 'theta': 0.0000, 'phi': 0.0000, 'e': 0.0000, 'f': 0.0000},
    {'r': 0.0500, 's': -0.5000, 'theta': 0.0000, 'phi': 0.0000, 'e': 0.0000, 'f': 1.0000},
    {'r': 0.6000, 's': 0.5000, 'theta': 0.6980, 'phi': 0.6980, 'e': 0.0000, 'f': 0.6000},
    {'r': 0.5000, 's': 0.4500, 'theta': 0.3490, 'phi': 0.3492, 'e': 0.0000, 'f': 1.1000},
    {'r': 0.5000, 's': 0.5500, 'theta': -0.5240, 'phi': -0.5240, 'e': 0.0000, 'f': 1.0000},
    {'r': 0.5500, 's': 0.4000, 'theta': -0.6980, 'phi': -0.6980, 'e': 0.0000, 'f': 0.7000}
]
rules = [
    {'a': 0.21,'b': 3,'c': 0,'d': 0.4,'e': 0,'f': 0,'p': 0.17},
    {'a': 0.12,'b': 2,'c': 0,'d': -0.2,'e': 0,'f': 2,'p': 0.17},
    {'a': 0.14,'b': -0.21,'c': 0.82,'d': 0.3,'e': 0,'f': 0.2,'p': 0.17},
    {'a': 0.47,'b': -0.56,'c': 0.11,'d': 0.2,'e': 0,'f': 1,'p': 0.17},
    {'a': 0.05,'b': 0.12,'c': 0.34,'d': 0.612,'e': 0,'f': 2,'p': 0.16},
    {'a': 0.31,'b': 0.6,'c': -0.38,'d': 0.21,'e': 0,'f': 0.2,'p': 0.16}
]
if __name__ == "__main__":
    display_fractal(rules, iterations=100000, delay=0.01, pixels=100000, name="hello")


