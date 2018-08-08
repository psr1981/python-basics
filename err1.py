try:
    print (10/0)

except ValueError as e:
    print ('exception')
    print (e.args)

finally:
    print('finally block');
