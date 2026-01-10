#Merge two lists and remove duplicates
list1 = [1, 2, 3, 4, 5]
list2 = [4, 5, 6, 7, 8]
merged_list = list1 + list2
unique_merged_list = list(set(merged_list))
print("Merged list without duplicates:", unique_merged_list)