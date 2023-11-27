import random

# for i in range(5):
#     random.seed(11)
#     print(random.random())

# print(random.randint(1, 99))

random_num = random.randint(1, 99)
num2 = int(input("введите число: "))

while num2 != random_num:
    if num2 > random_num:
        print("загаданное число меньше")
    else:
        print("загаданное число больше")
    num2 = int(input("введите число: "))

print("вы угадали")
