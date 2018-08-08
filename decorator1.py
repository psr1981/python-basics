def my_decorator(func):

    def wrapper(*args, **kwargs):
        print('wrapper-start');
        func(*args, **kwargs)
        print('wrapper-end');

    return wrapper



@my_decorator
def foo(i):
    print('value of foo', str(i))


print(foo(10))
    
