
def sumListOneByOne():
    print("Enter a number. To stop enter the word \"stop\"")
    listOfNums = []
    num = input()
    while str(num) != "stop":
        listOfNums.append(int(num))
        num = input()
    return sum(listOfNums)


def main():
    print("\nSum is: "+ str(sumListOneByOne())+"\n")

main()