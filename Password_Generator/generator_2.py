#Code generates random passowrd based on a user specified string length

#Imported classess
import secrets
import string


#declaring variables to prevent empty
choice = ""
choice2 = ""
a = 0

#Gets precoded library lists
c_letters = string.ascii_uppercase
l_letters = string.ascii_lowercase
digits = string.digits
c_symbols = string.punctuation


password_characters = c_letters + l_letters + digits + c_symbols

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

    #restarts password
    password = ''

    pwd_length = int(input("Enter the length of your password:\t"))

    print("==========================================")
    #joins characters
    for i in range(pwd_length):
        password += ''.join(secrets.choice(password_characters))
    
    print("\nAuto generated password: " + password + "\n\n==========================================\n")
    #input 2
    choice2 = input("Would you like to generate another password? 'Yes' or 'No': \n").lower()
    #switch statement for different values
    match choice2:
        case "yes":
            a += 1
            print("\n==========================================\nAttempt ", a)
            print("==========================================")
        case "no":
            print("Done")
            exit()
        case _:
            print()
