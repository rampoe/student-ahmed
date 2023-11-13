import os

count = 0
for i in os.listdir():
    if i != "main.py":
        os.rename(i, f"rahman{count}.js")
        count += 1
