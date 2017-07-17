ip=raw_input("Enter your sentence")
a=0
d=0
for char in ip:
	if char.isalpha():
		a=a+1
	if char.isdigit():
		d=d+1
print "LETTERS: " +str(a)
print "DIGITS: " +str(d)