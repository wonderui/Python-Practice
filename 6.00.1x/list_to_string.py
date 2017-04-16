# convert a list to a string
a = (1, 2, 3, 4, 5)
b = list(map(str, a))
a = ','.join(b)
print(a)