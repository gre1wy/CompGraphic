import matplotlib.pyplot as plt

def remove_third_seventh(interval):
    # Видаляємо третю та сьому частину відрізка
    new_intervals = []
    length = interval[1] - interval[0]
    new_length = length * 3 / 9  # Нова довжина кожного з 9 підінтервалів
    for i in range(9):
        if i != 3 and i != 7:  # Пропускаємо 3-й та 7-й підінтервали
            new_intervals.append((interval[0] + i * new_length, interval[0] + (i + 1) * new_length))
    return new_intervals

def generate_fractal(interval, depth):
    # Базовий випадок: якщо досягнуто кінцеву глибину, повертаємо поточний відрізок
    if depth == 0:
        return [interval]

    # Видаляємо третю та сьому частину відрізка
    new_intervals = remove_third_seventh(interval)

    # Рекурсивно викликаємо функцію для кожного нового відрізка
    fractal_intervals = []
    for i in new_intervals:
        fractal_intervals.extend(generate_fractal(i, depth - 1))

    return fractal_intervals

def plot_fractal(fractal_intervals):
    # Відображення фрактала
    for interval in fractal_intervals:
        plt.plot([interval[0], interval[1]], [0, 0], color='black')

    # Налаштування відображення
    plt.title("Fractal з видаленням третини та сьомої частини")
    plt.xlabel("x")
    plt.ylabel("y")
    plt.ylim(-0.1, 0.1)
    plt.gca().axes.yaxis.set_ticks([])  # Приховуємо вісь Y
    plt.show()

if __name__ == "__main__":
    initial_interval = (0, 1)
    fractal_intervals = generate_fractal(initial_interval, 1)  # Глибина рекурсії 5
    print(fractal_intervals)