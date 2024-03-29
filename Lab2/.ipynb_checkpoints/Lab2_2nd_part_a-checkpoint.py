import matplotlib.pyplot as plt
import math
import numpy as np
from lab2_1st_part import Cube, Line

# 4. Задати пряму як у прикладі 1 даної лабораторної роботи. Здійснити поворот
# куба відносно прямої на деякий кут φ. Вказати перетворення, які необхідні
# для одержання такого результату.

# Point and vector
point_on_line = np.array([1, 2, 3])
direction_vector = np.array([2, 1, 3])
direction_vector_with_one = np.array([2, 1, 3, 1])

# Unit vector 
magnitude = np.linalg.norm(direction_vector)
direction_vector = direction_vector / magnitude
direction_vector_with_one = np.append(direction_vector, 1)

# Some coordinates
l, m, n = direction_vector[0], direction_vector[1], direction_vector[2]
a, b, c = point_on_line[0], point_on_line[1], point_on_line[2]

# Find angle
cos_psi = n/math.sqrt((m**2+n**2))
sin_psi = m/math.sqrt((m**2+n**2))

# Building line
line_original = np.array([point_on_line + t * direction_vector for t in np.linspace(-8, 8, 100)])
line_original = np.hstack([line_original, np.ones((line_original.shape[0], 1))])

# Building cube
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


# Moving to center
matrix_move_to_center = np.array([[ 1, 0, 0, -a],
                            [ 0, 1, 0, -b],
                            [ 0, 0, 1, -c],
                            [ 0, 0, 0, 1]])

line_moved_to_center = np.dot(line_original, matrix_move_to_center.T)
cube_moved_to_center = np.dot(cube_vertices_with_ones, matrix_move_to_center.T)

# Rotate to XOZ
matrix_XOZ = np.array([[ 1, 0, 0, 0,],
                    [ 0, cos_psi, -sin_psi, 0],
                    [ 0, sin_psi, cos_psi, 0],
                    [ 0, 0, 0, 1]])

line_moved_XOZ = np.dot(line_moved_to_center, matrix_XOZ.T)
cube_moved_XOZ = np.dot(cube_moved_to_center, matrix_XOZ.T)

dir_vec_moved_to_XOZ = np.dot(direction_vector_with_one, matrix_XOZ.T)
l,d = dir_vec_moved_to_XOZ[0], dir_vec_moved_to_XOZ[2]

# Rotate to Z
matrix_Z = np.array([[ d, 0, -l, 0,],
                    [ 0, 1, 0, 0],
                    [ l, 0, d, 0],
                    [ 0, 0, 0, 1]])
line_rotate_to_Z = np.dot(line_moved_XOZ, matrix_Z.T)
cube_rotate_to_Z = np.dot(cube_moved_XOZ, matrix_Z.T)

# Rotate on given angle
phi = np.pi/2
cos_phi = np.cos(phi)
sin_phi = np.sin(phi)
matrix_phi = np.array([[ cos_phi, -sin_phi, 0, 0,],
                    [ sin_phi, cos_phi, 0, 0],
                    [ 0, 0, 1, 0],
                    [ 0, 0, 0, 1]])
line_rotate_phi = np.dot(line_rotate_to_Z, matrix_phi.T)
cube_rotate_phi = np.dot(cube_rotate_to_Z, matrix_phi.T)

# Rotate from Z
matrix_Z_rev = matrix_Z.T
line_rotate_from_Z = np.dot(line_rotate_phi, matrix_Z_rev.T)
cube_rotate_from_Z = np.dot(cube_rotate_phi, matrix_Z_rev.T)

# Rotate from XOZ
matrix_XOZ_rev = matrix_XOZ.T
line_moved_from_XOZ = np.dot(line_rotate_from_Z, matrix_XOZ_rev.T)
cube_moved_from_XOZ = np.dot(cube_rotate_from_Z, matrix_XOZ_rev.T)

# Moving to center
matrix_move_from_center = np.array([[ 1, 0, 0, a],
                            [ 0, 1, 0, b],
                            [ 0, 0, 1, c],
                            [ 0, 0, 0, 1]])

line_moved_from_center = np.dot(line_moved_from_XOZ, matrix_move_from_center.T)
cube_moved_from_center = np.dot(cube_moved_from_XOZ, matrix_move_from_center.T)


# Building lines
line_original = Line(line_original)

line_center = Line(line_moved_to_center)

line_XOZ = Line(line_moved_XOZ)

line_Z = Line(line_rotate_to_Z)

line_phi = Line(line_rotate_phi)

line_from_Z = Line(line_rotate_from_Z)

line_from_XOZ = Line(line_moved_from_XOZ)

line_from_center = Line(line_moved_from_center)

# Building cubes
cube_original = Cube(cube_vertices_with_ones)

cube_center = Cube(cube_moved_to_center)

cube_XOZ = Cube(cube_moved_XOZ)

cube_Z = Cube(cube_rotate_to_Z)

cube_phi = Cube(cube_rotate_phi)

cube_from_Z = Cube(cube_rotate_from_Z)

cube_from_XOZ = Cube(cube_moved_from_XOZ)

cube_from_center = Cube(cube_moved_from_center)

# Visualition
fig2 = plt.figure()
ax = fig2.add_subplot(111, projection='3d')

# Lines visualisation
line_original.plot(ax, label = "original", color = "#A60909")

# line_center.plot(ax, label = "moved_to_center", color = "#E17D0A")

# line_XOZ.plot(ax, label = line_XOZ", color = "#E2D737")

# line_Z.plot(ax, label = "Z", color = "#37E23D")

# line_phi.plot(ax, label = "Phi", color = "#37DCE2")

# line_from_Z.plot(ax, label = "from_Z", color = "#37E23D")

# line_from_XOZ.plot(ax, label = "from_XOZ", color = "#E2D737")

line_from_center.plot(ax, label = "from center", color = "#E2D737")

# Cubes visualisation
cube_original.plot(ax, color='red', label='original')

# cube_center.plot(ax, color='#CA671B', label='moved to center')

# cube_XOZ.plot(ax, color='#F0B234', label='moved to XOZ')

# cube_Z.plot(ax, color='#DCB515', label='moved to Z')

# cube_phi.plot(ax, color='#DCCF15', label='rotated')

# cube_from_Z.plot(ax, color='#B3FA39', label='moved from Z')

# cube_from_XOZ.plot(ax, color='#66FA39', label='moved from XOZ')

cube_from_center.plot(ax, color='#2A7911', label='rotated at angle')

plt.legend()
plt.show()
