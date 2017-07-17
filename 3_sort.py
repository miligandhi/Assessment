import logging
import operator
logging.basicConfig(format='%(asctime)s %(message)s',filename='3.log',level=logging.DEBUG)

l1=[(1,6,3),(7,3,9),(2,8,1)]
print "original list of tuples"
print l1
logging.info("Printed the original list")
l1.sort(key=operator.itemgetter(2))
logging.info("Performed sorting")
print "Sorted list of tuples:"
print l1
logging.info("Printed the sorted list")