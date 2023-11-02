import random

options = ["камень", "ножницы", "бумага"]

user_choice = input("ваш выбор (камень, ножницы, бумага): ")
computer_choice = random.choice(options)
