def counter_generator(low, high):
    while (low <= high):
        yield low
        low = low + 1



for i in counter_generator(5, 10):
    print (i, end=' ')
