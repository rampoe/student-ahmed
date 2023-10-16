contacts = {}

def read(contact_book):
    for key, value in contact_book.items():
        print(f"{key}: {value}")
    

def create(name, phone):
    contacts[name] = phone


# def update():

# def delete():

create("Rahman", "+99362172337")
print(contacts["Rahman"])