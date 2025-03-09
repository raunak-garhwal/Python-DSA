n=int(input("\nEnter the total number of element in the list : "))
if(n<=0):
    print("\nThe list is empty, Please enter a valid number greater than 0")
else:
    num_list=[]
    for i in range(n):
        value=int(input(f"Enter {i+1} element : "))
        num_list.append(value)

    maximum = minimum = num_list[0]
    for i in num_list:
        if(maximum<i):
            maximum=i
        if(minimum>i):
            minimum=i

    print("\nList of elements :",num_list)
    print("\nMaximum value from the list :",maximum)
    print("\nMinimum value from the list :",minimum)