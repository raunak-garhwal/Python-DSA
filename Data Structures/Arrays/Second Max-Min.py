def second_largest_smallest(arr):
    unique_arr = sorted(set(arr))
    if len(unique_arr) < 2:
        return "Not enough unique elements"
    return unique_arr[1], unique_arr[-2]

arr = list(map(int, input("Enter array elements: ").split()))
res = second_largest_smallest(arr)
print("Second Smallest:", res[0], "Second Largest:", res[1])
