database = {}

valid_lessons = [
    "math",
    "computer science",
    "pe",
    "russian",
    "algebra",
    "geometry",
    "culture",
    "chemistry",
]


def check_lesson(lesson):
    if lesson in valid_lessons:
        return True
    return False


def get_lessons():
    while True:
        new_lesson = input("Enter a lesson (press Enter to exit): ")
        if new_lesson == "":
            break
        if check_lesson(new_lesson):
            database[new_lesson] = None


get_lessons()


def get_marks():
    for key in database.keys():
        new_mark = int(input("Enter new mark: "))
        database[key] = new_mark


get_marks()


count = 0
for key, value in database.items():
    count += 1
    print(f"\n{count}. {key}: {value}")
