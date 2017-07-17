import logging
logging.basicConfig(format='%(asctime)s %(message)s',filename='8.log',level=logging.DEBUG)

def add(x,y):
	return x+y
def concatenation(x,y):
	return str(x)+str(y)
x=5
y=6
z=5+6
print "+ as addition"
print add(x,y)
print "+ as concatenation"
print concatenation(x,y)