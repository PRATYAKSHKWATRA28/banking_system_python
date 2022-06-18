# This is the Main Banking System Code
import json
import time
import functions as f
from forex_python.converter import  CurrencyCodes

f.clear_screen()

bank_name = 'Simple Bank' # Changes to be added to functions.py also

password =  ''     

currency_code_list = ["AED", "AFN", "ALL", "AMD", "ANG", "AOA", "ARS", "AUD", "AWG", "AZN", "BAM", "BBD", "BDT", "BGN", "BHD", "BIF", "BMD", "BND", "BOB", "BRL", "BSD", "BTC", "BTN", "BWP", "BYR", "BZD", "CAD", "CDF", "CHF", "CLP", "CNY", "COP", "CRC", "CUC", "CVE", "CZK", "DJF", "DKK", "DOP", "DZD", "EEK", "EGP", "ERN", "ETB", "EUR", "FJD", "FKP", "GBP", "GEL", "GHS", "GIP", "GMD", "GNF", "GQE", "GTQ", "GYD", "HKD", "HNL", "HRK", "HTG", "HUF", "IDR", "ILS", "INR", "IQD", "IRR", "ISK", "JMD", "JOD", "JPY", "KES", "KGS", "KHR", "KMF", "KPW", "KRW", "KWD", "KYD", "KZT", "LAK", "LBP", "LKR", "LRD", "LSL", "LTL", "LVL", "LYD", "MAD", "MDL", "MGA", "MKD", "MMK", "MNT", "MOP", "MRO", "MUR", "MVR", "MWK", "MXN", "MYR", "MZN", "NAD", "NGN", "NIO", "NOK", "NPR", "NZD", "OMR", "PAB", "PEN", "PGK", "PHP", "PKR", "PLN", "PYG", "QAR", "RON", "RSD", "RUB", "RWF", "SAR", "SBD", "SCR", "SDG", "SEK", "SGD", "SHP", "SLL", "SOS", "SRD", "STD", "STN", "SYP", "SZL", "THB", "TJS", "TMT", "TND", "TOP", "TRY", "TTD", "TWD", "TZS", "UAH", "UGX", "USD", "UYU", "UZS", "VEB", "VND", "VUV", "WST", "XAF", "XCD", "XDR", "XOF", "XPF", "YER", "ZAR", "ZMW", "ZWR"]

main_loop_continue = True
starting_selection_text = (f'''
Welcome to The {bank_name}!
Please select any 1 of the following services

1) Log-In
2) Create Account
3) Info
4) Exit

: ''')

secure_login_text = (f'''
{bank_name} Secure Login Service
''')

