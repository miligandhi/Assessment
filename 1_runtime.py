import logging
logging.basicConfig(format='%(asctime)s %(message)s',filename='example.log',level=logging.DEBUG)

a=6
b=0
try:
	c=a/b
except:
	raise ZeroDivisionError("Division by zero!")	
	