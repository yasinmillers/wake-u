import os
import sys

files= os.listdir()
for file in files:
    if os.path.isfile(file):
        print(file)
    else:
        print(f"{file} is a directory") 