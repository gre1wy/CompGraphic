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

def angle_between_planes(norm_vector):
    # Нормалізуємо вектор
    n = norm_vector / np.linalg.norm(norm_vector)
    
    # Нормалізований вектор до площини z
    z_normal = np.array([0, 0, 1])
    
    # Знаходимо косинус кута
    cos_theta = np.dot(n, z_normal) / (np.linalg.norm(n) * np.linalg.norm(z_normal))
    
    # Знаходимо кут в радіанах
    theta_rad = np.arccos(cos_theta)
    
    return theta_rad
angle = angle_between_planes(normal_vector)
# Matrices
M1_plane_to_Z_x = np.array([[1,0,0,0],
                          [0, np.cos(angle), np.sin(angle), 0],
                          [0,-np.sin(angle), np.cos(angle), 0],
                          [0,0,0,1]])

M1_plane_to_Z_y = np.array([[np.cos(angle),0,np.sin(angle),0],
                          [0, 1, 0, 0],
                          [-np.sin(angle),0,np.cos(angle), 0],
                          [0,0,0,1]])

M1_plane_to_Z_z = np.array([[np.cos(angle),np.sin(angle),0,0],
                          [-np.sin(angle), np.cos(angle), 0, 0],
                          [0,0, 1, 0],
                          [0,0,0,1]])



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

# Створення візуалізації
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Куб
cube = Cube(cube_vertices_with_ones)
cube.plot(ax)

vertices = [corner1, corner2, corner4, corner3, corner1]
vertices = [np.append(arr, 1) for arr in vertices]

# flat_moved_x = np.dot(vertices, M1_plane_to_Z_x.T)
flat_moved_y = np.dot(vertices, M1_plane_to_Z_y.T)
cube_moved_y = np.dot(cube_vertices_with_ones, M1_plane_to_Z_y.T)
cube2 = Cube(cube_moved_y)
# cube2.plot(ax)
# flat_moved_z = np.dot(vertices, M1_plane_to_Z_z.T)

z1 = flat_moved_y[0,2]
M2 = np.array([[1,0,0,0],
                [0, 1, 0, 0],
                [0,0, 1, -z1],
                [0,0,0,1]])

flat_moved_to_z0 = np.dot(flat_moved_y, M2.T)
cube_moved_to_z0 = np.dot(cube_moved_y, M2.T)
cube3 = Cube(cube_moved_to_z0)
# cube3.plot(ax)

M3_main = np.array([[1,0,0,0],
                [0, 1, 0, 0],
                [0,0, 0, 0],
                [0,0,0,1]])
cube_main = np.dot(cube_moved_to_z0, M3_main.T)
cube4 = Cube(cube_main)
# cube4.plot(ax)

M4 = np.array([[1,0,0,0],
                [0, 1, 0, 0],
                [0,0, 1, z1],
                [0,0,0,1]])

flat_moved_from_z0 = np.dot(flat_moved_to_z0, M4.T)
cube_moved_from_z0 = np.dot(cube_main, M4.T)
cube5 = Cube(cube_moved_from_z0)
# cube5.plot(ax)

M5 = M1_plane_to_Z_y.T

flat_final = np.dot(flat_moved_from_z0, M5.T)
cube_final = np.dot(cube_moved_from_z0, M5.T)
cube6 = Cube(cube_final)
cube6.plot(ax)

flat = Poly3DCollection([[arr[:-1] for arr in vertices]], alpha=0.5, facecolors='cyan', edgecolors='red')
ax.add_collection3d(flat)

# flat_1 = Poly3DCollection([[arr[:-1] for arr in flat_moved_x]], alpha=0.5, facecolors='cyan', edgecolors='yellow')
# ax.add_collection3d(flat_1)
# flat_2 = Poly3DCollection([[arr[:-1] for arr in flat_moved_y]], alpha=0.5, facecolors='cyan', edgecolors='black')
# ax.add_collection3d(flat_2)
# flat_3 = Poly3DCollection([[arr[:-1] for arr in flat_moved_z]], alpha=0.5, facecolors='cyan', edgecolors='blue')
# ax.add_collection3d(flat_3)

# flat_3 = Poly3DCollection([[arr[:-1] for arr in flat_moved_to_z0]], alpha=0.5, facecolors='cyan', edgecolors='black')
# ax.add_collection3d(flat_3)

# flat_3 = Poly3DCollection([[arr[:-1] for arr in flat_moved_to_z0]], alpha=0.5, facecolors='cyan', edgecolors='black')
# ax.add_collection3d(flat_3)

flat_6 = Poly3DCollection([[arr[:-1] for arr in flat_final]], alpha=0.5, facecolors='cyan', edgecolors='black')
ax.add_collection3d(flat_6)
plt.show()