def recursionSum(nums):
    if len(nums) == 1:
        return nums[0]
    else:
        return nums[0] + recursionSum(nums[1::])


if __name__ == "__main__":
    print(recursionSum([1, 2, 3]))
