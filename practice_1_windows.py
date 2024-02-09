# Practice 1
# The Question Is In The README.md File

# Library 
from os import system as sys 
from termcolor2 import colored
from pyfiglet import figlet_format

# Clear Terminal 
sys('cls')

# Intro
print(colored(figlet_format("Exercises Part 1"), color='cyan'))
print(colored('=====================================================================', color='red'))
print(colored('Question Number ===> 1', color='blue'))
print(colored('Be Sure To Read The README File To See The Question', color='blue'))
print('                                            ')

# Fname ==> First Name / Lname ==> Last Name
# Value Input
fname = input('Enter Fname: ')
lname = input('Enter Lname: ')
print('                     ')

# Start Code
print(colored('==============================================', color='green'))
print(f'Full Name ===> {fname.capitalize()} {lname.capitalize()}')
print(colored('==============================================', color='green'))
print(f'The Full Name Is Reversed ===> {lname.capitalize()} {fname.capitalize()}')
print(colored('==============================================', color='green'))

# Create By Moein Heshmati
# Finish