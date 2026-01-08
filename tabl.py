#multiplication table
num = int(input("Enter a number to display its multiplication table: "))    
for i in range(1, 14):
    print(num, "x", i, "=", num * i)    \
        
 #factorial of a number
n = int(input("Enter a number to find its factorial: "))
factorial = 1
for i in range(1, n + 1):
    factorial *= i
print("The factorial of", n, "is", factorial)
# Check if a number is prime
num = int(input("Enter a number to check if it is prime: "))
is_prime = True
if num <= 1:
    is_prime = False
else:
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            is_prime = False
            break
if is_prime:
    print(num, "is a prime number.")
else:
    print(num, "is not a prime number.")       