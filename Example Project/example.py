import sys #Imports the module named "sys" into the current namespace
import os #Imports the module named "os" into the current namespace

os.system('cls' if os.name == 'nt' else 'clear') #Clears the screen
print("Hello!") #Prints Text to the terminal 
name = input("What is your name? ") #Creates a variable "name" and allows input of text
print("Nice to meet you", name) #Prints text and displays input from "name" variable
