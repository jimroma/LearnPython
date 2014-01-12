print "How old are you?", #comma at the end of the line prevents print from adding a new line charcter at the end of the line
age = raw_input() #promt user for input equal to the age variable
print "How tall are you?",
height = raw_input()
print "How much do you weigh?"
weight = raw_input()

print "So you're %r old, %r tall and %r heavy." % (age, height, weight)
