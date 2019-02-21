from functools import reduce

# gets an id number as input, prints if its valid or not.
def is_id_valid():
    string = input("Enter id number:\n")
    print("valid") if (sum(list(map(lambda x, y: int(x) + (int(y)*2 if int(y)*2 <= 9 else int(y)*2 - 9) ,string[0:7:2], string[1:8:2])))+int(string[8])) % 10 == 0 else print("Not valid")

is_id_valid()