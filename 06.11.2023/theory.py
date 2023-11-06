what_is_this = {
    "name": "Ahmed",
    "age": 16,
}

print(type(what_is_this))  # dict = dictionary = словарь

does_dict_have_length = {
    "first": "first_item",
    "second": "second_item",
}

print(len(does_dict_have_length))  # 2
print()

sample_dict = {
    "name": "Rahman",
    "age": 17,
    "birth_year": 2006,
    "nationality": "turkmen",
    "spam": "this is spam and needs to be deleted",
}

print(sample_dict)

del sample_dict["spam"]  # удаляем spam из sample_dict

print(sample_dict)
print()

for key in sample_dict:  # работаем с ключами
    print(key)
print()

for key in sample_dict.keys():  # работаем с ключами
    print(key)
print()

for value in sample_dict.values():  # работаем со значениями
    print(value)
print()

for key, value in sample_dict.items():  # работаем с ключами и значениями
    print(f"{key} : {value}")
print()

print("likes_ice_cream" in sample_dict)
print("birth_year" in sample_dict)

if "name" in sample_dict:
    print('Yes "name" is in sample_dict')

sample_dict["likes_ice_cream"] = True  # добавляем новый элемент в словарь

print("likes_ice_cream" in sample_dict)
