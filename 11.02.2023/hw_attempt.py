import random

options = ["камень", "ножницы", "бумага"]
user_choise = input("ВАШ ВЫБОР(камень, ножницы, бумага):")
computer_choice = random.choice(options)
print(user_choise, computer_choice)
if user_choise == "камень" and computer_choice == "ножницы":
    print("камень ломает ножницы")
    print("you WON!!!! (: the computers are trash")
elif user_choise == "ножницы" and computer_choice == "бумага":
    print("ножницы разрезают бумагу")
    print("you WON!!!(: the computers are trash")
elif user_choise == "бумага" and computer_choice == "камень":
    print("бумага накрывает камень")
    print("you WON!!!(; the computers are trash")
elif user_choise == "ножницы" and computer_choice == "камень":
    print("камень разрушает ножницы")
    print("the computer won you are a LOOOOOOSER ):")
elif user_choise == "камень" and computer_choice == "бумага":
    print("бумага накрывает камень")
    print("the computer won you are a LOOOOOOSER ):")
elif user_choise == "бумага" and computer_choice == "ножницы":
    print("ножницы разрезают бумагу")
    print("the computer won you are a LOOOOOOSER ):")
else:
    print("НИЧЬЯ")
