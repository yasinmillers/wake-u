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
'''


a=['10',"twenty","30"]  
try:
   total =int(a[0]) + int(a[1]) + int(a[2])
   print("Total:", total)
except NameError as e:
   print("An error occurred:", e)
except ValueError as e:
   print("An error occurred:", e)
except Exception as e:
   print("An unexpected error occurred:", e)    
except IndexError as e:
   print("An error occurred:", e)
except TypeError as e:
   print("An error occurred:", e)   
finally:
   print("Execution completed.")
    
    