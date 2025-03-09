def rotate_array(arr, k, direction):
    k %= len(arr)  # Handle cases where k > len(arr)
    if direction == "left":
        return arr[k:] + arr[:k]
    else:
        return arr[-k:] + arr[:-k]

arr = list(map(int, input("Enter array elements: ").split()))
k = int(input("Enter rotation count: "))
direction = input("Enter direction (left/right): ").strip().lower()
print("Rotated Array:", rotate_array(arr, k, direction))
