from sys import argv

script, user_name, cat_name = argv
prompt = '### '

print "Hi %s, I'm the %s script." % (user_name, script)
print "I'd like to ask you a few questions"
print "Do you like turtles %s?" % (user_name)
likes = raw_input(prompt)

print "%s, Have you ever felt as though you're brain we going to explode?" % (user_name)
brain_explode = raw_input(prompt) 

print "Bro, do you even lift"
lift = raw_input(prompt)

print """
When I asked about turtles you said %r. 
Felt as if your brain were going to explode %r.
Lift: %r
cat name: %r
blah.....
""" % (likes, brain_explode, lift, cat_name)

