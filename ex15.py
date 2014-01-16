# import argv module
from sys import argv

# declare filename argument
script, filename = argv

#create a filehandle called txt
txt = open(filename)
#print txt
print txt.read()

#print the filename
print "Here's your file %r:" % filename
print txt.read()

print "Type the file name again (or any file)"
file_again = raw_input("> ")

txt_again = open(file_again)

print txt_again.read()
txt.close()
txt_again.close()