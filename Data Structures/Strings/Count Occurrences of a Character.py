def count_occurrences(s, char):
    return s.count(char)

s = input("Enter a string: ")
char = input("Enter the character to count: ")
print(f"Occurrences of '{char}':", count_occurrences(s, char))
