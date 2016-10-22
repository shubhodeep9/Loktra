"""
The code will be class based consisting of function to trigger operation
"""

class Hash:
	LETTERS = "acdegilmnoprstuw"

	"""
	Method to hash from letters to numbers
	Algorithm mentioned in question
	"""
	def hash(self,s):
		h=7
		for i in s:
			h = (h*37 + self.LETTERS.index(i))
		return h

	"""
	Method to dehash from number to letters
	"""
	def dehash(self,num):
		out_s = "" #output string, declared as s in hash function
		while(num > 0 and num != 7):
			i = num%37 #substituting index of letter from formula used h = h*37 + letters.indexOf(s[i])
			try:
				out_s = self.LETTERS[i] + out_s
			except IndexError:
				#position was more than the length of LETTERS
				raise SystemExit("Inappropriate number")
			num = (num - i)/37 #h = h*37 + letters.indexOf(s[i])

		if num == 7: #As h was taken 7 in hash function
			return out_s
		else:
			raise SystemExit("Inappropriate number")


def main():
	obj = Hash()
	print "Executin with sample case hash(leepadg)"
	print "Calling dehash(680131659347)"
	sample_dh = obj.dehash(680131659347)
	print sample_dh
	print "Calling hash(leepadg)"
	sample_h = obj.hash("leepadg")
	print sample_h
	print "Output for dehash(680131659347) == leepadg"
	print sample_dh == "leepadg"
	print "Output for hash(leepadg) == 680131659347"
	print sample_h == 680131659347


if __name__ == '__main__':
	main()