def my_decorator(func):
    def wrapper(*args, **kwargs):
        print ('before call')
        result  = func(*args, **kwargs)
        print ('after call')
        return result
    return wrapper

@my_decorator

def add(a,b):
    return a+b


print (add(10,20))
print (add(20,30))
print (add(40,90))
