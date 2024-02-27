import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d.art3d import Poly3DCollection

class Cube:
    def __init__(self, vertices):
        self.vertices = vertices

    def plot(self, ax):
        # З'єднуємо вершини для створення граней куба
        edges = np.array([
            [self.vertices[0,:-1], self.vertices[1,:-1], self.vertices[2,:-1], self.vertices[3,:-1]],
            [self.vertices[4,:-1], self.vertices[5,:-1], self.vertices[6,:-1], self.vertices[7,:-1]],
            [self.vertices[0,:-1], self.vertices[1,:-1], self.vertices[5,:-1], self.vertices[4,:-1]],
            [self.vertices[2,:-1], self.vertices[3,:-1], self.vertices[7,:-1], self.vertices[6,:-1]],
            [self.vertices[1,:-1], self.vertices[2,:-1], self.vertices[6,:-1], self.vertices[5,:-1]],
            [self.vertices[0,:-1], self.vertices[3,:-1], self.vertices[7,:-1], self.vertices[4,:-1]]
        ])

        # Відображення осей координат
        ax.quiver(0, 0, 0, 10, 0, 0, color='k', label='X-axis')
        ax.quiver(0, 0, 0, 0, 10, 0, color='k', label='Y-axis')
        ax.quiver(0, 0, 0, 0, 0, 10, color='k', label='Z-axis')

        # Відображення кожної грани окремо
        for i in range(len(edges)):
            ax.add_collection3d(Poly3DCollection([edges[i]], facecolors='cyan', linewidths=1, edgecolors='r', alpha=0))

        ax.set_xlabel('X')
        ax.set_ylabel('Y')
        ax.set_zlabel('Z')

        # Задаємо діапазон значень та позначки на вісях
        ax.set_xlim([-8, 8])
        ax.set_ylim([-8, 8])
        ax.set_zlim([-8, 8])

class Line:
    def __init__(self, points):
        self.points = points
    def plot(self, ax, label, color):
        ax.plot(self.points[:, 0], self.points[:, 1], self.points[:, 2], label=label, color = color)
        # Це треба видалити
        ax.quiver(0, 0, 0, 10, 0, 0, color='k', label='X-axis')
        ax.quiver(0, 0, 0, 0, 10, 0, color='k', label='Y-axis')
        ax.quiver(0, 0, 0, 0, 0, 10, color='k', label='Z-axis')

        ax.set_xlabel('X')
        ax.set_ylabel('Y')
        ax.set_zlabel('Z')

        ax.set_xlim([-8, 8])
        ax.set_ylim([-8, 8])
        ax.set_zlim([-8, 8])

# Задаємо координати вершин куба
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

# 2. Задати куб через його вершини. Здійснити масштабування куба (збільшення,
# зменшення у кілька разів). Записати відповідну матрицю.
# 3. Отриманий результат з попереднього пункту симетрично відобразити
# відносно початку координат, відносно однієї з координатних площин у
# тривимірній декартовій системі координат (простір).

matrix_increment = np.array([[1.5,   0,   0, 0],
                             [  0, 1.5,   0, 0],
                             [  0,   0, 1.5, 0],
                             [  0,   0,   0, 1]])
matrix_decrease = np.array([[0.5,   0,   0, 0],
                            [  0, 0.5,   0, 0],
                            [  0,   0, 0.5, 0],
                            [  0,   0,   0, 1]])
matrix_sym_start_coord = np.array([[  -1,  0,  0, 0],
                                    [  0, -1,  0, 0],
                                    [  0,  0, -1, 0],
                                    [  0,  0,  0, 1]])
matrix_sym_one_coord_plane = np.array([[  1,  0,  0, 0],
                                    [  0, -1,  0, 0],
                                    [  0,  0, 1, 0],
                                    [  0,  0,  0, 1]])

cube_increment = np.dot(cube_vertices_with_ones, matrix_increment.T)
cube_decrease = np.dot(cube_vertices_with_ones, matrix_decrease.T)
cube_sym_start_coord = np.dot(cube_vertices_with_ones, matrix_sym_start_coord.T)
cube_sym_one_coord_plane = np.dot(cube_vertices_with_ones, matrix_sym_one_coord_plane.T)

# Створюємо об'єкти кубів
my_cube = Cube(cube_vertices_with_ones)
cube_scalled_1 = Cube(cube_increment)
cube_scalled_2 = Cube(cube_decrease)
cube_sym_1 = Cube(cube_sym_start_coord)
cube_sym_2 = Cube(cube_sym_one_coord_plane)

# Виводимо куби на одному графіку
# fig = plt.figure()
# ax = fig.add_subplot(111, projection='3d')
# my_cube.plot(ax)
# cube_scalled_1.plot(ax)
# cube_scalled_2.plot(ax)
# cube_sym_1.plot(ax)
# cube_sym_2.plot(ax)

# plt.show()



