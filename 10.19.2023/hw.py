# Написать калькулятор с использованием sys.argv
# 1) если sys.argv пустой, то должна выводиться ошибка
# 2) все 4 операции (+, -, *, /)
# 3) только для 2 чисел
# 4) если строка, то ошибка

from sys import *

num1 = input()

if num1 == "+":
    print(int(argv[1]) + int(argv[2]))
