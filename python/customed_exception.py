#Python user-defined exceptions
class CustomException(Exception):
# """Base class for other exceptions"""
    pass
class PrecedingLetterError(CustomException):
# """Raised when the entered alphabet is smaller than the actual one"""
    pass
class SucceedingLetterError(CustomException):
# """Raised when the entered alphabet is larger than the actual one"""
    pass
# we need to guess this alphabet till we get it right
alphabet = 'k'

while True:
    try:
        foo = raw_input ( "Enter an alphabet: " )
        if foo < alphabet:
            raise PrecedingLetterError
        elif foo > alphabet:
            raise SucceedingLetterError
        break
    except PrecedingLetterError:
        print("The entered alphabet is preceding one, try again!")
        print('')
    except SucceedingLetterError:
        print("The entered alphabet is succeeding one, try again!")
        print('')
print("Congratulations! You guessed it correctly.")
