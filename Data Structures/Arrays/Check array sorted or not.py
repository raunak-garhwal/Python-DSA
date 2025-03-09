def is_sorted(arr):
    return arr == sorted(arr)

arr = list(map(int, input("Enter array elements: ").split()))
print("Is Sorted:", is_sorted(arr))
