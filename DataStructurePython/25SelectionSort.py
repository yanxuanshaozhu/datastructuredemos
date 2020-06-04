def selectionsort(nums: list) -> list:
    for i in range(len(nums) - 1, 0, -1):
        position = 0
        for j in range(1, i + 1):
            if nums[j] > nums[position]:
                position = j
        nums[i], nums[position] = nums[position], nums[i]
    return nums


if __name__ == "__main__":
    import numpy as np

    ls = np.random.normal(4, 2, 10)
    result = [int(x) for x in ls]
    print(result)
    print("____________________")
    print(selectionsort(result))
