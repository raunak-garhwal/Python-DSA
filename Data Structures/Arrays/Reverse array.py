def reverse_array(arr):
    return arr[::-1]

arr = list(map(int, input("Enter array elements: ").split()))
print("Reversed Array:", reverse_array(arr))
