class ListOp:
	def append1(self,l,value):
		l.append(value)
		print "The new list is: "
		print l
	def delete1(self,l,value):
		l.pop(value)
		print "The new list is: "
		print l
	def display1(self,l):
		print "Displaying List:"
		print l

listop=ListOp()
l=[1,2,3,4]
print l
listop.append1(l,input("Enter value to append:"))
listop.delete1(l,input("Enter value to delete:"))
listop.display1(l)