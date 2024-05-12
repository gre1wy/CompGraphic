import cv2
import numpy as np
import matplotlib.pyplot as plt
wm_image = cv2.imread('CompGraphic\Lab6\Images\WM.png', cv2.IMREAD_GRAYSCALE)
input_image = cv2.imread('CompGraphic\Lab6\Images\InputImage.png')
_, wm_binary = cv2.threshold(wm_image, 70, 255, cv2.THRESH_BINARY)
# plt.imshow(wm_binary)
histogram = cv2.calcHist([wm_binary], [0], None, [256], [0, 256])

# Отображение гистограммы
plt.figure(figsize=(8, 6))
plt.plot(histogram, color='black')
plt.title('Histogram of the Image')
plt.xlabel('Pixel Intensity')
plt.ylabel('Frequency')
plt.show()
