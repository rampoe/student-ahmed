# what_is_this = {
#     "name": "Ahmed",
#     "age": 16,
# }

# print(type(what_is_this))  # dict = dictionary = словарь

# does_dict_have_length = {
#     "first": "first_item",
#     "second": "second_item",
# }

# print(len(does_dict_have_length))  # 2
# print()

# sample_dict = {
#     "name": "Rahman",
#     "age": 17,
#     "birth_year": 2006,
#     "nationality": "turkmen",
#     "spam": "this is spam and needs to be deleted",
# }

# print(sample_dict)

# del sample_dict["spam"]  # удаляем spam из sample_dict

# print(sample_dict)
# print()

# for key in sample_dict:  # работаем с ключами
#     print(key)
# print()

# for key in sample_dict.keys():  # работаем с ключами
#     print(key)
# print()

# for value in sample_dict.values():  # работаем со значениями
#     print(value)
# print()

# for key, value in sample_dict.items():  # работаем с ключами и значениями
#     print(f"{key} : {value}")
# print()

# print("likes_ice_cream" in sample_dict)  # False
# print("birth_year" in sample_dict)  # False

# if "name" in sample_dict:
#     print('Yes "name" is in sample_dict')

# sample_dict["likes_ice_cream"] = True  # добавляем новый элемент в словарь

# print("likes_ice_cream" in sample_dict)  # True
# print()

# # Основные возможности последовательностей – это проверка
# # принадлежности (т.е. выражения “in” и “not in”)и оператор индексирования

# shoplist = ["яблоки", "манго", "морковь", "бананы"]
# name = "Ahmed"

# # Операция индексирования
# print("Элемент 0 -", shoplist[0])
# print("Элемент 1 -", shoplist[1])
# print("Элемент 2 -", shoplist[2])
# print("Элемент 3 -", shoplist[3])
# print("Элемент -1 -", shoplist[-1])
# print("Элемент -2 -", shoplist[-2])

# print("Символ 0 -", name[0])

# # Вырезка из списка
# print("Элементы с 1 по 3:", shoplist[1:3])
# print("Элементы с 2 до конца:", shoplist[2:])
# print("Элементы с 1 по -1:", shoplist[1:-1])
# print("Элементы от начала до конца:", shoplist[:])

# print(name[0])
# print(name[-1])
# print(name[1:-1])
# print(name[0:-1:2])
# print(name[::2])
# print(name[::-1])

# print(shoplist[::-1])
# print()

this_is_a_set = set(["Бразилия", "Россия", "Индия"])
print("Индия" in this_is_a_set)

this_is_a_copy = this_is_a_set.copy()
print(this_is_a_copy)

this_is_a_copy.add("Китай")
print(this_is_a_copy)
