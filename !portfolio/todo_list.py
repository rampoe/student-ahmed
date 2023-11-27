import time

to_do_list = []


def create():
    task_name = input("введите название задачи: ")
    print("добавляем...")
    time.sleep(2)
    to_do_list.append(task_name)
    print("сохранено")


def read():
    counter = 0
    for i in to_do_list:
        counter += 1
        print(f"{counter}. {i} ")


def update():
    print("введите номер задачи: ")
    task_num = int(input()) - 1
    task_name = input("введите новое название задачи: ")
    to_do_list[task_num] = task_name


def delete():
    task_num = int(input("введите номер задачи: ")) - 1
    del to_do_list[task_num]


while True:
    print(
        """выберите действие:
    1. создать задачу
    2. посмотреть список задач
    3. изменить задачу
    4. удалить задачу"""
    )
    choice = int(input("что вы хотите сделать? "))

    if choice == 1:
        create()
    elif choice == 2:
        read()
    elif choice == 4:
        delete()
    elif choice == 3:
        update()

# ["ahmed", "rahman"]

# 1. ahmed
# 2. rahman
# 3. task3
