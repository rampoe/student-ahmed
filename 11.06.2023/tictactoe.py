import random


def pc_or_player():
    choice = int(input("1. PC , 2. Player"))
    if choice == 1:
        return "PC"
    return "Player"


symbol = input("x or o : ")

answer = input("ARE YOU READY? y or n: ")

if answer == "y":
    pass
