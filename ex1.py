import os

secret_code = 8282
balance = 80.00
options = "Please select an option:\n1.View Account Balance.\n2.Withdraw money.\n3.Change secret code.\n4.Exit.\n"
withdraw_options = "Please select a sum to withdraw:\n1.20 nis.\n2.50 nis.\n3.Other.\n"
clear = lambda: os.system('cls')

# Asks for user input and checks if it 
# matches the secret code. You can only
# get out of this method when you get 
# the secret code. 
def auth():
    input_code = ""
    while input_code != str(secret_code):
        print("Input secret code:")
        input_code = input()
        clear()
        if input_code == str(secret_code):
            print("Authorization Succesful\n")
        else:
            print("Authorization Failed\n")
    clear()


# Prints the current balance
def print_balance():
    print("Balance: " + str(balance) + "\n")


# Input: float/integer as an amount to withdraw
# Checks if there is enough money in the account
# for the requested withdraw. If there is, withdraws
# it. Otherwise prints a message.
def withdraw(amount):
    global balance
    if amount > balance:
        print("You don't have enough money.\n")
    else:
        balance = balance - amount

# Prints the withdraw menu and gets an input
# from the user. Lets the user choose between
# withdrawing 20, 50, or a custom amount.
def withdraw_menu():
    print(withdraw_options)
    op = int(input())
    clear()
    if op == 1: 
        withdraw(20) 
    elif op == 2: 
        withdraw(50)
    elif op == 3:
        print("Enter the amount you'd like to withdraw:") 
        amount = float(input())
        withdraw(amount)
    else:
        print("Invalid input.\nTry again:")

# Lets the user pick between 4 main 
# operations: viewing account balance,
# withdrawing money, changing the secret code,
# and exiting the program. Authorizes the user 
# for every operation except exiting the program.
def main_menu():
    global secret_code
    keep_running = True
    while(keep_running):
        print(options)
        op = int(input())
        clear()
        if op == 1: 
            auth()
            print_balance()
        elif op == 2: 
            auth()
            withdraw_menu()
        elif op == 3: 
            auth()
            print("Please input the new secret code:")
            secret_code = input()
            clear()
        elif op == 4: 
            keep_running = False
        else:
            print("Invalid input.\nTry again:")


# Authorizes the user for the first time
# Calls the main menu function.
def main():
    auth()
    main_menu()

main()


