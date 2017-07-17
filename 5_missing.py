import logging
logging.basicConfig(format='%(asctime)s %(message)s',filename='5.log',level=logging.DEBUG)

l=[1,2,3,4,6,7,8]
n=l[0]
for i in range(0,len(l)):
	if l[i]==n:
		pass
		n=n+1
	else:
		print "Missing number is:" +str(n)
		logging.info("Missing number found")
		break	
