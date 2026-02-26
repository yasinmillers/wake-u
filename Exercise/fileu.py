'''
file=open("new.txt","r")
data=file.read()
print(data)
file.close()'''


with open("new.txt","r") as file:
    data=file.read()
    print(data) 