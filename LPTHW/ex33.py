'''
i = 0
numbers = []

while i < 6:
	print "At the top i is %d" % i
	numbers.append(i)
	
	i = i + 1
	print "Numbers now:", numbers
	print "At the bottom i is %d" % i

print "The numbers: "

for num in numbers:
	print num
'''	

def print_i(i, m):
	while i < m:
		numbers.append(i)
		
		i = i + 1
	print numbers

numbers = []
print_i(0, 6)