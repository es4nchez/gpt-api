import os
# import openai
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

def print_menu(gpt_api):
    print(bcolors.BLUE)
    print("1. Selet a model and start generate !")
    print("2. Conversation mode")
    if not gpt_api.audio_mode:
        print("3. Activate audio mode (deactivated)")
    else:
        print("3. Deactivate audio mode (activated)")
    print("4. Marvin")
    print("5. Quit program \n")
    print(bcolors.ENDC)
    return ""

def select_model():
    print("Enter a model number :")

def main():
    gpt_api = GPT_API()
    display_banner()
    while True:
        print_menu(gpt_api)
        user_choice = input("Enter a number : ").lower()
        if user_choice == '1':
            gpt_api.print_models()
            user_choice = input("Enter a model's number : ").lower()
            gpt_api.generate(user_choice)
        elif user_choice == '2':
            gpt_api.conversation()
        elif user_choice == '3':
            gpt_api.audio_mode = not gpt_api.audio_mode
        elif user_choice == '4':
            gpt_api.Marvin()
        elif user_choice == '5':
            exit (0)
        elif user_choice == 'q':
            print("Goodbye!")
            break
        else:
            print(bcolors.RED + "----------\nInvalid choice. Please try again :" + bcolors.ENDC)

if __name__ == "__main__":
    main()
