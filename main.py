import os
import openai
import json
from datetime import datetime
from gptapi import GPT_API
from utils import bcolors

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
    print("1. Selet a model and start generate !")
    print("2. Not define yet")
    print("3. Quit program \n")
    print(bcolors.ENDC)
    return ""

def select_model():
    print("Enter a model number :")

def main():
    gpt_api = GPT_API()
    display_banner()
    while True:
        print_menu()
        user_choice = input("Enter a number : ").lower()
        if user_choice == '1':
            gpt_api.print_models()
            user_choice = input("Enter a model's number : ").lower()
            gpt_api.generate(user_choice)
        elif user_choice == '2':
            print("Not defined")
        elif user_choice == '3':
            exit (0)
        elif user_choice == 'q':
            print("Goodbye!")
            break
        else:
            print(bcolors.RED + "----------\nInvalid choice. Please try again :" + bcolors.ENDC)

if __name__ == "__main__":
    main()
