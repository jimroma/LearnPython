def add(a, b):
	print "ADDING %d + %d" % (a, b)
	return a + b
	
def subtract(a, b):
	print "SUBTRACTING %d + %d" % (a, b)
	return a - b
	
def multiply(a, b):
	print "MULTIPLYING %d + %d" % (a, b)
	return a * b

def divide(a, b):
	print "DIVIDINGING %d + %d" % (a, b)
	return a / b
	
print "Let's do some math with just functions"

age = add(30, 5)
height = subtract(78, 4)
weight = multiply(90, 2)
iq = divide(100, 2)
print "Age: %d, Height: %d, Weight: %d, IQ: %d" % (age, height, weight, iq)

# extra blah
print "Here is a puzzle"

what = add(age, subtract(height, multiply(weight, divide(iq, 2))))
print what
	
print "Convert Fahrenheit to Celsius"
print "give me a number to convert to Celsius"
temp = int(raw_input())
#x = ((temp - 32) * 5) / 9
#print x	
def convert(temp):
	return ((temp - 32) * 5) / 9
	
cel = convert(temp)
print "%d degrees Fahrenheit is %d degrees Celsius" % (temp, cel)




