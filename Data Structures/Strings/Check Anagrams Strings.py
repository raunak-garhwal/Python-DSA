from collections import Counter

def are_anagrams(s1, s2):
    return Counter(s1) == Counter(s2)

s1 = input("Enter first string: ")
s2 = input("Enter second string: ")
print("Are Anagrams:", are_anagrams(s1, s2))
