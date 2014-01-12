name = 'Timmy T Timmons'
age = 35 # not a lie
height = 74  # inches
weight = 180 # lbs
eyes = 'black'
teeth = 'yellow'
hair = 'green'

print "Let's talk about %s" % name # string formatter
print "He's %d inches tall." % height # digit formatter
print "He's %d pounds heavy." % weight # digit formatter 
print "Actually that's not too heavy." 
print "He's got %s eyes and %s hair." % (eyes, hair) # two string formatters using ()
print "His teeth are usually %s depending on the coffee" % teeth
 
#tricky
print "If I add %d, %d, and %d I get %d" % (age, height, weight, age + height + weight) 