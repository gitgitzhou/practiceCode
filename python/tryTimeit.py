import timeit

mysetup = "from math import sqrt"

mycode = '''
def example():
    mylist = []
    for x in range(10000):
        mylist.append(sqrt(x))
'''

print timeit.timeit(setup=mysetup, stmt=mycode, number=10000)
