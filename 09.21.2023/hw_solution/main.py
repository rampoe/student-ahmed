numbersAmount = int(input("how many numbers do you want to enter? "))

if numbersAmount == 2:
    num1 = int(input("enter the first number: "))
    num2 = int(input("enter the second number: "))
    operation = input("enter the operation: ")
    if operation == "+":
        print(f"{num1} + {num2} = {num1 + num2}")
    elif operation == "-":
        print(f"{num1} - {num2} = {num1 - num2}")
    else:
        print(f"{num1} / {num2} = {num1 / num2}")
elif numbersAmount == 3:
    num1 = int(input("enter the first number: "))
    num2 = int(input("enter the second number: "))
    num3 = int(input("enter the third number: "))
    operation = input("enter the operation: ")
    if operation == "+":
        print(f"{num1} + {num2} + {num3} = {num1 + num2 + num3}")
    elif operation == "-":
        print(f"{num1} - {num2} - {num3} = {num1 - num2 - num3}")
    else:
        print(f"{num1} / {num2} / {num3} = {num1 / num2 / num3}")
elif numbersAmount == 4:
    num1 = int(input("enter the first number: "))
    num2 = int(input("enter the second number: "))
    num3 = int(input("enter the third number: "))
    num4 = int(input("enter the forth number: "))
    operation = input("enter the operation: ")
    if operation == "+":
        print(f"{num1} + {num2} + {num3} + {num4} = {num1 + num2 + num3 + num4}")
    elif operation == "-":
        print(f"{num1} - {num2} - {num3} - {num4} = {num1 - num2 - num3 - num4}")
    else:
        print(f"{num1} / {num2} / {num3} / {num4} = {num1 / num2 / num3 / num4}")
else:
    print("sorry! an error occured...")
