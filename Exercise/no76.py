#Function that accepts list and returns even list
def get_even_numbers(numbers):
    even_numbers = []
    for num in numbers:
        if num % 2 == 0:
            even_numbers.append(num)
    return even_numbers 

number=list(map(int,input("Enter numbers separated by space: ").split()))
even_list = get_even_numbers(number)
print("Even numbers:", even_list)