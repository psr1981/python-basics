class Counter():
    def __init__(self, low, high):
        self.current = low
        self.max = high


    def __iter__(self):
        return self

    def __next__(self):

        if (self.current<= self.max):
            retval = self.current;
            self.current = self.current + 1
            return retval

        else:
            raise StopIteration


c1 = Counter(10, 20)

for i in c1:
    print (i)


