import numpy as np

a = np.array([[3,1,4], [1,2,4], [2,5,5]])
b = np.array([9,8,6])
x = np.linalg.solve(a, b)

print a
print b
print x

print np.allclose(np.dot(a, x), b)
