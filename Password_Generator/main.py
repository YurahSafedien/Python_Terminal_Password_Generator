#Generates a random 8 character password consisteing of symbols, letters and numbers

import random

#declaring variables to prevent empty
auto_password = ""
choice = ""
choice2 = ""
i = 0

#list of capital letters
c_letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]

#list of lower case letters
l_letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]

#list of numbers
c_numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]

#list of symbols
c_symbols = ["~", "!", "@", "#", "$", "%", "^", "&", "*", "(", ")", ".", "<", ">", "?"]

#method to auto 4 characters from each list and put random index values of eac list together to form a string with random characters
def password_generator(auto_password):

    #creates list of 4 automatically generated indexes from c_letters list
    auto_c_letters = [random.choice(c_letters) for i in range(4)]
    #creates list of 4 automatically generated indexes from l_letters list
    auto_l_letters = [random.choice(l_letters) for i in range(4)]
    #creates list of 4 automatically generated indexes from c_numbers list
    auto_c_numbers = [random.choice(c_numbers) for i in range(4)]
    #creates list of 4 automatically generated indexes from c_symbols list
    auto_c_symbols = [random.choice(c_symbols) for i in range(4)]

    #Adds all auto-generated indexes to a list
    password_characters = [auto_c_letters[0], auto_c_letters[1], auto_c_letters[2], auto_c_letters[3], auto_c_symbols[0], auto_c_symbols[1], auto_c_symbols[2], auto_c_symbols[3], auto_c_numbers[0], auto_c_numbers[1], auto_c_numbers[2], auto_c_numbers[3], auto_l_letters[0], auto_l_letters[1], auto_l_letters[2], auto_l_letters[3]]

    #Gets a random value from password_characters
    char1 = random.choice(password_characters)
    char2 = random.choice(password_characters)
    char3 = random.choice(password_characters)
    char4 = random.choice(password_characters)
    char5 = random.choice(password_characters)
    char6 = random.choice(password_characters)
    char7 = random.choice(password_characters)
    char8 = random.choice(password_characters)

    #Puts together randomly generated characters
    auto_password = char1 + char2 + char3 + char4 + char5 + char6 + char7 + char8

    #returns random string for password
    return auto_password


#Loops until user enters "yes" to generate password, "no" to exit app or makes user re-enter if input is not matched according to switch statement
while (choice != "no" or choice != "yes") == True:
    #input 1
    choice = input("\nWould you like a auto-generated password? 'Yes' or 'No'. :\n").lower()
    #switch statement for different values
    match choice:
        case "yes":
            break
        case "no":
            exit()
        case _:
            print("Invalid option! Try again!")
#-----------------------------------------------
        #first decision method
        # if choice == "yes":
        #     break
        # elif choice == "no":
        #     exit()
        # else:
        #     "Invalid option! Try again!"
#-----------------------------------------------
print("==========================================")

while (choice2 != "yes" or choice2 != "no") == True:
    #calls password_generator() method and gets return value "auto_password"
    auto_password = password_generator(auto_password)
    print("\nAuto generated password: " + auto_password + "\n\n==========================================\n")
    #input 2
    choice2 = input("Would you like to generate another password? 'Yes' or 'No': \n").lower()
    #switch statement for different values
    match choice2:
        case "yes":
            i += 1
            print("\n==========================================\nAttempt ", i)
            print("==========================================")
        case "no":
            print("Done")
            exit()
        case _:
            print()