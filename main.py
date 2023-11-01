import os
import openai
import json
from datetime import datetime
from gptapi import GPT_API


class bcolors:
        PURPLE = '\033[95m'
        CYAN = '\033[96m'
        DARKCYAN = '\033[36m'
        BLUE = '\033[94m'
        GREEN = '\033[92m'
        YELLOW = '\033[93m'
        RED = '\033[91m'
        BOLD = '\033[1m'
        UNDERL = '\033[4m'
        ENDC = '\033[0m'

def display_banner():
    ascii_art = '''
    ______   _______   ________           ______   _______   ______ 
   /      \ |       \ |        \         /      \ |       \ |      \\
  |  $$$$$$\| $$$$$$$\ \$$$$$$$$        |  $$$$$$\| $$$$$$$\ \$$$$$$
  | $$ __\$$| $$__/ $$   | $$    ______ | $$__| $$| $$__/ $$  | $$  
  | $$|    \| $$    $$   | $$   |      \| $$    $$| $$    $$  | $$  
  | $$ \$$$$| $$$$$$$    | $$    \$$$$$$| $$$$$$$$| $$$$$$$   | $$  
  | $$__| $$| $$         | $$           | $$  | $$| $$       _| $$_ 
   \$$    $$| $$         | $$           | $$  | $$| $$      |   $$ \\
    \$$$$$$  \$$          \$$            \$$   \$$ \$$       \$$$$$$
                                                                    
                                                                       
    '''
    print(bcolors.GREEN + ascii_art)
    print("\t\t\t------------------------")
    print(bcolors.BOLD + "\t\t\t| Welcome to GPT-API ! |")
    print("\t\t\t------------------------\n" + bcolors.ENDC)
    print("\nWhat you want to do now ?\n")

def print_menu():
    print(bcolors.BLUE)
    print("1. List and select an availaible model")
    print("2. Start generate a prompt\n")
    print(bcolors.ENDC)
    print("Enter a number :")
    return ""

def select_model():
    print("Enter a model number :")

def main():
    gpt_api = GPT_API()
    display_banner()
    while True:
        user_choice = input(print_menu()).lower()
        if user_choice == '1':
            gpt_api.print_models()
        elif user_choice == '2':
            model_name = input("Enter the name of the model: ")
            gpt_api.generate(model_name)
        elif user_choice == 'q':
            print("Goodbye!")
            break
        else:
            print(bcolors.RED + "----------\nInvalid choice. Please try again :" + bcolors.ENDC)

if __name__ == "__main__":
    main()
