import logging
logging.basicConfig(format='%(asctime)s %(message)s',filename='4.log',level=logging.DEBUG)

try:
	n=int(raw_input("Enter a number:"))
	logging.info("Number accepted from user")
	n=str(n)
	sum=0
	for i in n:
		sum=sum+int(i)
	logging.info("sum of digits is calculated")
	print "The sum of digits is: " + str(sum)
	logging.info("Printed the sum")
except ValueError:
	print "Only numeric digits!"
	logging.info("Exception : User entered a wrong value")



