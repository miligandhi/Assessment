class Circle:
	def area(self,r):
		return r**2*3.14

r=float(input("Enter the radius:"))
c=Circle()
print "Area of circle: "+ str(c.area(r))