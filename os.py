import os


path = "."  # current directory

items = os.listdir(path)

for item in items:
    file = os.path.join(path, item)
    if os.path.isfile(file):
        print("file:", item)
    elif os.path.isdir(file):
        print("directory:", item)
        
        
        
print(" Current WorkingDirectory:")
print(os.getcwd())
print("\ Files in CurrentDirectory:")
files = os.listdir()
for file in files:
    if os.path.isfile(file):
        print(" File:", file)
else:
    print(" Folder:", file)