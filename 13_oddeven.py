n=int(raw_input("n="))
print str(n),
while n<>1:
	if n%2==0:
		n=n/2
		print str(n),
	else:
		n=3*n+1
		print str(n),
