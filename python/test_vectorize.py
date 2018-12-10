import numpy as np

@np.vectorize
def myfunc(a, b):
    "Return a-b if a>b, otherwise return a+b"
    if a > b:
        return a - b
    else:
       return a + b

print myfunc(10, 8)


# vfunc = np.vectorize(myfunc)
# print vfunc([1, 2, 3, 4], 2)

print myfunc(3, [2, 1])
