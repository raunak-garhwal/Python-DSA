def remove_duplicates(arr):
    return sorted(set(arr))

arr = list(map(int, input("Enter sorted array elements: ").split()))
print("Array without duplicates:", remove_duplicates(arr))