while main_loop_continue:
        main_loop_continue = False
        starting_selection = input(starting_selection_text)

        user_exited = False
        further_password_loop_continue = True

        while user_exited != True:
            if starting_selection == '1':
                f.clear_screen()
                print(secure_login_text)
                username = input('Username: ')
                password = f.load_password(username)
                security_pin = f.load_security_pin(password, username)
                f.check_security_pin(security_pin)
                user_currency_code = f.get_currency(username)
                currency_symbol = CurrencyCodes().get_symbol(user_currency_code)

                f.clear_screen()
                f.main_menu_selection = f.main_menu(username)

                while user_exited != True:
                    if f.main_menu_selection == '1':
                        f.clear_screen()
                        bank_balance = f.check_bank_balance(username)
                        print(f'Your Current Bank Balance is {currency_symbol}{bank_balance}')
                        time.sleep(2)
                        f.main_menu_selection = f.main_menu_return(username)
                    elif f.main_menu_selection == '2':
                        f.clear_screen()
                        bank_balance = f.check_bank_balance(username)
                        print(f'Your Current Bank Balance is {currency_symbol}{bank_balance}')
                        Deposit_amount = input(f'Deposit Amount : {currency_symbol}')
                        Deposit_amount_loop = True
                        while Deposit_amount_loop:
                            Deposit_amount_loop = False
                            if Deposit_amount[-1].lower() == 'k' or Deposit_amount[-1].lower() == 't':
                                Deposit_amount = int(Deposit_amount[:-1])  * 1000
                            elif Deposit_amount[-1].lower() == 'm':
                                Deposit_amount = int(Deposit_amount[:-1])  * 1000000
                            elif Deposit_amount[-1].lower() == 'b':
                                Deposit_amount = int(Deposit_amount[:-1])  * 1000000000
                            elif type(Deposit_amount[-1]) == 'int':
                                Deposit_amount = Deposit_amount
                            else:
                                print('Invalid Transfer Amount, Try Again')
                                Deposit_amount_loop = True
                        bank_balance = int(bank_balance)
                        updated_bank_balance = bank_balance + Deposit_amount
                        f.updateJsonFile(username, updated_bank_balance)
                        time.sleep(1)
                        print(f'Your Updated Bank Balance is {currency_symbol}{updated_bank_balance}')
                        f.main_menu_selection = f.main_menu_return(username)
                    elif f.main_menu_selection == '3':
                        loop_withdraw = True
                        while loop_withdraw:
                            loop_withdraw = False
                            f.clear_screen()
                            bank_balance = f.check_bank_balance(username)
                            print(f'Your Current Bank Balance is {currency_symbol}{bank_balance}')
                            withdrawal_amount = input(f'Withdrawal Amount : {currency_symbol}')
                            withdrawal_amount_loop = True
                            while withdrawal_amount_loop:
                                withdrawal_amount_loop = False
                                if withdrawal_amount[-1].lower() == 'k' or withdrawal_amount[-1].lower() == 't':
                                    withdrawal_amount = int(withdrawal_amount[:-1])  * 1000
                                elif withdrawal_amount[-1].lower() == 'm':
                                    withdrawal_amount = int(withdrawal_amount[:-1])  * 1000000
                                elif withdrawal_amount[-1].lower() == 'b':
                                    withdrawal_amount = int(withdrawal_amount[:-1])  * 1000000000
                                elif type(withdrawal_amount[-1]) == 'int':
                                    withdrawal_amount = withdrawal_amount
                                else:
                                    print('Invalid Transfer Amount, Try Again')
                                    withdrawal_amount_loop = True
                            if withdrawal_amount < bank_balance:
                                bank_balance = int(bank_balance)
                                updated_bank_balance = bank_balance - withdrawal_amount
                                f.updateJsonFile(username, updated_bank_balance)
                                time.sleep(1)
                                print(f'Your Updated Bank Balance is {currency_symbol}{updated_bank_balance}')
                                f.main_menu_selection = f.main_menu_return(username)
                                loop_withdraw = False
                            elif withdrawal_amount > bank_balance:
                                f.clear_screen()
                                print('Withdrawal Amount cannot be greater than your current Bank Balance')
                                loop_withdraw = True
                                time.sleep(1)
                                print('\n Try Again')
                                time.sleep(1)
                            else:
                                f.clear_screen()
                                print('Unknown Error, Clearing Invalid Processes')                         
                    elif f.main_menu_selection == '4':
                        f.clear_screen()
                        bank_balance_sender = f.check_bank_balance(username)
                        print(f'Your Current Bank Balance is {currency_symbol}{bank_balance_sender}')
                        transfer_amount_loop = True
                        while transfer_amount_loop:
                            transfer_amount_loop = False
                            transfer_amount = str(input(f'Transfer Amount : {currency_symbol}'))
                            if transfer_amount[-1].lower() == 'k' or transfer_amount[-1].lower() == 't':
                                transfer_amount = int(transfer_amount[:-1])  * 1000
                            elif transfer_amount[-1].lower() == 'm':
                                transfer_amount = int(transfer_amount[:-1])  * 1000000
                            elif transfer_amount[-1].lower() == 'b':
                                transfer_amount = int(transfer_amount[:-1])  * 1000000000
                            elif type(transfer_amount[-1]) == 'int':
                                transfer_amount = transfer_amount
                            else:
                                print('Invalid Transfer Amount, Try Again')
                                transfer_amount_loop = True
                        if transfer_amount < bank_balance_sender:
                            transfer_to = input('Transfer To : ').upper()
                            bank_balance_receiver = f.check_bank_balance(transfer_to)
                            bank_balance_sender = int(bank_balance_sender)
                            bank_balance_receiver = int(bank_balance_receiver)
                            sender_currency_code = user_currency_code
                            receiver_currency_code = f.get_currency(transfer_to)
                            if sender_currency_code == receiver_currency_code:
                                updated_bank_balance_sender = bank_balance_sender - transfer_amount
                                updated_bank_balance_receiver = bank_balance_receiver + transfer_amount
                            elif sender_currency_code != receiver_currency_code:
                                updated_bank_balance_sender = bank_balance_sender - transfer_amount
                                converted_transfer_amount = round(f.currency_conversion(sender_currency_code, transfer_amount, receiver_currency_code))
                                updated_bank_balance_receiver = bank_balance_receiver + converted_transfer_amount
                            f.updateJsonFile(username, updated_bank_balance_sender)
                            f.updateJsonFile(transfer_to, updated_bank_balance_receiver)
                            time.sleep(1)
                            receiver_currency_symbol = CurrencyCodes().get_symbol(receiver_currency_code)
                            print(f'{currency_symbol}{transfer_amount} has been transferred from User-{username.title()} to User-{transfer_to.title()}')
                            print(f'User-{transfer_to.title()} has received {receiver_currency_symbol}{converted_transfer_amount} after currency conversion')
                            print(f'Your Updated Bank Balance is {currency_symbol}{updated_bank_balance_sender}')
                            f.main_menu_selection = f.main_menu_return(username)
                        elif transfer_amount > bank_balance_sender:
                            print('Transfer Amount cannot be greater than your Bank Balance')
                            print('Clearing Invalid Processes')
                            time.sleep(3)
                            f.clear_screen()
                            print('Returning to Main Menu in 3!')
                            time.sleep(1)
                            f.clear_screen()
                            print('Returning to Main Menu in 2!')
                            time.sleep(1)
                            f.clear_screen()
                            print('Returning to Main Menu in 1!')
                            time.sleep(1)
                            f.clear_screen()
                            f.main_menu_selection = f.main_menu(username)
                    elif f.main_menu_selection == '5':
                        amount_to_be_asked = True
                        main_loop_continue = True
                        while main_loop_continue:
                            loop_continue = True
                            loop_final_continue = True
                            main_loop_continue = False
                            f.clear_screen()
                            initial_currency_code = input('Initial Currency (Code) : ').upper()
                            if initial_currency_code in currency_code_list:
                                    initial_currency_symbol = CurrencyCodes().get_symbol(initial_currency_code)
                            elif initial_currency_code not in currency_code_list:
                                print('Currency Code is Invalid')
                                time.sleep(2)
                                loop_continue = False
                                main_loop_continue = True
                                amount_to_be_asked = False
                            while loop_continue:
                                if amount_to_be_asked == True:
                                    amount_to_be_converted = input(f'Amount : {initial_currency_symbol}')
                                    amount_to_be_converted_loop = True
                                    while amount_to_be_converted_loop:
                                        amount_to_be_converted_loop = False
                                        if amount_to_be_converted[-1].lower() == 'k' or amount_to_be_converted[-1].lower() == 't':
                                            amount_to_be_converted = int(amount_to_be_converted[:-1])
                                            amount_to_be_converted = amount_to_be_converted * 1000
                                        elif amount_to_be_converted[-1].lower() == 'm':
                                            amount_to_be_converted = int(amount_to_be_converted[:-1])
                                            amount_to_be_converted = amount_to_be_converted * 1000000
                                        elif amount_to_be_converted[-1].lower() == 'b':
                                            amount_to_be_converted = int(amount_to_be_converted[:-1])
                                            amount_to_be_converted = amount_to_be_converted * 1000000000
                                        elif type(amount_to_be_converted[-1]) == 'int':
                                            amount_to_be_converted = amount_to_be_converted
                                        else:
                                            print('Invalid Conversion Amount, Try Again')
                                            amount_to_be_converted_loop = True
                                
                                final_currency_code = input('Final Currency (Code) : ').upper()
                                if final_currency_code in currency_code_list:
                                    final_currency_symbol = CurrencyCodes().get_symbol(final_currency_code)
                                    loop_final_continue = True
                                elif final_currency_code not in currency_code_list:
                                    print('Currency Code is Invalid')
                                    loop_final_continue = False
                                    main_loop_continue = True
                                    amount_to_be_asked = False
                                while loop_final_continue:
                                    print('Processing can take a while!')
                                    converted_amount = round(f.currency_conversion(initial_currency_code, amount_to_be_converted, final_currency_code),2)
                                    print(f'{initial_currency_symbol}{amount_to_be_converted} converted to {final_currency_code}({final_currency_symbol}) = {final_currency_symbol}{converted_amount}')
                                    loop_final_continue = False
                                    loop_continue = False
                                    main_loop_continue = False
                                    time.sleep(1)
                                    f.main_menu_selection = f.main_menu_return(username)
                    elif f.main_menu_selection == '6':
                        f.clear_screen()
                        old_currency_code = f.get_currency(username).upper()
                        new_currency_code = input('New Currency Code : ').upper()
                        bank_balance_old = f.check_bank_balance(username)
                        bank_balance_new = round(f.currency_conversion(old_currency_code, bank_balance_old, new_currency_code))
                        f.updateJsonFile(username, bank_balance_new)
                        f.updateJsonFile_currency_code(username, new_currency_code)
                        new_currency_symbol = CurrencyCodes().get_symbol(new_currency_code)
                        f.clear_screen()
                        print('Updating Bank Balance with respect to Latest Conversion Rates')
                        time.sleep(1)
                        print(f'Your Updated Bank Balance is {new_currency_symbol}{bank_balance_new}')
                        f.main_menu_selection = f.main_menu_return(username)
                    elif f.main_menu_selection == '7':
                        f.clear_screen()
                        print('Exit Command Recieved')
                        print('Exiting in 3!')
                        time.sleep(1)
                        f.clear_screen()
                        print('Exit Command Recieved')
                        print('Exiting in 2!')
                        time.sleep(1)
                        f.clear_screen()
                        print('Exit Command Recieved')
                        print('Exiting in 1!')
                        time.sleep(1)
                        f.clear_screen()
                        user_exited = True
                    else:
                        f.clear_screen()
                        print('Invalid/Unwanted Input Received, Exiting in 3!')
                        time.sleep(1)
                        f.clear_screen()
                        print('Invalid/Unwanted Input Received, Exiting in 2!')
                        time.sleep(1)
                        f.clear_screen()
                        print('Invalid/Unwanted Input Received, Exiting in 1!')
                        time.sleep(1)
                        f.clear_screen()
                        user_exited = True
            elif starting_selection == '2':
                    if further_password_loop_continue == True:
                        f.clear_screen()
                        user_data_file = open('user_data.json')
                        user_data = json.load(user_data_file)
                        new_username = input('New Username : ').upper()
                        check_username = new_username
                        for check_username in user_data['user_data']:
                            try:
                                tmp = check_username[new_username]
                            except:
                                break
                            print('Entered Username already has an account associated with it')
                            time.sleep(1)
                            print('Returning to Main Menu')
                            time.sleep(1)
                            main_loop_continue = True
                            further_password_loop_continue = False
                            break
                        if further_password_loop_continue != False:
                                new_password = input('New Password : ')
                                new_security_pin = input('New Security PIN : ')
                                currency_code_loop = True
                                while currency_code_loop:
                                    currency_code_loop = False
                                    new_currency_code = input('Currency Code : ').upper()
                                    if new_currency_code in currency_code_list:
                                        new_user = [{"password": new_password, "security_pin": new_security_pin, "bank_balance": 0, "currency": new_currency_code}]
                                    elif new_currency_code not in currency_code_list:
                                        print('Invalid/Unaccepted Currency Code , Try Again')
                                        currency_code_loop = True
                                f.write_json(new_user, new_username)
                                f.clear_screen()
                                print('New user has been created!')
                                user_exit_command = str(input('Do you want to go back to the Main Menu? (Y/N) : '))
                                if user_exit_command.upper() != 'Y' and user_exit_command.upper() != 'YES':
                                    f.clear_screen()
                                    print('Exit Command Recieved')
                                    print('Exiting in 3!')
                                    time.sleep(1)
                                    f.clear_screen()
                                    print('Exit Command Recieved')
                                    print('Exiting in 2!')
                                    time.sleep(1)
                                    f.clear_screen()
                                    print('Exit Command Recieved')
                                    print('Exiting in 1!')
                                    time.sleep(1)
                                    f.clear_screen()
                                    user_exited = True
                                elif user_exit_command.upper() == 'Y' or user_exit_command == 'YES':
                                    further_password_loop_continue = False
                                    user_exited = False
                                    f.clear_screen()
                                    main_loop_continue = True
                                else:
                                    print('Unknown Error')
                        else:
                            f.clear_screen()
                            print('Unknown Error Occured!')
                    else:
                        break
            elif starting_selection == '3':
                f.clear_screen()
                print(f'{bank_name} Services are currently under development')
                print('Currently, we only support active currencies for our services')
                print('Currency Conversion Rates are taken from the last updated conversion rate list')
                print('Currency Conversion Rates are updated only during bank working hours')
                print(      )
                time.sleep(1.75)
                user_exit_command = str(input('Do you want to go back to the Main Menu? (Y/N) : '))
                if user_exit_command.upper() != 'Y' and user_exit_command.upper() != 'YES':
                    f.clear_screen()
                    print('Exit Command Recieved')
                    print('Exiting in 3!')
                    time.sleep(1)
                    f.clear_screen()
                    print('Exit Command Recieved')
                    print('Exiting in 2!')
                    time.sleep(1)
                    f.clear_screen()
                    print('Exit Command Recieved')
                    print('Exiting in 1!')
                    time.sleep(1)
                    f.clear_screen()
                    user_exited = True
                elif user_exit_command.upper() == 'Y' or user_exit_command == 'YES':
                    user_exited = False
                    f.clear_screen()
                    main_loop_continue = True
                    break
                else:
                    print('Unknown Error')
            elif starting_selection == '4':
                time.sleep(1)
                f.clear_screen()
                print('Exit Command Recieved')
                print('Exiting in 3!')
                time.sleep(1)
                f.clear_screen()
                print('Exit Command Recieved')
                print('Exiting in 2!')
                time.sleep(1)
                f.clear_screen()
                print('Exit Command Recieved')
                print('Exiting in 1!')
                time.sleep(1)
                f.clear_screen()
                user_exited = True
            elif starting_selection != 1 and 2:
                time.sleep(1)
                f.clear_screen()
                print('Invalid Selection, Exiting in 3!')
                time.sleep(1)
                f.clear_screen()
                print('Invalid Selection, Exiting in 2!')
                time.sleep(1)
                f.clear_screen()
                print('Invalid Selection, Exiting in 1!')
                time.sleep(1)
                f.clear_screen()
                user_exited = True
            else:
                time.sleep(1)
                f.clear_screen()
                print('Unknown Input, Exiting in 3!')
                time.sleep(1)
                f.clear_screen()
                print('Unknown Input, Exiting in 2!')
                time.sleep(1)
                f.clear_screen()
                print('Unknown Input, Exiting in 1!')
                time.sleep(1)
                f.clear_screen()
                user_exited = True