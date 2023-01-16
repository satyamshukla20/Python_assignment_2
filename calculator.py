def add(a,b):
    print(a+b)
def sub(a,b):
    print(a-b)
def mul(a,b):
    print(a*b)
def div(a,b):
    try:
        print(a/b)
    except ZeroDivisionError as e:
        print(e)
try:  
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))
    print("What do you want to operate?")
    print("Enter 1 for Addition")
    print("Enter 2 for Subtraction")
    print("Enter 3 for Multiplication")
    print("Enter 4 for Division")
    op = int(input("Enter the number for operation: "))
    if(op==1):
        add(num1, num2)
    elif(op == 2):
        sub(num1,num2)
    elif(op==3):
        mul(num1, num2)
    elif(op==4):
        div(num1, num2)
    else:
        print("You entered invalid input")
except ValueError as e:
    print("Enter valid Integer")