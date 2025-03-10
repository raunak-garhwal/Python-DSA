elements = list(map(int,input("\nEnter the elements of the tuple : ").split()))

replist=[]

tup = tuple(elements)

for i in tup:
    if (tup.count(i))>1:
        if i not in replist:
            replist.append(i)
                  
print("\nThe repeated items is/are:",replist)