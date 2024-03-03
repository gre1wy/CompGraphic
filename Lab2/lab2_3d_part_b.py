import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d.art3d import Poly3DCollection
from lab2_1st_part import Cube
from sympy import symbols, Eq, solve

# Three points
point1 = np.array([1, 2, 3])
point2 = np.array([4, 3, 5])
point3 = np.array([1, 5, 3])

#Coordinates of points
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

# Original cube
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

# Geometric calculations
# A*x+B*y+C*z+D=0
# (x-p1[0])/A = (y-p1[1])/B = (z-p1[2])/C = t
# x = A*t+p1[0], y = B*t+p1[1],  z = C*t+p1[2]
# A*(A*t+p1[0])+B*(B*t+p1[1])+C*(C*t+p1[2])+D=0
# t = h
# x = A*h+p1[0], y = B*h+p1[1],  z = C*h+p1[2] coordinates of symmetric point

# vertices of symmetric cube
sym_cube = []

for vertex in cube_vertices:
    t = symbols('t')

    x, y, z = vertex[0], vertex[1], vertex[2]

    equation = Eq(A * (A * t + x) + B * (B * t + y) + C * (C * t + z) + D, 0)
    solution = solve(equation, t)

    x_o, y_o, z_o = A*solution[0]+x, B*solution[0]+y, C*solution[0]+z

    x_sym, y_sym, z_sym = 2*x_o-x, 2*y_o-y, 2*z_o-z

    point = [x_sym, y_sym, z_sym]
    sym_cube.append(point)

# Add ones to sym_cube
sym_cube = np.array(sym_cube)
sym_cube = np.hstack([sym_cube, np.ones((sym_cube.shape[0], 1))])

# Building cubes
cube_original = Cube(cube_vertices_with_ones)
cube_symmetric = Cube(sym_cube)

# Visualistion
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Visualization of original cube
cube_original.plot(ax, color='red', label='Original')

# Visualization of final cube
cube_symmetric.plot(ax, color='green', label='Symmetric to plane')

# Vertices of plane 
vertices = [corner1, corner2, corner4, corner3, corner1]
vertices = [np.append(arr, 1) for arr in vertices]

# Visualization of original plane
plane = Poly3DCollection([[arr[:-1] for arr in vertices]], alpha=0.5, facecolors='cyan', edgecolors='r')
ax.add_collection3d(plane)

plt.show()