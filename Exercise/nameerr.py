#14+ pam*3  

#1 '2'+4

'''try:
    x=int(input("Enter a number: "))
    pass


except ValueError: 
    print("An error occurred: Invalid input. Please enter a valid integer.")
    
n=10
try:
    result=n/0
    print(result)
except:
    print("An error occurred: Division by zero is not allowed.")
    
    
finally:
    print("Execution completed.") x  
    
'''
    

try:
    n=0
    result=10/n
    
    
except ZeroDivisionError:
    print("An error occurred: Division by zero is not allowed.")
    
else:
    
    print(result)
    
finally:
    print("Execution completed.")