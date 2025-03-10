line=input("\nEnter a sentence : ")

word_list=line.split()

frequency_count={}
for i in word_list:
    if i in frequency_count:
        frequency_count[i]+=1
    else:
        frequency_count[i]=1

print(f"\nThe sentence is :",line)

count=1
for words in line:
    if(words==" "):
        count+=1

print("\nThe total number of words in the sentence are :",count)

print("\nThe frequency of elements in the list :- ")
for key,value in frequency_count.items():
    print(f"{key} -> {value}")