from sys import argv

num1 = input("Введите оператор: ")

if num1 == "+":
    print(int(argv[1]) + int(argv[2]))
elif num1 == "-":
    print(int(argv[1]) - int(argv[2]))
elif num1 == "*":
    print(int(argv[1]) * int(argv[2]))
elif num1 == "/":
    print(int(argv[1]) / int(argv[2]))
