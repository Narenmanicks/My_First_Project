import random
import datetime
from datetime import *

mobile_g= None
pass_g = None
email_g = None
def login_page():
    print("----------Log In----------")
    global pass_g, email_g, mobile_g
    while True:
        log_email = str(input("Enter your email address or mobile number:"))
        log_pass = str(input("Enter your password:"))

        if (log_email == email_g or log_email == mobile_g) and log_pass == pass_g:
            print("You've successfully logged in.")
            break

        elif (log_email != email_g or log_pass != pass_g) or (log_email == email_g or log_pass != pass_g):
            print("The entered email or password is incorrect")

        elif (log_email != mobile_g or log_pass != pass_g) or (log_email == mobile_g or log_pass != pass_g):
            print("The entered mobile number or password is incorrect")
    return  my_project()

def sign_up_page():
    global pass_g, email_g, mobile_g
    print("----------Sign Up----------")
    name_user = input("Enter your full name:")
    len_name= len(name_user)
    while len_name < 3:
        print("Please try again.Name must contain atleast 3 letters. ")
        name_user = input("Enter your full name:")
        len_name2 = len(name_user)
        if len_name2 >= 3:
            break
    mobile_user = int(input("Enter your mobile number:"))
    len_mobile = len(str(mobile_user))
    while len_mobile != 10:
        try:
            print("Invalid, mobile number should contain 10 numbers")
            mobile_user = int(input("Enter your mobile number:"))
            len_mobile2 = len(str(mobile_user))
            if len_mobile2 == 10:
                mobile_g = str(mobile_user)
                break
        except ValueError:
            print("Invalid, mobil number shouldn't contain spaces or letters or any special characters.")
        break
    email_user = str(input("Enter your email address:"))
    email_g = email_user
    pass_user = str(input("Create your password:"))
    confirm_pass = str(input("confirm your password:"))
    while True:
        if pass_user != confirm_pass:
            print("Password dosen't match.")
            pass_user = str(input("Create your password:"))
            confirm_pass = str(input("confirm your password:"))
        if pass_user == confirm_pass:
            print("You've successfully signed up")
            pass_g = confirm_pass
            break
    return login_page()
#age finder
def age_find():
    print("----------AGE FINDER----------")
    year= int(input("Enter Your Birth Year:"))
    current_year= datetime.now().year
    imp = current_year - year
    while imp >90:
        try:
            print("The year you entered is impossible to live now.")
            year = int(input("Enter Your Birth Year:"))
            imp2= current_year - year
            if imp2 <= 90:
                break
        finally:
            pass
    age1= current_year - year
    age2= (current_year - year) - 1
    bday= input("Have you celebrated your birthday this year?(Yes/No):")
    low_bday= bday.lower()
    if low_bday=="yes":
        age_1 = f"You're {age1} years old."
        print(age_1)
    elif low_bday=="no":
        age_2= f"You're {age2} years old."
        print(age_2)
    else:
        print("Invalid option")
    return "Exiting..."
#number guessing game

def num_guess():
    print("----------NUMBER GUESSING GAME----------")
    ran_num= random.randint(1,10)
    try:
        guess_num= int(input("Guess the correct number:"))
        if guess_num <=0 or guess_num >=11:
            print("Invalid, Enter number between 1 to 10")
        elif guess_num==ran_num:
            print("Correct answer, You won.")
        while guess_num != ran_num:
            try:
                print("Incorrect")
                guss_num= int(input("Guess the correct number:"))
                if guess_num <= 0 or guess_num >= 11:
                    print("Invalid, Enter number between 1 to 10")
                elif guss_num==ran_num:
                    print("Correct answer, You won.")
                    break
            except ValueError:
                print("ERROR, Please enter only numbers.")
    except ValueError:
        print("ERROR, Please enter only numbers.")
    return "Exiting..."

#Greetings
def greeting():
    print("----------GREETINGS----------")
    name= str(input("Enter your Name:"))
    print("Hello", name)
    print("Thank You for taking the time ro review my projects.")
    print("Have a nice day.")
    return "Exiting..."

#calculator
def calculator():
    print("----------CALCULATOR----------")
    operators= ["Addition", "Subtraction", "Multiplication", "Division", "Power", "Odd/Even","Percentage"]
    for no, operation in enumerate(operators):
        print(no, operation)
    option= int(input("Enter any option"))
    if option==0:
        num1 = int(input("Enter any number:"))
        num2 = int(input("Enter any number:"))
        add = num1 + num2
        print("The answer is", add)
    elif option==1:
        num1 = int(input("Enter any number:"))
        num2 = int(input("Enter any number:"))
        subtract = num1 - num2
        print("The answer is", subtract)
    elif option==2:
        num1 = int(input("Enter any number:"))
        num2 = int(input("Enter any number:"))
        multiply = num1 * num2
        print("The answer is", multiply)
    elif option==3:
        num1 = int(input("Enter any number:"))
        num2 = int(input("Enter any number:"))
        divide = num1 / num2
        print("The answer is", divide)
    elif option==4:
        num1 = int(input("Enter any number:"))
        num2 = int(input("Enter any number:"))
        power = num1 ** num2
        print("The answer is", power)
    elif option == 5:
        number = int(input("Enter any number:"))
        if number % 2 == 0:
            print("It is an even number.")
        elif number % 2 != 0:
            print("It is an odd number")
    elif option == 6:
        num4 = int(input("Enter any number:"))
        num5 = int(input("Enter any number:"))
        percent = num4 // num5
        print(percent, "Percentage(%)")
    else:
        print("Enter a valid option.")
    return "Exiting..."

#symbol pattern
def symbol_patt():
    n= int(input("Enter no. of rows"))
    symbol = str(input("Enter any symbol"))
    for sym in range(1, n+1):
        print(symbol * sym)
    return "Exiting..."

#home page
def my_project():
    print("----------MY PROJECTS----------")
    project= ["Age finder",  "Number guessing game", "Greetings", "Calculator"]
    project.append("Symbol Pattern")
    for i, proj in enumerate(project):
        print(i, proj)
    try:
        opt= int(input("Enter any option:"))
        if opt==0:
            age_finder= age_find()
            print(age_finder)
            return my_project()
        elif opt==1:
            num_guessing= num_guess()
            print(num_guessing)
            return my_project()
        elif opt==2:
            greetings= greeting()
            print(greetings)
            return my_project()
        elif opt==3:
            calculat= calculator()
            print(calculat)
            return my_project()
        elif opt ==4:
            symbol_pattern= symbol_patt()
            print(symbol_pattern)
            return my_project()
        else:
            print("Invalid, Enter a valid option.")
    except ValueError:
        print("ERROR, please enter a valid option. (only in numbers)")
    return my_project()

print("----------WELCOME----------")
start= input("Enter any key to continue:")
print("Hi there")
print("Sign up to continue.")
sign = sign_up_page()
print(sign)