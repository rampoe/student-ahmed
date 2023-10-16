contacts = {}


def read(contact_book):
    for key, value in contact_book.items():
        print(f"{key}: {value}")


def create(name, phone):
    contacts[name] = phone


def update(name, phone):
    if name in contacts.keys():
        contacts[name] = phone
    else:
        print(f"Контакта с именем {name} нету. Сначала создайте, а потом можете изменить!")


def delete(name):
    if name in contacts.keys():
        del contacts[name]
    else:
        print(f"Контакта с именем {name} нету. Сначала создайте, а потом можете удалить!")


print("1. read")
print("2. create")
print("3. update")
print("4. delete")
print("0. exit")

while True:
    option = int(input("Выберите действие: "))

    if option == 1:
        read(contacts)
    elif option == 2:
        name = input("введите имя нового контакта ")
        phone = input("введите номер нового контакта ")
        create(name, phone)
    elif option == 3:
        name = input("чей номер вы хотите изменить? ")
        phone = input(f"введите новый номер {name}: ")
        update(name, phone)
    elif option == 4:
        name = input("кого вы хотите удалить? ")
        delete(name)
    elif option == 0:
        break
    else:
        print("я не знаю такой команды!!")
