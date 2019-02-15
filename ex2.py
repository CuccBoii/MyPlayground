
# gets a list from input number after number.
# prints the sum of the list.
def sumListOneByOne():
    print("Enter a number. To stop enter the word \"stop\"")
    listOfNums = []
    num = input()
    while str(num) != "stop":
        listOfNums.append(int(num))
        num = input()
    print("\nSum is: "+ str(sum(listOfNums))+"\n")


# gets a list of numbers from input that is delimited by commas.
# prints the sum of the list.
def sumListAllinOne():
    separator = ","
    mylist = map(int, input("Enter a list of numbers delimited by commas.\n").split(separator)) 
    print("The sum of numbers is: "+str(sum(mylist)))
    

def main():
    sumListOneByOne()
    sumListAllinOne()

main()
