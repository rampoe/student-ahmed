# def total(initial=5, *numbers, **keywords):
#     count = initial
#     for number in numbers:
#         count += number
#     for key in keywords:
#         count += keywords[key]
#     print(count)


# total(10, 1, 2, 3, vegetables=50, fruits=100)

# =============================================

# def total(**keywords):
#     for key, value in keywords.items():
#         print(f"{key}: {value}")

# total(vegetables=50, fruits=100)

# =============================================

# def summa(a, b, c):
#     print(a + b + c)

# summa(1, 2, 3)

# def summa(*arg, a, b, c):
#     """эта функция выводит сумма"""
#     print(a + b + c)

# print(summa.__doc__)

