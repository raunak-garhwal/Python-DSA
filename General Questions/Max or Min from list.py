num_list = list(map(int,input("\nEnter the elements of the list separated by space : ").split()))

maximum = minimum = num_list[0]

for i in num_list:
    if(maximum<i):
        maximum=i
    if(minimum>i):
        minimum=i

print("\nList of elements :",num_list)
print("\nMaximum value from the list :",maximum)
print("\nMinimum value from the list :",minimum)