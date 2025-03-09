def find_subarray_sum(arr, target):
    start, curr_sum = 0, 0
    for end in range(len(arr)):
        curr_sum += arr[end]
        while curr_sum > target and start <= end:
            curr_sum -= arr[start]
            start += 1
        if curr_sum == target:
            return arr[start:end + 1]
    return "No subarray found"

arr = list(map(int, input("Enter array elements: ").split()))
target = int(input("Enter target sum: "))
print("Subarray with sum:", find_subarray_sum(arr, target))
