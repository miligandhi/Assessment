ip=raw_input("Enter the string you want to append:")
f=raw_input("Enter the name of file:")
with open(f,'a') as f1:
	f1.write(ip)
