from sys import argv

script, filename = argv

print "We're going to erase % r." % filename
print "If you don't want to do that hit CTRL-C (^C)."
print "If you do want that, hit RETURN"

raw_input("?")

print "opening the file..." 
target = open(filename, 'w')

#print "Truncating the file. BYE"
#target.truncate()

print "Now I'm going to ask you for three lines"

line1 = raw_input("line 1: ")
line2 = raw_input("line 2: ")
line3 = raw_input("line 3: ")

print "I'm going to write these to the file."

#new_text = line1 + line2 +line3
#target.write(new_text)
target.write(line1 + "\n" + line2 + "\n" + line3)
#target.write("\n")
#target.write(line2)
#target.write("\n")
#target.write(line3)
#target.write("\n")

print "And finally, we close it."
target.close()