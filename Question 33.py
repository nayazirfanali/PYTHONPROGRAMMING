def permute_unique(nums):
    def backtrack(start):
        if start == len(nums):
            result.append(nums[:])
            return
        used = set()
        for i in range(start, len(nums)):
            if nums[i] in used:
                continue
            nums[start], nums[i] = nums[i], nums[start]
            backtrack(start + 1)
            nums[start], nums[i] = nums[i], nums[start]
            used.add(nums[i])

    nums.sort()
    result = []
    backtrack(0)
    return result

def main():
    nums = [int(x) for x in input("Enter the collection of numbers separated by space: ").split()]
    unique_permutations = permute_unique(nums)
    print("All possible unique permutations:", unique_permutations)

if __name__ == "__main__":
    main()



