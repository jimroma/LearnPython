def print_two(*args):
	arg1, arg2 = args
	print "arg1: %r, arg2: %r" % (arg1, arg2)
	
def print_two_again(arg1, arg2):
	print "arg1: %r, arg2: %r" % (arg1, arg2) 
	
def print_one(arg):
	print "arg: %r" % (arg)
	
def print_none():
	print "I got nothing"
	
print_two("timmy","timmons")
print_two_again("Bilbo","Baggins")
print_one("one")
print_none()
