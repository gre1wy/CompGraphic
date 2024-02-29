import matplotlib.pyplot as plt

def generate_cantor_fractal(start, end, depth):
    if depth == 0:
        return [(start, end)]
    
    third = (end - start) / 3
    left_third = start + third
    right_third = end - third
    
    # Вилучаємо інтервал з точками, де є цифри 3 та 7
    middle_interval = (left_third, right_third)
    cantor_fractal = generate_cantor_fractal(start, left_third, depth - 1) + \
                     [middle_interval] + \
                     generate_cantor_fractal(right_third, end, depth - 1)
    
    return cantor_fractal

def plot_cantor_fractal(cantor_fractal):
    for interval in cantor_fractal:
        plt.plot(interval, [0, 0], color='black', linewidth=1)
    plt.gca().axes.get_yaxis().set_visible(False)
    plt.show()

if __name__ == "__main__":
    depth = 5  # Глибина рекурсії
    cantor_fractal = generate_cantor_fractal(0, 1, depth)
    plot_cantor_fractal(cantor_fractal)
