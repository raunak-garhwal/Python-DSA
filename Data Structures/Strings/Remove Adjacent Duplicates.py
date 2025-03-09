def remove_adjacent_duplicates(s):
    stack = []
    for char in s:
        if stack and stack[-1] == char:
            stack.pop()
        else:
            stack.append(char)
    return ''.join(stack)

s = input("Enter a string: ")
print("After Removing Adjacent Duplicates:", remove_adjacent_duplicates(s))
