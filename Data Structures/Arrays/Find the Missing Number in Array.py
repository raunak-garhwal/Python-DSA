def find_missing_number(arr, n):
    total = n * (n + 1) // 2
    return total - sum(arr)

n = int(input("Enter N: "))
arr = list(map(int, input("Enter array elements (1 to N with one missing): ").split()))
print("Missing Number:", find_missing_number(arr, n))
