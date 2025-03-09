n=int(input("\nEnter the total number of element in the list : "))

num_list=[]

for i in range(n):
    value=int(input(f"Enter {i+1} element : "))
    num_list.append(value)    

even_list=[i for i in num_list if i%2==0]
odd_list=[i for i in num_list if i%2!=0]

# for i in num_list:
#     if(i%2==0):
#         even_list.append(i)
#     else:
#         odd_list.append(i)

print("\nList of All Numbers :",num_list)
print("\nList of Even Numbers :",even_list)
print("\nList of Odd Numbers :",odd_list)