def is_palindrome(s):
    return s == s[::-1]

s = input("Enter a string: ")
print("Is Palindrome:", is_palindrome(s))
