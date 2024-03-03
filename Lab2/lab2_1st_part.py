import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d.art3d import Poly3DCollection, Line3DCollection


class Cube:
    def __init__(self, vertices):
        self.vertices = vertices

    def plot(self, ax, color = 'r', label = 'cube'):
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
        ax.quiver(-8, 0, 0, 16, 0, 0, color='k', label='_X-axis')
        ax.quiver(0, -8, 0, 0, 16, 0, color='k', label='_Y-axis')
        ax.quiver(0, 0, -8, 0, 0, 16, color='k', label='_Z-axis')

        # Відображення
        poly3d = Poly3DCollection(edges, facecolors='cyan', linewidths=1, edgecolors=color, alpha=0)
        ax.add_collection3d(poly3d)

        ax.add_collection3d(Line3DCollection([], colors=color, linewidths=1, label=label))

        ax.set_xlabel('X')
        ax.set_ylabel('Y')
        ax.set_zlabel('Z')

        ax.set_xlim([-8, 8])
        ax.set_ylim([-8, 8])
        ax.set_zlim([-8, 8])

class Line:
    def __init__(self, points):
        self.points = points

    def plot(self, ax, label, color):
        ax.plot(self.points[:, 0], self.points[:, 1], self.points[:, 2], label = '_'+label, color = color)

        # Відображення осей координат
        ax.quiver(-8, 0, 0, 16, 0, 0, color='k', label='_X-axis')
        ax.quiver(0, -8, 0, 0, 16, 0, color='k', label='_Y-axis')
        ax.quiver(0, 0, -8, 0, 0, 16, color='k', label='_Z-axis')
        
        ax.set_xlabel('X')
        ax.set_ylabel('Y')
        ax.set_zlabel('Z')

        # Задаємо діапазон значень та позначки на вісях
        ax.set_xlim([-8, 8])
        ax.set_ylim([-8, 8])
        ax.set_zlim([-8, 8])

if __name__ == "__main__":
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

    center_x = np.mean(cube_vertices[:, 0])
    center_y = np.mean(cube_vertices[:, 1])
    center_z = np.mean(cube_vertices[:, 2])

    matrix_move_to_center = np.array([[1, 0, 0, -center_x],
                                [0, 1, 0, -center_y],
                                [0, 0, 1, -center_z],
                                [0, 0, 0, 1]])
    matrix_move_from_center = np.array([[1, 0, 0, center_x],
                                [0, 1, 0, center_y],
                                [0, 0, 1, center_z],
                                [0, 0, 0, 1]])
    matrix_increment = np.array([[1.5, 0, 0, 0],
                                [0, 1.5, 0, 0],
                                [0, 0, 1.5, 0],
                                [0, 0, 0, 1]])
    matrix_decrease = np.array([[0.5, 0, 0, 0],
                                [0, 0.5, 0, 0],
                                [0, 0, 0.5, 0],
                                [0, 0, 0, 1]])
    matrix_sym_start_coord = np.array([[-1, 0, 0, 0],
                                        [0, -1, 0, 0],
                                        [0, 0, -1, 0],
                                        [0, 0, 0, 1]])
    matrix_sym_one_coord_plane = np.array([[1, 0, 0, 0],
                                        [0, -1, 0, 0],
                                        [0, 0, 1, 0],
                                        [0, 0, 0, 1]])
    # Куб переміщений до центру
    cube_to_center = np.dot(cube_vertices_with_ones, matrix_move_to_center.T)
    # Куб збільшений в центрі
    cube_increment = np.dot(cube_to_center, matrix_increment.T)
    # Збільшений куб переміщений від центру
    cube_from_center_increment = np.dot(cube_increment, matrix_move_from_center.T)
    # Куб зменшений в центрі
    cube_decrease = np.dot(cube_to_center, matrix_decrease.T)
    # Зменшений куб переміщений від центру
    cube_from_center_decrease = np.dot(cube_decrease, matrix_move_from_center.T)
    # Куб симетричний до центру координат
    cube_sym_start_coord = np.dot(cube_vertices_with_ones, matrix_sym_start_coord.T)
    # Куб симетричний відносно однієї з координатних площин
    cube_sym_one_coord_plane = np.dot(cube_vertices_with_ones, matrix_sym_one_coord_plane.T)

    # Створюємо об'єкти кубів
    cube_original = Cube(cube_vertices_with_ones)
    cube_scaled_up = Cube(cube_from_center_increment)
    cube_scaled_down = Cube(cube_from_center_decrease)
    cube_sym_1 = Cube(cube_sym_start_coord)
    cube_sym_2 = Cube(cube_sym_one_coord_plane)

    # Виводимо куби на одному графіку
    fig = plt.figure(figsize=(8, 6))
    ax = fig.add_subplot(111, projection='3d')
    cube_original.plot(ax, label= 'Original', color='green')
    cube_scaled_up.plot(ax, label= 'Bigger', color = 'red')
    cube_scaled_down.plot(ax, label = 'Smaller', color = 'yellow')
    cube_sym_1.plot(ax, label = 'Sym to start coord', color='purple')
    cube_sym_2.plot(ax, label = 'Sym to coord plane', color='orange')
    plt.legend()
    plt.show()



