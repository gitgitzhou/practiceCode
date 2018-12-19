class Mammal(object):
    def __init__(self, mammalName):
        print(mammalName, 'is a warm-blooded animal.')


class Dog(Mammal):
    def __init__(self):
        print('Dog has four legs.')

        super(Dog, self).__init__('Dog')

    def adding(self, x, y):
        return x+y


def myprint(architecture):
    # rc is the object of class architecture(Dog)
    rc = architecture()
    print rc.adding(3, 5)
    print 'yes'


def myprint2(architecture):
    print architecture.adding(3, 5)
    print 'yes'


myprint(Dog)

print ''

d1 = Dog()
myprint2(d1)
