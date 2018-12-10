#!/usr/bin/env python

class Myclass:


    i = 1234 # class variable

    def f(self):
        return 'Hello world'

    def __init__(self, N, H):
        self.name = N
        self.height = H
        self.weight = 20 # instance variable

    def test(self, A, B):
        print self.i  # class variable
        print self.weight # instance variable
        self.x = A
        self.y = B
        print A + B
        print self.x + self.y

    def add(self, X, Y):
        zz = X + Y
        return zz

class Bag:

    def __init__(self):
        self.data = []

    def add(self, x):
        self.data.append(x)

    def addtwice(self, x):
        self.add(x)
        self.add(x)

# V = Myclass('Kevin', 105)
# print V.i
# print ''

# b = V.f()
# print b
# print ''

# print V.name
# print V.height
# print V.weight
# print ''

# V.test(3, 5)
# print ''

# ZZ = V.add(3, 5)
# print ZZ

mybag = Bag()
print mybag.data

mybag.add('pen')
print mybag.data

mybag.addtwice('book')
print mybag.data

yourbag = Bag()
print yourbag.data

yourbag.add('pen')
print yourbag.data

yourbag.addtwice('apple')
print yourbag.data


