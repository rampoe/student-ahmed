contacts = {}

print("read")
print("create")
print("update")
print("delete")
print("exit")

while True:
    num1 = input()

    if num1 == "read":
        for key, value in contacts.items():
            print(f"{key}:{value}")

    if num1 == "create":
        name = input()
        phone = input()

        contacts[name] = phone

    if num1 == "update":
        name = input()
        phone = input()

        if name in contacts.keys():
            contacts[name] = phone
        else:
            print(
                f"Контакта с именем {name} нету. Сначала создайте, а потом можете изменить!"
            )

    if num1 == "delete":
        name = input()

        if name in contacts.keys():
            del contacts[name]
        else:
            print(
                f"Контакта с именем {name} нету. Сначала создайте, а потом можете удалить!"
            )

    if num1 == "exit":
        break
