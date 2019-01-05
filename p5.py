# cons(a, b) constructs a pair, and car(pair) and cdr(pair) returns the first and last element of that pair. For example, car(cons(3, 4)) returns 3, and cdr(cons(3, 4)) returns 4.
#
# Given this implementation of cons:
#
# def cons(a, b):
#     def pair(f):
#         return f(a, b)
#     return pair
# Implement car and cdr.


def cons(a, b):
     def pair(f):
         return f(a, b)
     return pair

def car(func):
    pair = func(lambda a,b : a)
    return pair

def csr(func):
    pair = func(lambda a,b : b)
    return pair

def main():
    print(car(cons(1,2)))
    print(csr(cons(1,2)))

main()