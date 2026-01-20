#Find pair whose sum is given number
def find_pair(arr, target):
    num_dict = {}
    for i, num in enumerate(arr):
        complement = target - num
        if complement in num_dict:
            return (num_dict[complement], i)
        num_dict[num] = i
    return None

# Example usage:
#arr = [2, 7, 11, 15]
arr= list(map(int, input("Enter numbers separated by spaces: ").split()))
target = int(input("Enter the target sum: ")) 
  
result = find_pair(arr, target)
if result:
    print(f"Pair found at indices {result}")
else:
    print("No pair found")