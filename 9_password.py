import logging
logging.basicConfig(format='%(asctime)s %(message)s',filename='9.log',level=logging.DEBUG)
class Pswd:
	def validate(self,s):
	
		if len(s)<6:
			return "Invalid"
		if len(s)>16:
			return "Invalid"
		a=0
		A=0
		n=0
		sp=0
		for char in str(s):
			if char in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ':
				A=A+1
		for char in str(s):
			if char in 'abcdefghijklmnopqrstuvwxyz':
				a=a+1
		for char in str(s):
			if char in '1234567890':
				n=n+1
		for char in str(s):
			if char in '$#@':
				sp=sp+1
	
		if a==0 or A==0 or n==0 or sp==0:
			return "Invalid"
		else:
			return "Valid"
	
p=Pswd()
s=raw_input("Enter your password:")
print p.validate(s)