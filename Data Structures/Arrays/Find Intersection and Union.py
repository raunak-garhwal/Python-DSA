def find_union_intersection(arr1, arr2):
    union = sorted(set(arr1) | set(arr2))
    intersection = sorted(set(arr1) & set(arr2))
    return union, intersection

arr1 = list(map(int, input("Enter first sorted array: ").split()))
arr2 = list(map(int, input("Enter second sorted array: ").split()))
union, intersection = find_union_intersection(arr1, arr2)
print("Union:", union)
print("Intersection:", intersection)
