# import numpy as np
# import matplotlib.pyplot as plt

# check = np.zeros((9, 9))
# check[::2, 1::2] = 1
# check[1::2, ::2] = 1

# plt.imshow(check, cmap='gray', interpolation='nearest')
# plt.show()

import matplotlib.pyplot as plt
from skimage import data

camera = data.camera()
camera_multiply = 3 * camera

plt.figure(figsize=(8, 4))
plt.subplot(121)
plt.imshow(camera, cmap='gray', interpolation='nearest')
plt.axis('off')
plt.subplot(122)
plt.imshow(camera_multiply, cmap='gray', interpolation='nearest')
plt.axis('off')

plt.tight_layout()
plt.show()
print ''
