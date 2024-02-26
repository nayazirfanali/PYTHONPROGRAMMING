def nth_largest_number(nums, n):
    unique_nums = list(set(nums))
    unique_nums.sort(reverse=True)
    if 1 <= n <= len(unique_nums):
        return unique_nums[n - 1]
    else:
        return "N is out of range"

number_list = [14, 67, 48, 23, 5, 62]
N = 1

result = nth_largest_number(number_list, N)
print(f"The {N}th largest number in the list is: {result}")
