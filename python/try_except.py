#!/usr/bin/python

try:
    fh = open("testfile", "r")
    fh.write("This is my test file for exception handling!!")
except IOError:
    print "some problem here: maybe I can\'t find file or read data"
else:
    print "Written content in the file successfully"
    fh.close()

# try:
#     fh = open("testfile", "r")
#     fh.write("This is my test file for exception handling!!")
# finally:
#     print "Error: can\'t find file or read data"

print "\nbut i am continuing my program!"
