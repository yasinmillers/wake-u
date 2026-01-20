#Find pair whose sum is given number
def find_pair(arr, target):
    num_dict = {}
    for num in arr:
        complement = target - num
        if complement in num_dict:
            return (complement, num)
        num_dict[num] = True
    return None


arr = list(map(int, input("Enter numbers separated by spaces: ").split()))
target = int(input("Enter the target sum: "))

result = find_pair(arr, target)
if result:
    print("Pair found:", result)
else:
    print("No pair found")
