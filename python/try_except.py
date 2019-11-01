#!/usr/bin/python


# try:
#     fh = open("testfile", "r")
#     fh.write("This is my test file for exception handling!!")
# except IOError:
#     print "some problem here: maybe I can\'t find file or read data"
# else:
#     print "Written content in the file successfully"
#     fh.close()
# print "\nbut i am continuing my program!"

# try:
#     fh = open("testfile", "r")
#     fh.write("This is my test file for exception handling!!")
# finally:
#     print "Error: can\'t find file or read data"


class MyError(Exception):

    def __init__(self, msg):
        self.msg = msg


try:
    a = 3
    if a < 5:
        # raise Exception('a cannot be less than 5!')
        # raise(MyError('a cannot be less than 5!'))
        raise MyError("a cannot be less than 5!")

except MyError as error:
    print("a new exception occured: %s" % error.msg)


print "\nbut i am continuing my program!"
