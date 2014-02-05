#i = 0
#numbers = []
#while i < 6:
#    print "At the top i is %d" % i
#    numbers.append(i)
#    i += 1
#    print "Numbers now: ", numbers
#    print "At the bottom i is %d" % i
#	
#print "The numbers: "
#for num in numbers:
#    print num
	
	
def numloop(x, y):
    i = 0
    numbers = []
    while i < x:
        print "At the top i is %d" % i
        numbers.append(i)
        i = i + y
        print "Numbers now: ", numbers
        print "At the bottom i is %d" % i

    print "The numbers: "
    for num in numbers:
        print num
		
		

x = raw_input("enter a number: ")	
y = raw_input("enter a number: ")		
numloop(int(x), int(y))

print "######################################################"
print "######################################################"
print "######################################################"

elements = []
for i in range(0, 6):
    print "At the top i is %d" % i
    #append to a list
    elements.append(i)
    #i = i + 1 DONT NEED THE INCREMENTOR BECAUSE IT'S USING RANGE
    print "Numbers now: ", elements
    print "At the bottom i is %d" % i

print "The numbers"
for num in elements:
    print num   
