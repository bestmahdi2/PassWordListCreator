from itertools import product


class PasswordMaker:
    def __init__(self, count_char, file, default=[], add=[]):

        self.passCounter = 0         # to count passwords created
        self.million_counter = 0     # to count millions of password created

        combine = add                # keep selected chars

        # default  chars :
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
    @staticmethod
    def saver(holder, file):
        to_print = []
        for i in holder:
            to_print.append("".join(i) + "\n")

        file = open(file, "a")
        file.writelines(to_print)
        file.close()

    # main func
    def counting(self, count_char, file, combine):
        # try different length to creat passwords:
        for number in count_char:
            print(" == Creating password list for length : {} ".format(number))

            holder = []  # to keep passwords
            lister = product(combine, repeat=number)  # create all possible passwords

            # to avoid 'memoryError', program saves each one million passwords to file, because if it doesn't
            # it can't convert 'lister' to a list (lack of memory)
            for i in lister:
                holder.append(list(i))

                if len(holder) > 1000000:
                    self.million_counter += 1
                    self.saver(holder, file)

                    if self.million_counter == 1:
                        to_print = "st"
                    elif self.million_counter == 2:
                        to_print = "nd"
                    elif self.million_counter == 3:
                        to_print = "rd"
                    else:
                        to_print = "th"

                    print(" ~  Saving the {0}{1} million in {2}".format(self.million_counter, to_print, file))
                    holder = []

            self.passCounter += len(holder)
            self.saver(holder, file)

        print("\n ++ All passwords: {}".format(str(self.million_counter * 1000000 + self.passCounter)))
        input("\n ++ Finished >> [Enter] to exit.")


if __name__ == "__main__":
    def junkCleaner(text):
        junks = ["-", "_", ",", " ", "\'", "\""]
        for junk in junks:
            if junk in text:
                text = text.replace(junk, "")

        return text

    def main():
        keys, count_char = [], []
        # to get characters user wants to be in passwords:
        keys_ = input("\n Which one would you like to be used?(you can use several numbers together)\n  " +
                      "1) English Small letters(a-z)\n  2) English Capital letters(A-Z)\n  3) numbers(1-9)\n " +
                      " 4) Persian letters(الف-ی)\n  5) Other signs(@#{...)\n  6) + Use my list\n > ")

        keys_ = junkCleaner(keys_)
        try:
            keys = [int(i) for i in keys_]
        except Exception as E:
            input(" -- Wrong input for entering numbers >> [Enter] to exit.")
            exit()

        # to get additional characters that user wants to be in passwords that weren't in defaults:
        additional_chars = []
        if 6 in keys:
            additional_chars = input("\n Enter all characters you want to use (don't separate with any character)\n > ")
            additional_chars = list(set(list(additional_chars)))

        # keys and additional can't be empty:
        if not additional_chars and not keys:
            input(" -- Wrong input. You should at least use 'your characters' or one of 'defaults' >> [Enter] to exit.")
            exit()

        # to get length of passwords user wants :
        count_char_ = input("\n How many characters your passwords should have?(can use several numbers)\n > ")
        count_char_ = junkCleaner(count_char_)

        if not count_char_:
            input(" -- Wrong input. you should at least choose one length for passwords >> [Enter] to exit.")
            exit()
        try:
            count_char = [int(i) for i in count_char_]
        except Exception as E:
            input(" -- Wrong input for entering numbers >> [Enter] to exit.")
            exit()

        # get name of file user wants to save passwords in :
        file_save = input("\n Which file would you like to save passwords ?(with type-extension)\n > ")
        try:
            opener = open(file_save, "w")
            opener.close()
        except Exception as E:
            input(" -- Can't create or modify '{}' , make sure it's not [directory] or [in use by other processes] >>" +
                  " [Enter] to exit.".format(file_save))
            exit()

        print()
        # Main:
        PasswordMaker(default=keys, file=file_save, count_char=count_char, add=additional_chars)

    main()
