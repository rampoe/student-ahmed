# Написать программу, которая переводит часы в секунды. К примеру, если вводится 2, должно вывестись 7200, так как в 2 часах 7200 секунд.


def hours_to_sec(hours):
    print(hours, "=", 3600 * hours, "секунд")


hours = int(input("введите часы: "))
hours_to_sec(hours)