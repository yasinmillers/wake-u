'''
file=open("new.txt","r")
data=file.read()
print(data)
file.close()'''

# Using with statement to read the file for better resource management
'''
with open("new.txt","r") as file:
    data=file.read()
    print(data) '''
    
file=open("new.txt","r")
for line in file:
    print(line) 