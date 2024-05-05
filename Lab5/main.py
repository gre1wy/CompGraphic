import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from scipy import interpolate
import numpy as np

xs = [0.15, 0.35, 0.5, 0.67, 0.8]
ys = [0.01,0.01, 0.01, 0.01, 0.01]
z = [0.75, 0.83, 1.00, 0.92, 0.91]

tck = interpolate.bisplrep(xs, ys, z, s=0)
def givemeZ(x,y):
    return interpolate.bisplev(x,y,tck)
print(givemeZ(0.3,0.5))