# Python program to illustrate 
# *args 
def argument_test(arg1, *argv):
    print(*argv)
    print ("first argument :", arg1)
    for arg in argv:
        print("Next argument through *argv :", arg)
 




def hello(**kwargs):
    print(kwargs)
    if kwargs is not None:
        for key, value in kwargs.items():
            print ("%s == %s" %(key, value))




argument_test('Hello', 'Welcome', 'to', 'GeeksforGeeks')

hello(a=90, b=80, c=66)


