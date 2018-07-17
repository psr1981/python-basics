def add_number(n1):
    def adder(n2):
        return n1+n2

    return adder


a_100 = add_number(100)

print (a_100(20));
print (a_100(40));
print (a_100(90));
print (a_100(30));
print (a_100(3));
