import os

secret_code = 8282
balance = 80.00
authorized = False
options = "Please select an option:\n1.View Account Balance.\n2.Withdraw money.\n3.Change secret code.\n4.Exit.\n"
withdraw_options = "Please select a sum to withdraw:\n1.20 nis.\n2.50 nis.\n3.Other.\n"
clear = lambda: os.system('cls')
# Asks for user input.
# Returns true if the code the user's
# input is the secret code. 
def auth():
    input_code = ""
    while input_code != str(secret_code):
        print("Input secret code:")
        input_code = input()
        if input_code == str(secret_code):
            print("Authorization Succesful\n")
        else:
            print("Authorization Failed\n")
    clear()


def print_balance():
    print("Balance: " + str(balance) + "\n")


def withdraw(amount):
    global balance
    if amount > balance:
        print("You don't have enough money.\n")
    else:
        balance = balance - amount

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



def main():
    auth()
    main_menu()

main()


