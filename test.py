
try:
    date = input("Enter Your Birthdate in dd/mm/yyyy: ")
    if date == "":

        raise ValueError('String is empty')
    elif date == '?':

        date = input("Enter your birthdate in dd/mm/yyyy: ")
        if date == "":
            raise ValueError('String is Empty')
    elif date != '':

        age = date[-4:-1]

    elif date == 'q' or 'Q':
        exit()
except ValueError as e:
    print(e)
    date = input("Please Enter your Date in dd/mm/yyyy format")
finally:
    print("Bye! Hope you run this program again")
