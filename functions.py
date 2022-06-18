import json
from os import system, name
import time
from forex_python.converter import  CurrencyRates
import datetime

bank_name = 'Simple Bank' # Changes to be added to main.py also
currentTime = datetime.datetime.now()

def clear_screen():
    import os
    os.system('cls' if os.name == 'nt' else 'clear')

def load_password(username):
    user_data_file = open('user_data.json')
    user_data = json.load(user_data_file)
    for after_username_loading in user_data['user_data'][0][username.upper()]:
        password = after_username_loading['password'].lower()
        return password

def load_security_pin(password, username):
    user_data_file = open('user_data.json')
    user_data = json.load(user_data_file)
    password_correct = False
    while password_correct != True:
        input_password = str(input('Password: ')).lower()
        if input_password == password:
            password_correct = True
            for after_password_loading in user_data['user_data'][0][username.upper()]:
                security_pin = after_password_loading['security_pin']
        elif input_password != password:
            print('Entered Password is Incorrect, Please Try Again')
        else:
            print('Unknown Error, Please Try Again')
    return security_pin

def check_security_pin(security_pin):
    pin_correct = False
    while pin_correct != True:
        input_security_pin = input('Security PIN: ')
        if input_security_pin == security_pin:
            print('User Login Successful')
            pin_correct = True
        elif input_security_pin != security_pin:
            print('Entered PIN is Incorrect, Please Try Again')
        else:
            print('Unknown Error, Please Try Again')


def greeting_based_on_time_finder():
    greeting = 'Hi'
    if 3 <= currentTime.hour and 12 > currentTime.hour:
        greeting = 'Good Morning!'
    elif 12 <= currentTime.hour and 18 > currentTime.hour:
        greeting = 'Good Afternoon!'
    elif 18 <= currentTime.hour and 3 > currentTime.hour:
        greeting = 'Good Evening!'

    return greeting

def main_menu(username):
    greeting_user = greeting_based_on_time_finder()
    main_menu_selection = input(f'''
{greeting_user} {username}, Welcome to The {bank_name}!
Please select any 1 of the following services

1) View your current Bank Balance
2) Deposit Money
3) Withdraw Money
4) Transfer Money
5) Conversion Rate Calculator
6) Change Preffered Currency
7) Exit

: ''')
    return main_menu_selection


def check_bank_balance(username):
    user_data_file = open('user_data.json')
    user_data = json.load(user_data_file)
    for bank_balance_loading in user_data['user_data'][0][username.upper()]:
        bank_balance = bank_balance_loading['bank_balance']
    return bank_balance

def main_menu_return(username):
    main_menu_return = input('\nDo you want to return to the Main Menu? (Y/N): ')
    if main_menu_return.lower() == 'y' or 'yes':
        clear_screen()
        main_menu_selection = main_menu(username)
    elif main_menu_return.lower() != 'y' or 'yes':
        clear_screen()
        print('Invalid Input, Exiting!')
    else:
        print('Unknown Input, Exiting!')
    return main_menu_selection

def updateJsonFile(username, updated_bank_balance):
    with open("user_data.json", "r") as jsonFile:
        data = json.load(jsonFile)

    
    data['user_data'][0][username.upper()][0]['bank_balance'] = updated_bank_balance

    with open("user_data.json", "w") as jsonFile:
        json.dump(data, jsonFile)
    
def updateJsonFile_currency_code(username, new_currency_code):
    with open("user_data.json", "r") as jsonFile:
        data = json.load(jsonFile)

    
    data['user_data'][0][username.upper()][0]['currency'] = new_currency_code

    with open("user_data.json", "w") as jsonFile:
        json.dump(data, jsonFile)

def write_json(new_data, new_username, filename='user_data.json'):
    with open(filename,'r+') as file:
        file_data = json.load(file)
        file_data['user_data'][0][new_username] = new_data
        file.seek(0)
        json.dump(file_data, file, indent = 4)  

def currency_conversion(initial_currency_code, amount, final_currency_code):
    converted_amount = CurrencyRates().convert(initial_currency_code, final_currency_code, amount)
    return converted_amount

def get_currency(username):
    user_data_file = open('user_data.json')
    user_data = json.load(user_data_file)
    for get_currency_loading in user_data['user_data'][0][username.upper()]:
        currency_code = get_currency_loading['currency']
    return currency_code