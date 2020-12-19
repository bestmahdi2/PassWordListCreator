import itertools 
import gc


class passwordMaker:
	def __init__(self, count_char, file, default=[], add=[]):

		self.passCounter = 0 		# to count passwords created
		self.million_counter = 0	# to count milions of password created
		
		combine = add 				# keep selected chars
		
		# possible chars : 
		EsLetters = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
		EcLetters = list("abcdefghijklmnopqrstuvwxyz")
		PLetters = list("اآبپتثجچحخرزدذژسشصضطظفقعغکگلمنوهی")
		numbers = list("1234567890")
		signs = list("!@#$%^&*()_-+=|}{?/\\.><,[] ")

		# add selected chars to 'combine'
		if 1 in default:
			combine = combine + EsLetters
		if 2 in default:
			combine = combine + EcLetters
		if 3 in default:
			combine = combine + numbers
		if 4 in default:
			combine = combine + PLetters
		if 5 in default:
			combine = combine + signs

		# remove duplicated items and sort the list
		combine = list(set(combine))
		combine.sort()


		self.counting(count_char, file, combine)

	# func to save passwords to a file
	def saver(self, holder, file):
		to_print = []
		for i in holder:
			to_print.append("".join(i) + "\n")

		file = open(file, "a")
		file.writelines(to_print)
		file.close()

	# main func
	def counting(self, count_char, file, combine):
		# try diffrent length to creat passwords:
		for number in count_char:
			print(" == Creating password list for length : {} ".format(number))

			holder = []											# to keep passwords
			lister = itertools.product(combine, repeat=number)	# creat all possible passwords


			# to avoid 'memmoryError', program saves each one million password to file, because if it doesn't
			# it can't conver 'lister' to a list (lack of memmory)
			for i in lister:
				holder.append(list(i))

				if len(holder) > 1000000:
					self.million_counter += 1
					self.saver(holder, file)
					
					if self.million_counter == 1 : to_print = "st"
					elif self.million_counter == 2 : to_print = "nd"
					elif self.million_counter == 3 : to_print = "rd"
					else: to_print = "th"

					print(" ~  Saving the {0}{1} million in {2}".format(self.million_counter, to_print, file))
					holder = []

			self.passCounter += len(holder)
			self.saver(holder, file)

		print("\n ++ All passwords: {}".format(str(self.million_counter*1000000 + self.passCounter)))
		input("\n ++ Finished >> [Enter] to exit.")


if __name__ == "__main__":
	def Main():
		# to get characters user wants to be in passwords:
		keys_ = input("\n Which one would you like to be used?(you can use several numbers together)\n  1) English Small letters(a-z)\n" +
                       "  2) English Capital letters(A-Z)\n  3) numbers(1-9)\n  4) Persian letters(الف-ی)\n  5) Other signs(@#{...)\n  6) + Use my list\n > ")
		keys_ = keys_.replace(" ","").replace(",","").replace("-","").replace("_","").replace("\"","").replace("\'","")
		try:
			keys = [int(i) for i in keys_]
		except :
			input(" -- Wrong input for entering numbers >> [Enter] to exit.")
			exit()


		# to get additional characters user wants to be in passwords that weren't in defaults:
		additional_chars = []
		if 6 in keys:
			additional_chars = input("\n Enter all characters you want to use (don't seprate them with any character)\n > ")
			additional_chars = list(set(list(additional_chars)))
		
		# keys and additional can't be empty:
		if not additional_chars and not keys:
			input(" -- Wrong input. You should at least use 'your characters' or one of 'defaults' >> [Enter] to exit.")
			exit()

		# to get length of passwords user wants :
		count_char_ = input("\n How many characters your passwords should have?(can use several numbers)\n > ")
		count_char_ = count_char_.replace(" ","").replace(",","").replace("-","").replace("_","").replace("\"","").replace("\'","")
		if not count_char_ :
			input(" -- Wrong input. you should at least choose one length for passwords >> [Enter] to exit.")
			exit()
		try:
			count_char = [int(i) for i in count_char_]
		except :
			input(" -- Wrong input for entering numbers >> [Enter] to exit.")
			exit()

		# get name of file user wants to save passwords in :
		fileSave = input("\n Which file would you like to save passwords ?(with filetype)\n > ")
		try:
			opener = open(fileSave, "w")
			opener.close()
		except :
			input(" -- Can't create or modify '{}' , make sure it's not [directory] or [in use by other processes] >> [Enter] to exit.".format(fileSave))
			exit()
		

		print()
		# Main:
		P = passwordMaker(default=keys, file=fileSave, count_char=count_char, add=additional_chars)

	Main()