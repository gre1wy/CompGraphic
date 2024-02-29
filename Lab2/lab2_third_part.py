import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d.art3d import Poly3DCollection
from lab2 import Cube, Line

# Три точки на площині прямокутника
point1 = np.array([1, 2, 3])
point2 = np.array([4, 3, 5])
point3 = np.array([1, 5, 3])
x1,y1,z1 = point1[0],point1[1],point1[2]
x2,y2,z2 = point2[0],point2[1],point2[2]
x3,y3,z3 = point3[0],point3[1],point3[2]
# Розрахунки

A = np.linalg.det([[y2-y1,z2-z1],
                   [y3-y1,z3-z1]])
B = -np.linalg.det([[x2-x1,z2-z1],
                   [x3-x1,z3-z1]])
C = np.linalg.det([[x2-x1,y2-y1],
                   [x3-x1,y3-y1]])
D = -x1*A-y1*B-z1*C

# Створення векторів на площині
vector1 = point2 - point1
vector2 = point3 - point1

# Нормаль (перпендикулярний вектор до площини)
normal_vector = np.cross(vector1, vector2)
triple_sqrt = (A**2+B**2+C**2)**0.5
n_vector = np.array([A/triple_sqrt, B/triple_sqrt, C/triple_sqrt])

# Розрахунок координат для площини
corner1 = point1
corner2 = point1 + vector1
corner3 = point1 + vector2
corner4 = point1 + vector1 + vector2

# Cube
cube_vertices = np.array([
    [4, 6, 2],
    [6, 6, 2],
    [6, 8, 2],
    [4, 8, 2],
    [4, 6, 4],
    [6, 6, 4],
    [6, 8, 4],
    [4, 8, 4]])

cube_vertices_with_ones = np.hstack([cube_vertices, np.ones((cube_vertices.shape[0], 1))])

# Матриці
double_sqrt = (A**2+B**2)**0.5
M1 = np.array([[1,0,0,0],
               [0,1,0,0],
               [0,0,1,D/C],
               [0,0,0,1]])
M2 = np.array([[A/double_sqrt, B/double_sqrt, 0,0],
               [-B/double_sqrt, A/double_sqrt, 0,0],
               [0,0,1,0],
               [0,0,0,1]])
M3 = np.array([[C/triple_sqrt, 0, -double_sqrt/triple_sqrt,0],
               [0, 1, 0,0],
               [double_sqrt/triple_sqrt,0,C/triple_sqrt,0],
               [0,0,0,1]])
M4 = np.array([[1,0,0,0],
               [0,1,0,0],
               [0,0,-1,0],
               [0,0,0,1]])
M5 = M3.T
M6 = M2.T
M7 = np.array([[1,0,0,0],[0,1,0,0],[0,0,1,-D/C],[0,0,0,1]])

# Створення візуалізації
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Визначення вершин куба
cube_moved_1 = np.dot(cube_vertices_with_ones, M1.T)
cube_moved_2 = np.dot(cube_moved_1, M2.T)
cube_moved_3 = np.dot(cube_moved_2, M3.T)
cube_moved_4 = np.dot(cube_moved_3, M4.T)
cube_moved_5 = np.dot(cube_moved_4, M5.T)
cube_moved_6 = np.dot(cube_moved_5, M6.T)
cube_moved_7 = np.dot(cube_moved_6, M7.T)

# Куби
cube = Cube(cube_vertices_with_ones)
cube_1 = Cube(cube_moved_1)
cube_2 = Cube(cube_moved_2)
cube_3 = Cube(cube_moved_3)
cube_4 = Cube(cube_moved_4)
cube_5 = Cube(cube_moved_5)
cube_6 = Cube(cube_moved_6)
cube_7 = Cube(cube_moved_7)

# Зображення кубів
cube.plot(ax)
cube_7.plot(ax)

# Визначення вершин прямокутника
vertices = [corner1, corner2, corner4, corner3, corner1]
vertices = [np.append(arr, 1) for arr in vertices]
flat_moved_1 = np.dot(vertices, M1.T)
flat_moved_2 = np.dot(flat_moved_1, M2.T)
flat_moved_3 = np.dot(flat_moved_2, M3.T)
flat_moved_4 = np.dot(flat_moved_3, M4.T)
flat_moved_5 = np.dot(flat_moved_4, M5.T)
flat_moved_6 = np.dot(flat_moved_5, M6.T)
flat_moved_7 = np.dot(flat_moved_6, M7.T)

# Додавання оригінальної площини
flat = Poly3DCollection([[arr[:-1] for arr in vertices]], alpha=0.5, facecolors='cyan', edgecolors='r')
ax.add_collection3d(flat)

# Додавання фінальної площини
flat_7 = Poly3DCollection([[arr[:-1] for arr in flat_moved_7]], alpha=0.5, facecolors='cyan', edgecolors='yellow')
ax.add_collection3d(flat_7)


# Проміжні стадії

# flat_1 = Poly3DCollection([[arr[:-1] for arr in flat_moved_1]], alpha=0.5, facecolors='cyan', edgecolors='yellow')
# flat_2 = Poly3DCollection([[arr[:-1] for arr in flat_moved_2]], alpha=0.5, facecolors='cyan', edgecolors='yellow')
# flat_3 = Poly3DCollection([[arr[:-1] for arr in flat_moved_3]], alpha=0.5, facecolors='cyan', edgecolors='yellow')
# flat_4 = Poly3DCollection([[arr[:-1] for arr in flat_moved_4]], alpha=0.5, facecolors='cyan', edgecolors='yellow')
# flat_5 = Poly3DCollection([[arr[:-1] for arr in flat_moved_5]], alpha=0.5, facecolors='cyan', edgecolors='yellow')
# flat_6 = Poly3DCollection([[arr[:-1] for arr in flat_moved_6]], alpha=0.5, facecolors='cyan', edgecolors='yellow')

# ax.add_collection3d(flat_1)
# ax.add_collection3d(flat_2)
# ax.add_collection3d(flat_3)
# ax.add_collection3d(flat_4)
# ax.add_collection3d(flat_5)
# ax.add_collection3d(flat_6)

plt.show()