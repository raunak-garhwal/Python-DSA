from collections import Counter

def first_non_repeating(s):
    count = Counter(s)
    for char in s:
        if count[char] == 1:
            return char
    return "No unique character found"

s = input("Enter a string: ")
print("First Non-Repeating Character:", first_non_repeating(s))
