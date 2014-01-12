formatter = "%r %r %r %r" # string variable with 4 r formatters

print formatter, "- this is the formatter with no arguments passed to it"
print formatter % (1, 2, 3, 4) # formatter with 4 numbers passed to it
print formatter % ("one", "two", "three", "four") # formatter with 4 strings passed to it
print formatter % (True, False, False, True)# formatter with boolean values passed to it
print formatter % (formatter, formatter, formatter, formatter) # print formatter with no values 4 times
print formatter % (
	"I had this thing.",
	"That you could type up right",
	"But it didn't sing.",
	"Timmy"
)