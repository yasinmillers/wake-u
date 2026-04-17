import os


path = "."  # current directory

items = os.listdir(path)

for item in items:
    print(item)