from itertools import permutations

def find_permutations(s):
    return [''.join(p) for p in permutations(s)]

s = input("Enter a string: ")
print("All Permutations:", find_permutations(s))
