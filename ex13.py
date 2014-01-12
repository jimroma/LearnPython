from sys import argv # import sys module
# assign the arguments to variable names - the first argument is always the name of the script
script, first, second, third = argv 

print "The script is called:", script
print "Your first variable is:", first
print "Your second variable is:", second
print "Your third variable is:", third
fourth = raw_input("Enter your fourth varable ")
print "Your fourth variable is:", fourth