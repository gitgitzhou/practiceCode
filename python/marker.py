#!/usr/bin/env python

from scipy.stats import norm
import numpy as np
import matplotlib.pyplot as plt
import sys


def create_marker_function(x0, y0, angle_x, angle_y):
    @np.vectorize
    def marker_f(x, y):
        def f(x):
            k = np.tan(angle_x * np.pi / 180)
            return k*(x-x0) + y0

        def h(y):
            k = np.tan(angle_y * np.pi / 180)
            return k*(y-y0) + x0

        return (1 - 2*norm.cdf(x, loc=h(y), scale=0.5)) * \
            (1 - 2*norm.cdf(y, loc=f(x), scale=0.5))
    return marker_f


center = np.array([10.3, 9.7])
angle_x, angle_y = 25, -17
size = 20
marker_f = create_marker_function(center[0], center[1], angle_x, angle_y)
xv, yv = np.meshgrid(np.arange(size), np.arange(size))
im = marker_f(xv, yv)

plt.imshow(im, interpolation='none', cmap='gray')
x, y = center
plt.plot(x, y, 'ro')
plt.show()


def jianfeng_ultimate_marker_finder(im, initial_guess):
    # Does awesome stuff
    return center


jian_center = jianfeng_ultimate_marker_finder(im, np.array([10, 10]))

print(jian_center - center)
