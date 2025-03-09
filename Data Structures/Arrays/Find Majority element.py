def majority_element(arr):
    count, candidate = 0, None
    for num in arr:
        if count == 0:
            candidate = num
        count += (1 if num == candidate else -1)

    if arr.count(candidate) > len(arr) // 2:
        return candidate
    return "No Majority Element"

arr = list(map(int, input("Enter array elements: ").split()))
print("Majority Element:", majority_element(arr))
