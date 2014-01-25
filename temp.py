#F to C 	Deduct 32, then multiply by 5, then divide by 9
#C to F 	Multiply by 9, then divide by 5, then add 32
# x = raw_input("Enter temp in celsius: ")
#c = ((int(f) - 32) * 5) / 9
#print c
#f = ((int(c) * 9) / 5) + 32
#print f 


f = raw_input("Enter temp in Fahrenheit: ")
def FtoC(f):
	c = ((int(f) - 32) * 5) / 9
	return c
	
temp = FtoC(f)
print temp


c = raw_input("Enter temp in celsius: ")
def CtoF(c):
	f = ((int(c) * 9) / 5) + 32
	return f
	
temp = CtoF(c)
print temp

	


