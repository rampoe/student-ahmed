a = int(input("Введите длину комнаты: "))
b = int(input("Введите ширину комнаты: "))
c = int(input("Введите высоту комнаты: "))

s = 2 * a  * b + 2 * b * c + 2 * a * c - 5

print(f"Понадобится {s} кв.метров обоев")