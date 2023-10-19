# Переписать код контактной книжки без использования функций.
# ===========================================================

contacts = {}
num1 = input()
print("read")
print("create")
print("update")
print("delete")
print("exit")
if num1 == "read":
    for key, value in contacts.items():
        print(f"{key}:{value}")
if num1 == "create":
    name = input()
    phone = input()
    contacts[name] = phone
if num1 == "update":
    global name
    if name in contacts.keys():
        contacts[name] = phone
    else:
        print(
            f"Контакта с именем {name} нету. Сначала создайте, а потом можете изменить!"
        )
if num1 == "delete":
    del contacts[name]
else:
    print(f"Контакта с именем {name} нету. Сначала создайте, а потом можете удалить!")
