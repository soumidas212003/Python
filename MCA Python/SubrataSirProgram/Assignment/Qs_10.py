n = int(input("Enter the length of the list: ")) 
list = []
for i in range(n):
    element = input(f"Enter the element {i+1}: ")
    list.append(element)

print("List elements are:", list)

# Reverse the list using slicing
reverse_list = list[::-1]

print("After reversing, the list is:", reverse_list)
