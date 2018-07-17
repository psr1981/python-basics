fish_tuple = ('blowfish', 'clownfish', 'catfish', 'octopus')

fish_list = [ fish for fish in fish_tuple if fish != 'octopus' ]
print(fish_list)

number_list = [x ** 2 for x in range(10) if x % 2 == 0]
print(number_list)

