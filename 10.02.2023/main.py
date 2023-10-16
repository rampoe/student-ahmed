# name = "Rahman"
# def sayHi():
#     print(name)
# sayHi()

# x = 50
# def func():
#     global x
#     print("x is", x)
#     x = 2
#     print("changed global x to", x)
# func()
# print("Value of x is", x)


# # глобальная область видимости
# def func_outer():
#     # нелокальная область видимости
#     x = 2
#     print("x равно", x)
#     def func_inner():
#         # локальная область видимости
#         nonlocal x
#         x = 5
#     func_inner()
#     print("Локальное x сменилось на", x)
# func_outer()


# def sayHi(name="пользователь"):
#     print(f"Привет, {name}!")
# sayHi()


# def summa(num1="не ", num2="знаю"):  # значения аргументов по умолчанию
#     print(num1 + num2)
# summa()


# def func(a, b=5, c=10):
#     print("a is", a, "and b is", b, "and c is", c)
# func(3, 7)
# func(25, c=24)
# func(c=50, a=100)

# correct_login = "rahman"
# correct_password = "1234"

# login = input("enter your login: ")
# password = input("enter your password: ")
# age = int(input("enter your age: "))

# if login == correct_login and password == correct_password and age > 17:
#     print("доступ разрешен")
# else:
#     print("доступ запрещен")
