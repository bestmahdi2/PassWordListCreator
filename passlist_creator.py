import itertools 
import gc



def saver(holder, file):
	to_print = []
	for i in holder:
		to_print.append("".join(i) + "\n")

	file = open(file, "a")
	file.writelines(to_print)
	file.close()

def counting(nums, file, default="e_s"):

	combine = []
	EsLetters = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
	EcLetters = list("abcdefghijklmnopqrstuvwxyz")
	PLetters = list("اآبپتثجچحخرزدذژسشصضطظفقعغکگلمنوهی")
	numbers = list("1234567890")
	signs = list("!@#$%^&*()_-+=|}{?/\\.><,[] ")

	if "e_s" in default:
		combine = combine + EsLetters
	if "e_c" in default:
		combine = combine + EcLetters
	if "p" in default:
		combine = combine + PLetters
	if "n" in default:
		combine = combine + numbers
	if "si" in default:
		combine = combine + signs


	for number in nums:
		print(number)

		holder = []
		lister = itertools.product(combine, repeat=number)

		million_counter = 1
		for i in lister:
			holder.append(list(i))

			if len(holder) > 1000000:
				million_counter += 1
				saver(holder, file)
				print(million_counter)
				holder = []
		saver(holder, file)


counting(default="e_s", file="test.txt", nums=[1, 2, 3, 4])

input("End")