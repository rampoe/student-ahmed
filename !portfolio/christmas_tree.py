# print(
#     """
#     *
#    ***
#   *****
# *********
#    | |
#     """
# )


def tree(height):
    for i in range(1, height):
        spaces = " " * (height - i)
        stars = "*" * (2 * i - 1)
        print(spaces + stars)

    bottom = " " * (height - 2)
    print(bottom + "| |")


height = int(input("какую высоту вы хотите?"))
tree(height)
