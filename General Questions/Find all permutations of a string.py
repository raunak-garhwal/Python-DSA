def permutations(arr, l=0):
    if l == len(arr):
        print("".join(arr))
        return
    for i in range(l, len(arr)):
        arr[l], arr[i] = arr[i], arr[l]  # Swap
        permutations(arr, l + 1)
        arr[l], arr[i] = arr[i], arr[l]  # Backtrack

s = input("\nEnter a string: ")
permutations(list(s))
