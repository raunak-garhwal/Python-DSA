def find_min_max(arr):
    return min(arr), max(arr)

arr = list(map(int, input("Enter array elements: ").split()))
min_val, max_val = find_min_max(arr)
print("Minimum:", min_val, "Maximum:", max_val)
