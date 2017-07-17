fname = input("Enter file name: ")
num_lines = 0
with open(fname) as f:
    for line in f:
        num_lines=num_lines+ 1
print "Number of lines:"
print str(num_lines)