# def total(initial=5, *numbers):
#     count = initial
#     for number in numbers:
#         count += number
#     print(count)

# total(10, 1, 2, 3)

# =================================

# def add(num1, num2):
#     if num1 == 7:
#         return "number 1 should not be 7"
#     else:
#         return num1 + num2

# =================================

# def add(num1, num2):
#     return num1 + num2

# test = 3 + add(7, 10)

# print(test)

# =================================

# def check_login(login):
#     # if login == "rampoe":
#     #     return True
#     # else:
#     #     return False
#     return login == "rampoe"

# login = input("enter your login: ")

# if check_login(login):
#     print("login is correct")
# else:
#     print("login is wrong")

# =================================

# def count_8():
#     for i in range(5):
#         if i == 8:
#             return
#         print(i + 1)

# count_8()

# =================================

# def total(*numbers, initial=5):
#     count = initial
#     for number in numbers:
#         count += number
#     print(count)

# total(10, 1, 2, 3)

# =================================

# numbers = [1, 3, 5, 7]

# def total(initial=5, *numbers):
#     count = initial
#     for number in numbers:
#         count += number
#     return count

# =================================

# slovar = {
#     "Rahman": 2006,
#     "Ahmed": 2009,
# }

# print(slovar["Rahman"])

# =================================

# guests = {}

# def check_guest(name):
#     if guests.get(name):
#         print("ne vhodi")
#     else:
#         guests[name] = True
#         print("welcome!")

# check_guest("rahman")
# check_guest("ahmed")
# check_guest("rahman")