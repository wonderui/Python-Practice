# Functions as Arguments

def summation(n, term):
	'''
	n是整数
	term是一个方法
	方法返回term(k)的和，k从0到n
	'''
	# assign two variable at the same time
	total, k = 0, 1
	while k <= n:
		total, k = total + term(k), k + 1
	return total
	
def cube(x):
	return x * x * x
	
def sum_cubes(n):
	# 用上面两个方法包装一个新方法
	return summation(n, cube)
	
result = sum_cubes(3)
print(result)
