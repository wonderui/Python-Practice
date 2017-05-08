from sys import argv

script, argv1, argv2 = argv

def print_two(*args):
	arg1, arg2 = args
	print "arg1: %r, arg2: %r" %(arg1, arg2)

def print_two_again(arg1, arg2):
	print "arg1: %r, arg2: %r" %(arg1, arg2)
	
def print_one(arg1):
	print "arg1: %r" % arg1
	
def print_none():
	print "I got nothin'."

print "argv1: %r, argv2: %r" %(argv1, argv2)
print_two("zed", "shawn")
print_two_again("HeHe", "HaHa")
print_one(argv1)
print_none()