# Different list examples

the_count = [1, 2, 3, 4, 5]
fruits = ['apples', 'oranges', 'pears', 'apricots']
change = [1, 'pennies', 2, 'dimes', 3, 'quarters']

# this first kind of for-loop goes through a list
for num in the_count:
	print "this is the count %d" % (num)

# same as above
for fruit in fruits:
	print  "A fruit of type: %s" % (fruit)
	
# go though mixed lists
for i in change:
	print "I got %r" % (i)

# build a list
elements = []

# range function to generate a count
for i in range(0, 6):
	print "Adding %d to the list." % (i)
	#append to a list
	elements.append(i)
	

# print the elements list
for i in elements:
	print "Element was: %d" % i
	
elements2 = []
elements2.append(range(0, 6))
print elements[1]

	
