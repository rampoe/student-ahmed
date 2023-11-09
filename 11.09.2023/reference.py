# Простое присваивание

# shoplist = ["яблоки", "манго", "морковь", "бананы"]
# mylist = shoplist

# del shoplist[0]

# print(f"shoplist: {shoplist}")
# print(f"mylist: {mylist}")

# ===============================

# Копирование при помощи полной вырезки

# shoplist = ["яблоки", "манго", "морковь", "бананы"]
# mylist = shoplist

# mylist = shoplist[:]

# del shoplist[0]

# print(f"shoplist: {shoplist}")
# print(f"mylist: {mylist}")

# ===============================

# print(type("hello"))

# ===============================

name = "Ayhan"

if name.find("hm") != -1:
    print(f'Find returned {name.find("hm")}')
    print('Yes "hm" is in name')
else:
    print(f'Find returned {name.find("hm")}')
    print('No, "hm" is not in name')

delimeter = " -- "

mylist = ["Russia", "France", "Germany"]

print(delimeter.join(mylist))
