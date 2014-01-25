#F to C 	Deduct 32, then multiply by 5, then divide by 9
#C to F 	Multiply by 9, then divide by 5, then add 32

# tempature functions
def FtoC(f):
	c = ((int(f) - 32) * 5) / 9
	return c
	

def CtoF(c):
	f = ((int(c) * 9) / 5) + 32
	return f

print "Would you like to convert Celsius to Fahrenheit or Fahrenheit to Celsius?"
selection = raw_input("Enter 1 for F to C or enter 2 for C to F: ")


if selection == "1":
	#print "F to C"
	f = raw_input("Enter temp in Fahrenheit to convert to Celsius: ")
	temp = FtoC(f)
	print str(f) + " degrees in Fahrenheit is " + str(temp) + " degrees Celsius"
elif selection == "2":
	#print "C to F"
	c = raw_input("Enter temp in Celsius to convert to Fahrenheit: ")
	temp = CtoF(c)
	print str(c) + " degrees ion Celsius is " + str(temp) + " degrees Fahrenheit"
else:
	print "COME ON MAN."