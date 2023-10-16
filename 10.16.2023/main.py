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
        print("Этого контакта нету. Сначала создайте, а потом можете изменить!")
    

def delete(name):
    del contacts[name]


print("1. read")
print("2. create")
print("3. update")
print("4. delete")

option = int(input("Выберите действие: "))
