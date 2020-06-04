def insertionsort(nums: list) -> list:
    for i in range(1, len(nums)):
        position = i
        value = nums[i]
        while position > 0 and nums[position - 1] > value:
            nums[position] = nums[position - 1]
            position = position - 1
        nums[position] = value
    return nums


if __name__ == "__main__":
    import numpy as np

    ls = np.random.normal(4, 2, 10)
    result = [int(x) for x in ls]
    print(result)
    print("__________________________")
    print(insertionsort(result))