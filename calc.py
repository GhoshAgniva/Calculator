def add():
    first_input=int(input("Enter the first input: "))
    second_input=int(input("Enter the second input: "))
    addition=first_input+second_input
    print(addition)
    return addition

def sub():
    first_input=int(input("Enter the first input: "))
    second_input=int(input("Enter the second input: "))
    addition=first_input-second_input
    print(addition)
    return addition

def mul():
    first_input=int(input("Enter the first input: "))
    second_input=int(input("Enter the second input: "))
    addition=first_input*second_input
    print(addition)
    return addition

def div():
    first_input=float(input("Enter the first input: "))
    second_input=float(input("Enter the second input: "))
    addition=first_input/second_input
    print(addition)
    return addition

choise=input("choose the oparator: +  -   *  /: ")
if choise=="+":
    add()
elif choise=="-":
    sub()
elif choise=="*":
    mul()
elif choise=="/":
    div()
else:
    print("Invalid Inputs")



