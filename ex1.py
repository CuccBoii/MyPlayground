secret_code = 8282
balance = 80.00
authorized = False

# Asks for user input.
# Returns true if the code the user's
# input is the secret code. 
def auth():
    print("Input secret code:")
    input_code = input()
    if input_code == secret_code:
        print("Authorization Succesful\n")
    else:
        print("Authorization Failed\n")
    return input_code == secret_code


def print_balance():
    print("Balance: " + str(balance))


def withdraw(amount):
    global balance
    if amount > balance:
        print("You don't have enough money.")
    else:
        balance = balance - amount


def main():
    while authorized is False:
        auth()
    
    print_balance()

main()


