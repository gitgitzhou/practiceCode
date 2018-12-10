def add_a_book(func):
    def new_func():
        return func() + "Python Cookbook"
    return new_func

@add_a_book
def read_a_book():
     return "I am reading the book: "

print
print
print
print
print

# def read_a_book():
#     return "I am reading the book: "
# read_a_book = add_a_book(read_a_book)

print read_a_book()
