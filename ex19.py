#define and create function
def cheese_and_crackers(cheese_count, boxes_of_crackers):
	print "You have %d cheeses!" % cheese_count
	print "You have %d boxes of crackers!" % boxes_of_crackers
	print "Man that's enough for a party!"
	print "I like turtles. \n"

#call function	
print "We can just give the function numbers directly:"
cheese_and_crackers(20, 30)

print "OR, we can use variables from our script:"
cheese = 10
crackers = 50
cheese_and_crackers(cheese, crackers)

print "We can even do math inside too:"
cheese_and_crackers(10 + 10, 5 +6)

print "And we can combine the two, variables and math:"
cheese_and_crackers(cheese + 100, crackers + 1000)


def math(x, y):
	num = x + y
	print x, "plus", y, "equals", num

math (10, 10)
x = 23
y = 42
math(x, y)
math(x + x, y)
zebra = 3000
timmy = 9
math(zebra, timmy)
print "give me a number:"
num1 = int(raw_input())
print "give me another number":
num2 = int(raw_input())
math(num1, num2)














