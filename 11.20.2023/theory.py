def say_hi(name="ahmed", age=18):
    print(f"hi {name} тебе {age} лет")


# say_hi('rahman', 18)
# say_hi()

# children=['ahmed','rahman','ayhan']
# for i in children:
#     say_hi(i)

# children={'ahmed':14,'rahman':18,'ayhan':14}
# for keys,values in children.items():
#     say_hi(keys,values)

# children = [
#     ["ahmed", 14],
#     ["rahman", 17],
#     ["ayhan", 14],
# ]
# for i in children:
#     say_hi(i[0],i[1])

children = {
    "child0": ["ahmed", 14],
    "child1": ["rahman", 17],
    "child2": ["ayhan", 14],
}

for key, value in children.items():
    say_hi(value[0], value[1])
