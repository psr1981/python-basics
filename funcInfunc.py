def a():
    print ('i am func-a');

def b(func):
    print ('i am func-b');
    func()

print (b(a))
