import logging
import string
logging.basicConfig(format='%(asctime)s %(message)s',filename='2.log',level=logging.DEBUG)


alphabet=dict(zip(range(1, 27), string.ascii_lowercase))
n=int(raw_input("Enter no. of rows[1-27]:"))
logging.info("User inputs no. of rows")
k=1
for i in range(0,n):
	for j in range(0,i):
		print alphabet[k],
		k=k+1
	print
logging.info("Output displayed")