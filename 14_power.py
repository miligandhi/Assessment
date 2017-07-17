n=int(raw_input("Enter a positive integer:"))
while n>=2:
	if n%2==0:
		n=n/2
	else:
		print False
		break
	if n==2:
		print True