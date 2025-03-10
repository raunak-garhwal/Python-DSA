input_list = list(map(int,input("\nEnter the elements in the list : ").split()))

count_zero = count_pos = count_neg = 0

for i in input_list:
    if(i==0):
        count_zero+=1
    elif(i>0):
        count_pos+=1
    else:
        count_neg+=1

print("\nThe elements in the list :",input_list)
print("\nCount of zeros :",count_zero)
print("Count of positive numbers :",count_pos)
print("Count of negative numbers :",count_neg)