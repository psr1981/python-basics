#! /usr/bin/python3

#while True:
#    try:
#        x = int ( input('enter any number') )
#        break
#    except ValueError:
#        print ('Oops, it is an error')


def divide(x, y):
    try:
        result = x / y
    except ZeroDivisionError:
        print("division by zero!")
    else:
        print("result is", result)
    finally:
        print("executing finally clause")


divide(2, 1)

divide(2, 0)

divide("2", "1")


