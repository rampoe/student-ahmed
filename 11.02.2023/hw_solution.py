import random

options = ["камень", "ножницы", "бумага"]
user_choice = input("ВАШ ВЫБОР (камень, ножницы, бумага): ").lower()
computer_choice = random.choice(options)

print(f"Ваш выбор: {user_choice}")
print(f"Выбор компьютера: {computer_choice}")

if user_choice == computer_choice:
    print("НИЧЬЯ")
elif (
    (user_choice == "камень" and computer_choice == "ножницы")
    or (user_choice == "ножницы" and computer_choice == "бумага")
    or (user_choice == "бумага" and computer_choice == "камень")
):
    print(f"{user_choice} побеждает {computer_choice}")
    print("Вы выиграли! (: Компьютер - лузер")
else:
    print(f"{computer_choice} побеждает {user_choice}")
    print("Компьютер выиграл. Вы проиграли. ):")
