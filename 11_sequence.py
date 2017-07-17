import logging
logging.basicConfig(format='%(asctime)s %(message)s',filename='12.log',level=logging.DEBUG)

class Solution(object):

    def is_additive_number(self, num):
        length = len(num)
	logging.info("The length is determined")
        for i in range(1, int(length/2+1)):
	    for j in range(1, int((length-i)/2 + 1)):
		logging.info("The separation of 3 numbers is done to check whether third is sum of first two")
                first, second, others = num[:i], num[i:i+j], num[i+j:]
                if self.isValid(first, second, others):
                    return "The sequence is additive"
        return "The sequence is not additive"

    def isValid(self, first, second, others):
        if ((len(first) > 1 and first[0] == "0") or
                (len(second) > 1 and second[0] == "0")):
	    logging.info("validation for no input of zeros")
            return "The sequence is not additive"
        sum_str = str(int(first) + int(second))
	logging.info("Calcualting sum of first two numbers")
        if sum_str == others:
	    logging.info("validating if sum of first two euals to the third number")
            return "The sequence is additive"
        elif others.startswith(sum_str):
            return self.isValid(second, sum_str, others[len(sum_str):])
	    logging.info("iterative approach to check until sequence length")
        else:
            return "The sequence is not additive"

n=raw_input("Enter a sequence:")
logging.info("The sequence is accepted from user")
print(Solution().is_additive_number(n))
logging.info("Printing final result")

	