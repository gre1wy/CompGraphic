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
    def plot(self, ax):
        ax.plot(self.points[:, 0], self.points[:, 1], self.points[:, 2], label='Line')

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

# 4. Задати пряму як у прикладі 1 даної лабораторної роботи. Здійснити поворот
# куба відносно прямої на деякий кут φ. Вказати перетворення, які необхідні
# для одержання такого результату.

# Точка, напрям. вектор, генерація точок лінії

point_on_line = np.array([1, 2, 3])
direction_vector = np.array([2, 1, 3])

l, m, n = direction_vector[0], direction_vector[1], direction_vector[2]
a, b, c = point_on_line[0], point_on_line[1], point_on_line[2]

cos_phi = n/((n**2+m**2)**0.5)
sin_phi = m/((n**2+m**2)**0.5)

line_points = np.array([point_on_line + t * direction_vector for t in np.linspace(-8, 8, 100)])
line_points = np.hstack([line_points, np.ones((line_points.shape[0], 1))])

# Moving matrices
matrix_move_to_center = np.array([[ 1, 0, 0, -a],
                            [ 0, 1, 0, -b],
                            [ 0, 0, 1, -c],
                            [ 0, 0, 0, 1]])

matrix_2 = np.array([[ 1, 0, 0, 0,],
                    [ 0, cos_phi, sin_phi, 0],
                    [ 0, -sin_phi, cos_phi, 0],
                    [ 0, 0, 0, 1]])



direction_vector_with_one = np.array([2, 1, 3, 1])

# Multiplication
line_points_to_center = np.dot(line_points, matrix_move_to_center.T)
c_moved_to_center = np.dot(cube_vertices_with_ones, matrix_move_to_center.T)

v_moved_to_center = np.dot(direction_vector_with_one, matrix_move_to_center.T)

line_moved_2 = np.dot(line_points_to_center, matrix_2.T)
c_moved_2 = np.dot(c_moved_to_center, matrix_2.T)

v_moved_2 = np.dot(v_moved_to_center, matrix_2.T)
l,d = v_moved_2[0], v_moved_2[2]

matrix_3 = np.array([[ l, 0, d, 0,],
                    [ 0, 1, 0, 0],
                    [ -d, 0, l, 0],
                    [ 0, 0, 0, 1]])
matrix_4 = np.array([[ cos_phi, -sin_phi, 0, 0,],
                    [ sin_phi, cos_phi, 0, 0],
                    [ d, 0, 1, 0],
                    [ 0, 0, 0, 1]])
matrix_5 = matrix_3.T
matrix_6 = np.array([[ 1, 0, 0, 0,],
                    [ 0, cos_phi, -sin_phi, 0],
                    [ 0, sin_phi, cos_phi, 0],
                    [ 0, 0, 0, 1]])
matrix_7 = np.array([[ 1, 0, 0, a],
                     [ 0, 1, 0, b],
                     [ 0, 0, 1, c],
                     [ 0, 0, 0, 1]])

line_moved_3 = np.dot(line_moved_2, matrix_3.T)
c_moved_3 = np.dot(c_moved_2, matrix_3.T)

line_moved_4 = np.dot(line_moved_3, matrix_4.T)
c_moved_4 = np.dot(c_moved_3, matrix_4.T)

line_moved_5 = np.dot(line_moved_4, matrix_5.T)
c_moved_5 = np.dot(c_moved_4, matrix_5.T)

line_moved_6 = np.dot(line_moved_5, matrix_6.T)
c_moved_6 = np.dot(c_moved_5, matrix_6.T)

line_moved_7 = np.dot(line_moved_6, matrix_7.T)
c_moved_7 = np.dot(c_moved_6, matrix_7.T)

# Building
line = Line(line_points)
cube = Cube(cube_vertices_with_ones)

line_res = Line(line_moved_7)
cube_res = Cube(c_moved_7)

# Visualition
fig2 = plt.figure()
ax = fig2.add_subplot(111, projection='3d')

cube.plot(ax)
line.plot(ax)

line_res.plot(ax)
cube_res.plot(ax)

# plt.legend()
plt.show()


