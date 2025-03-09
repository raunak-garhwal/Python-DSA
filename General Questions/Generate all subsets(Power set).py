def generate_subsets(nums, index=0, subset=[]):
    if index == len(nums):
        print(subset)
        return
    generate_subsets(nums, index + 1, subset + [nums[index]])  # Include
    generate_subsets(nums, index + 1, subset)  # Exclude

nums = list(map(int, input("Enter numbers separated by space: ").split()))
generate_subsets(nums)
