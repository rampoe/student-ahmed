import random
import time

print("вы идете по темному густому лесу ")
print("перед собой вы видите 2 пещеры в какую пойдете?")

while True:
    choice = input("1 или 2_ ")
    comp = random.randint(1, 2)

    print("вы заходите в пещеру")
    time.sleep(2)
    print("вы видите большого дракона")
    time.sleep(2)
    print("он открывает рот и ...")
    time.sleep(4)
    if choice != comp:
        print("моментально съедает вас")
    else:
        print("отдает вам свои сокровища")
    flag = input("хотите начать игру заново да или нет  ")
    if flag == "нет":
        break
