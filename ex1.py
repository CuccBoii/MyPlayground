import os

secret_code = 8282
balance = 80.00
authorized = False
options = "Please select an option:\n1.View Account Balance.\n2.Withdraw money.\n3.Change secret code.\n4.Exit.\n"
withdraw_options = "Please select an option:\n1.20 nis.\n2.50 nis.\n3.Other.\n"

# Asks for user input.
# Returns true if the code the user's
# input is the secret code. 
def auth():
    print("Input secret code:")
    input_code = input()
    if input_code == str(secret_code):
        print("Authorization Succesful\n")
    else:
        print("Authorization Failed\n")
    return input_code == str(secret_code)


def print_balance():
    print("Balance: " + str(balance))


def withdraw(amount):
    global balance
    if amount > balance:
        print("You don't have enough money.")
    else:
        balance = balance - amount

def withdraw_menu():
    cls()

def main_menu(keep_running):
    while(keep_running):
        print(options)
        op = int(input())
        if op == 1: 
            print_balance()
        elif op == 2: 
            withdraw_menu()
        elif op == 3: 
            print("Please input the new secret code:")
            secret_code = input()
        elif op == 4: 
            keep_running = False
        else:
            print("Invalid input.\nTry again:")




def main():
    global authorized
    while authorized is False:
        authorized = auth()
    os.system('clear')
    main_menu(True)

main()


