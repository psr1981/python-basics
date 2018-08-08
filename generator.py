def counter(low, high):

    while (low <= high):
        yield low
        low = low + 1


for i in counter(10, 20):
    print (i)
