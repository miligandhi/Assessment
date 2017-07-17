import logging
logging.basicConfig(format='%(asctime)s %(message)s',filename='6.log',level=logging.DEBUG)
import re

logging.info("Accepting email from user")

email = raw_input("Enter your email ID:")

logging.info("Created regular expression")

cmp = "(\w+)@(\w+)\.(com)"
cmp1 = re.match(cmp,email)

logging.info("Compared with regular expression")

print cmp1.group(1)

logging.info("Printed the username")