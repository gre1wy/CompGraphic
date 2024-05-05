import numpy as np
import cv2
from RLE import *

image_name = "CompGraphic/project/Images/binary_image.jpg"
image_input = cv2.imread(image_name)
image_array = np.array(image_input)

test_image = np.array([[0,1,1,1,1,1,0,1],
                       [1,0,1,1,0,1,1,1],
                       [1,1,1,1,0,0,1,1],
                       [1,0,0,0,1,1,1,1],
                       [1,0,1,1,0,1,1,0],
                       [1,1,0,1,1,1,1,1],
                       [0,1,1,0,1,1,0,1],
                       [1,0,1,1,1,1,1,0]])

test_image_rgb = np.array([[[3, 5, 6], [3, 5, 1], [1, 1, 1], [1, 1, 1], [1, 1, 1], [1, 1, 1], [0, 0, 0], [1, 1, 1]],
                           [[1, 1, 1], [1, 4, 0], [1, 1, 1], [1, 1, 1], [0, 0, 0], [1, 1, 1], [1, 1, 1], [1, 1, 1]],
                           [[1, 1, 1], [1, 1, 1], [1, 1, 1], [1, 43, 1], [0, 39, 0], [0, 0, 0], [1, 1, 1], [1, 1, 1]],
                           [[1, 1, 1], [0, 0, 0], [0, 0, 0], [0, 0, 0], [1, 1, 1], [1, 1, 1], [1, 1, 1], [1, 1, 1]],
                           [[1, 1, 32], [0, 5, 0], [1, 9, 1], [1, 1, 1], [0, 0, 0], [1, 1, 1], [1, 1, 1], [0, 0, 0]],
                           [[1, 1, 1], [1, 1, 1], [0, 0, 0], [1, 24, 1], [1, 1, 1], [1, 1, 1], [1, 1, 1], [1, 1, 1]],
                           [[0, 0, 0], [1, 1, 1], [1, 1, 1], [0, 0, 0], [1, 1, 1], [1, 1, 1], [0, 0, 0], [1, 1, 1]],
                           [[1, 1, 1], [0, 0, 0], [1, 1, 1], [1, 1, 1], [1, 1, 1], [1, 1, 1], [1, 1, 1], [0, 0, 0]]])


f1 = rle_compress_rgb(test_image_rgb)
f2 = rle_decompress_rgb(f1)
print(f1)
print(np.array_equal(f2, test_image_rgb))

# compressed_data = rle_compress(test_image)
# print(compressed_data)
# decompressed_data = rle_decompress(compressed_data)
# print(decompressed_data)
# print(np.array_equal(decompressed_data, test_image))

# f1 = rle_compress_rgb(image_array)
# f2 = rle_decompress_rgb(f1)
# print(np.array_equal(f2, image_array))
# print(f1.shape)
# print(f1)