tabby_cat = "\tI'm tabbed in." # escaped tab
persian_cat = "I'm split \non a line" # escaped new line
backslash_cat = "I'm a \\ a \\ cat." # escaped backslashes

fat_cat = """
I'll do a list:
\t* Cat food
\t* fishies
\t* catnip\n\t* Grass
"""

print tabby_cat
print persian_cat
print backslash_cat
print fat_cat

# this creates an infinte loop 
#while True:
#	for i in ["/","-","|","\\","|"]:
#		print "%s\r" % i,