#Write a recursive function (a function that calls itself) to
#6count down from N to 0.
def countdown(n):
    if n == 0:
        print("Blast off!")
    else:
        print(n)
        countdown(n - 1)
number = int(input("Enter a number: "))
countdown(number)