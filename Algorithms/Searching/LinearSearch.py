def linear_search(my_list,target_value):
    n=len(my_list)
    for j in range(n):
        if my_list[j] == target_value:
            return j
    return -1

my_list = list(map(int,input("\nEnter the elements in the list : ").split()))

print(f"\nElements in the list are {my_list}")
         
target_value = int(input("\nEnter the element to search in the list : "))

result = linear_search(my_list,target_value)

if result == -1:
    print(f"\nElement {target_value} not found in the list.")
else:
    print(f"\nElement {target_value} found at index {result}.")