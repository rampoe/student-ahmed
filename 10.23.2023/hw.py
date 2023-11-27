import random

# есть следующий словарь:
contacts = {
    "Rahman": "+993654654654",
    "Ahmed": "+993321321321",
    "Ayhan": "+993987987987",
    "Rampoe": "+99365000000",
    "Spam": "+9936161616161",
}

# при каждом нажатии enter должен показываться один рандомный контакт
# показанный контакт должен удаляться из словаря и никогда не должен показываться снова
# программа должна прекращать свое исполнение как только все контакнты были показаны и удалены

while contacts:
    keys_array = list(contacts)
    random_key = keys_array[random.randint(0, len(keys_array) - 1)]
    print(f"{random_key}: {contacts[random_key]}")
    input()
    del contacts[random_key]

print("finish!")
