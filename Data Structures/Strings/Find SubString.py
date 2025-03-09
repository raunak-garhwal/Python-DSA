def find_substring(text, pattern):
    return text.find(pattern)

text = input("Enter the main text: ")
pattern = input("Enter the substring to find: ")
index = find_substring(text, pattern)
print(f"Substring found at index {index}" if index != -1 else "Substring not found")
