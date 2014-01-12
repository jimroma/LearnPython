x = "There are %d types of people." % 10
binary = "binary"
do_not = "don't"
y = "Those who know %s and those who %s." % (binary, do_not)

print x
print y

print "I said: %r." % x # r formatter String (converts any python object using repr())
print "I also said: '%s'." % y # s formatter pass variable string y

hilarious = False
joke_eval = "Isn't that joke so funny?! %r" # putting the r formatter in the string

# here the variable hilarious is passed to the r formatter in the joke_eval string
print joke_eval % hilarious

w = "This is the left side of..."
e = "a string with a right side."

print w + e
print "blah"
print w,e