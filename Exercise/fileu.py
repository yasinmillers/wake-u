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
    # Using with statement to read the file line by line
'''file=open("new.txt","r")
for line in file:
    print(line) '''
    
    #reading a file and storing its content in a list
'''with open("new.txt","r") as file:
    lines=file.readlines()
    print(lines) '''
    
    # Writing to a file
'''with open("new.txt","w") as file:
    file.write("This is a new line.\n")
    file.write("This is another line.\n") '''
    
    # Appending to a file
'''with open("new.txt","a") as file:
    file.write("This line is appended.\n") '''
    
    # Using try-except to handle file not found error
'''try:
    with open("nonexistent.txt","r") as file:
        data=file.read()
        print(data)
except FileNotFoundError:
    print("The file does not exist.") '''
'''
with open("images.jpeg","rb") as file:
    data=file.read(100)
    print(data)
'''
# Writing binary data to a file
'''
with open("report.txt","w") as file:
    file.write("This is a report file.\n")
    file.write("It contains some sample data.\n")   '''
    

