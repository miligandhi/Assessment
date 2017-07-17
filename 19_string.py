class StringOp:
	def accept(self):
		return raw_input("Please enter a string:")
	def display(self,ip):
		print "Your input string is: " + ip
s=StringOp()
ip=s.accept()
s.display(ip)
