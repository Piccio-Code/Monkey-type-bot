import time

import Wrapper

import os
from dotenv import load_dotenv


def menu():
    print('''
BOT MENU
===========================
1) Time
2) Words
3) Quote
4) Quit
===========================    
    ''')

    type_test = input("Insert choice: ")

    if type_test == '4':
        Wrapper.close_driver()



        exit()

    mode_test = ""

    match type_test:
        case "1":
            print('''
TIME MENU
===========================
1) 15
2) 30
3) 60
4) 120
===========================    
                ''')

            mode_test = input("Insert choice: ")
        case "2":
            print('''
WORDS MENU
===========================
1) 10
2) 25
3) 50
4) 100
===========================    
                ''')

            mode_test = input("Insert choice: ")
        case "3":
            print('''
QUOTE MENU
===========================
1) short
2) medium
3) long
4) thick
===========================    
                ''')

            mode_test = input("Insert choice: ")

    wpm = input("Insert wpm (Note this will not be accurate): ")

    return int(type_test), int(mode_test), int(wpm)

print("Welcome to Monkey Type Bot")

Wrapper.cookie_accept()
load_dotenv()

login_choice = input("Vuoi fare il login (Y/n): ")

if login_choice.upper() == "Y":
    if not os.environ.get("EMAIL") or not os.environ.get("PASSWORD"):
        with open(".env", "w") as f:
            f.write("EMAIL=" + input("Email: ") + "\n")
            f.write("PASSWORD=" + input("Password: "))

        load_dotenv()

    Wrapper.access_account(os.environ.get("EMAIL"), os.environ.get("PASSWORD"))
    Wrapper.home_page()

while True:
    type_index, mode_index, wpm = menu()
    Wrapper.home_page()
    time.sleep(1)

    Wrapper.select_test(type_index, mode_index)
    Wrapper.take_test(60 / (wpm * 4.3))
