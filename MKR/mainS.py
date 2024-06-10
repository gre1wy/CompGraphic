import matplotlib.pyplot as plt
import numpy as np

def is_point_in_fractal(x):
    x_str = str(x).split('.')[1]  # Десяткова частина
    if '3' in x_str or '7' in x_str:
        return False
    return True

def box_counting(N):

    boxes = np.linspace(0, 1, N+1)  # Розбиття відрізка на N ящиків
    count = 0
    for i in range(N):
        box_min, box_max = boxes[i], boxes[i+1]
        for x in np.linspace(box_min, box_max, 1000):  # Перевірка 1000 точок в ящику
            if is_point_in_fractal(x):
                count += 1
                break  # Якщо знайдено точку фрактала, переходимо до наступного ящика
    return count

# Побудова фрактала
fig, ax = plt.subplots(figsize=(8, 8))
x = np.linspace(0, 1, 10000)
y = np.zeros_like(x)
for i in range(len(x)):
    if is_point_in_fractal(x[i]):
        y[i] = 0.1  # Візуалізація точок фрактала

ax.scatter(x, y, s=1, c='k')
ax.set_xlim(0, 1)
ax.set_ylim(-0.1, 0.2)
ax.set_title('Фрактал')
plt.show()

# Обчислення фрактальної розмірності
N_values = [10**i for i in range(1, 5)]  # Різні значення N
log_N = np.log(N_values)
log_count = [np.log(box_counting(N)) for N in N_values]

# Знаходження нахилу прямої за методом найменших квадратів
coeffs = np.polyfit(log_N, log_count, 1)
fractal_dim = -coeffs[0]

print(f'Фрактальна розмірність: {fractal_dim:.2f}')