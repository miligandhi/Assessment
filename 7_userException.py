import logging
logging.basicConfig(format='%(asctime)s %(message)s',filename='7.log',level=logging.DEBUG)

class UserException(Exception):
	def __init__(self,value):
		self.value=value

	def __str__(self):
		return(self.value)

try:
	raise(UserException("User Defined Exception"))
except UserException as error:
	print error.value 