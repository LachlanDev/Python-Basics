import sys 
import os

end = False #Creates a loop 
menu = 0 #Sets the main menu

while not end: #Execute's the loop 
    if menu == 0: 
        os.system('cls' if os.name == 'nt' else 'clear') #Clears the screen
        print("Main Menu")
        print("1. Addition")
        print("2. Mutilation")
        print("3. Division")
        print("4. Exit")
        opt = input( "Please Select an Option (1-3): ") #Creates a variable
        if opt == "1":
            menu = 1
        if opt == "2":
            menu = 2
        if opt == "3":
            menu = 3
        if opt == "4":
            os.system('cls' if os.name == 'nt' else 'clear')
            exit()
    
    if menu == 1:
        os.system('cls' if os.name == 'nt' else 'clear') #Clears the screen
        print("Welcome to the Python Addition Calculator")
        num1 = int(input("Give me a number to add "))
        num2 = int(input("Give me another number to add "))
        print(num1,"+",num2,"=", num1 + num2)
        print("")
        print("1. Add more numbers")
        print("2. Go back")
        opt = input( "Please Select an Option (1-2): ") 
        if opt == "1":
            menu = 1
        if opt == "2":
            menu = 0

    if menu == 2:
        os.system('cls' if os.name == 'nt' else 'clear') #Clears the screen
        print("Welcome to the Python Mutilation Calculator")
        num1 = int(input("Give me a number to multiply "))
        num2 = int(input("Give me another number to multiply "))
        print(num1,"x",num2,"=", num1 * num2)
        print("")
        print("1. Multiply more numbers")
        print("2. Go back")
        opt = input( "Please Select an Option (1-2): ") 
        if opt == "1":
            menu = 2
        if opt == "2":
            menu = 0

    if menu == 3:
        os.system('cls' if os.name == 'nt' else 'clear') #Clears the screen
        print("Welcome to the Python Division Calculator")
        num1 = int(input("Give me a number to divide "))
        num2 = int(input("Give me another number to divide "))
        print(num1,"÷",num2,"=", num1 // num2)
        print("")
        print("1. Divide more numbers")
        print("2. Go back")
        opt = input( "Please Select an Option (1-2): ") 
        if opt == "1":
            menu = 3
        if opt == "2":
            menu = 0
