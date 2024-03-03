import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d.art3d import Poly3DCollection
from lab2_1st_part import Cube

# Three points
point1 = np.array([1, 2, 3])
point2 = np.array([4, 3, 5])
point3 = np.array([1, 5, 3])

# Coordinates of points
x1,y1,z1 = point1[0],point1[1],point1[2]
x2,y2,z2 = point2[0],point2[1],point2[2]
x3,y3,z3 = point3[0],point3[1],point3[2]

# Calculations
A = np.linalg.det([[y2-y1,z2-z1],
                   [y3-y1,z3-z1]])
B = -np.linalg.det([[x2-x1,z2-z1],
                   [x3-x1,z3-z1]])
C = np.linalg.det([[x2-x1,y2-y1],
                   [x3-x1,y3-y1]])
D = -x1*A-y1*B-z1*C

# Vectors on plane
vector1 = point2 - point1
vector2 = point3 - point1

# Normal vector to plane
normal_vector = np.cross(vector1, vector2)
triple_sqrt = (A**2+B**2+C**2)**0.5
n_vector = np.array([A/triple_sqrt, B/triple_sqrt, C/triple_sqrt])

# Coordinates of plane
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

vertices = [corner1, corner2, corner4, corner3, corner1]
vertices = [np.append(arr, 1) for arr in vertices]

# Rotate to make plane || Z
M1_plane_to_Z = np.array([[np.cos(angle),0,np.sin(angle),0],
                          [0, 1, 0, 0],
                          [-np.sin(angle),0,np.cos(angle), 0],
                          [0,0,0,1]])

plane_moved_y = np.dot(vertices, M1_plane_to_Z.T)
cube_moved_y = np.dot(cube_vertices_with_ones, M1_plane_to_Z.T)

# Distance to move
z1 = plane_moved_y[0][2]

# Move to Z=0 (XOY)
M2_moved_to_z0 = np.array([[1,0,0,0],
                [0, 1, 0, 0],
                [0,0, 1, -z1],
                [0,0,0,1]])

plane_moved_to_z0 = np.dot(plane_moved_y, M2_moved_to_z0.T)
cube_moved_to_z0 = np.dot(cube_moved_y, M2_moved_to_z0.T)

# Orthogonal projection to plane
M3_projection = np.array([[1,0,0,0],
                [0, 1, 0, 0],
                [0,0, 0, 0],
                [0,0,0,1]])

plane_projection = np.dot(plane_moved_to_z0, M3_projection.T)
cube_projection = np.dot(cube_moved_to_z0, M3_projection.T)

# Move from Z=0 (XOY)
M4_moved_from_z0 = np.array([[1,0,0,0],
                [0, 1, 0, 0],
                [0,0, 1, z1],
                [0,0,0,1]])

plane_moved_from_z0 = np.dot(plane_moved_to_z0, M4_moved_from_z0.T)
cube_moved_from_z0 = np.dot(cube_projection, M4_moved_from_z0.T)

# Rotate to make plane not || XOY
M5_plane_from_Z = M1_plane_to_Z.T

plane_final = np.dot(plane_moved_from_z0, M5_plane_from_Z.T)
cube_final = np.dot(cube_moved_from_z0, M5_plane_from_Z.T)

# Visualization
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Cubes visualization
cube_original = Cube(cube_vertices_with_ones)
cube_original.plot(ax, color='red', label='Original')

cube_projection_final = Cube(cube_final)
cube_projection_final.plot(ax, color='green', label='Orthogonal projection')

# Planes visualization
plane = Poly3DCollection([[arr[:-1] for arr in vertices]], alpha=0.5, facecolors='cyan', edgecolors='red')
ax.add_collection3d(plane)

plane_final = Poly3DCollection([[arr[:-1] for arr in plane_final]], alpha=0.5, facecolors='cyan', edgecolors='black')
ax.add_collection3d(plane_final)

plt.show()