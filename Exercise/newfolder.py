import os
print("Current working directory:", os.getcwd())

folder_name = "love_birds"
if not os.path.exists(folder_name):
    os.mkdir(folder_name)
    print(f"Folder '{folder_name}' created.")
else:
    print(f"Folder '{folder_name}' already exists.")    
    
    