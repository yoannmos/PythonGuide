
def add(num1, num2):  # Addition
    return num1+num2


def sub(num1, num2):  # Soustraction
    return num1-num2


def mul(num1, num2):  # Multiplication
    return num1*num2


def div(num1, num2):  # Division
    return num1/num2


def main():  # Main Prog
    start = input("Do you want to make an operation ? Y/N ")
    while(start == "Y"):
        operation = input("What do you want to do ? (+,-,*,/) ")
        if(operation != "+" and operation != "-" and operation != "*" and operation != "/"):
            print("Invalid input operation")
        else:
            num1 = int(input("Num1 "))
            num2 = int(input("Num2 "))
            print("The result is :")
        if(operation == '+'):
            print(add(num1, num2))
        elif(operation == '-'):
            print(add(num1, num2))
        elif(operation == '*'):
            print(add(num1, num2))
        elif(operation == '/'):
            print(add(num1, num2))
        start = input("Do you want to make an other operation ? Y/N ")
    print("Goodbye !")


main()
