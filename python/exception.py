# syntax error
# print(0/0))


# exception error
# print(0/0)


# rasing an Exception
# x = 10
# if x > 5:
#     raise Exception('x cannot exceed 5!')

# the AssertionError Exception
# and built-in exception


import sys
try:
    assert('linux' in sys.platform), 'this code runs on linux'
except AssertionError as error:
    print(error)
else:
    try:
        with open('file.log') as file:
            read_data = file.read()
            print ('printing file:\n{}').format(read_data)
    except IOError as error:
        print(error)
    else:
        try:
            print(0/0)
        except ZeroDivisionError as error:
            print(error)
finally:
    print('failed')
