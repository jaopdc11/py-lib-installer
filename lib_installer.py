# - Imports all the necessary libraries
import os
import platform
import colorama
from colorama import Fore, Style
import time as t

# - Starts the colorama system
colorama.init()

# - Defines a function to clear the terminal before the code executes
def cls():
    if platform.system() == 'Windows':
        os.system('cls')
    else:
        os.system('clear')

# - Cleans the terminal before the code execute
cls()

# - Ask for the user which librarie he wants to install
lib = str(input(Fore.GREEN + 'Type the name of the library that you want to install:   ' 
                + Style.RESET_ALL))

# - Clean the terminal before the installation starts
cls()

# - Gives a debug for the user
print (f'Starting download of {lib}... \n')

# - Starts downloading the librarie chosen by the user
os.system(f'pip install {lib}')

# - Gives a debug for the user after the installation
print (f'Succssesfully installed {lib}!')

# - Gives a pause before the program end
t.sleep(0.5)

# - Cleans the terminal before the program end
cls()
