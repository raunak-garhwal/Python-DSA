n=int(input("\nEnter the size of the tuple : "))
elements=[]
tup=()
replist=[]

for i in range(n):
    value=int(input(f"Enter {i+1} value : "))
    elements.append(value)

tup = tuple(elements)

for i in tup:
    if (tup.count(i))>1:
        if i not in replist:
            replist.append(i)
                  
print("\nThe repeated items is/are:",replist)