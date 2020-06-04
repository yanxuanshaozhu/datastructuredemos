def shellsort(nums: list) -> list:
    skip = len(nums) // 2
    while skip > 0:
        for i in range(skip):
            result = gapinsertionsort(nums, i, skip)
        print("for skip ", skip, " result is ", result)
        skip = skip // 2


def gapinsertionsort(nums: list, start: int, gap: int) -> list:
    for i in range(start + gap, len(nums), gap):
        position = i
        value = nums[i]
        while position > start and nums[position - gap] > value:
            nums[position] = nums[position - gap]
            position = position - gap
        nums[position] = value
    return nums


if __name__ == "__main__":
    import numpy as np

    ls = np.random.normal(4, 2, 10)
    # result = [int(x) for x in ls]a
    result = [54, 26, 93, 17, 77, 31, 44, 55, 20]
    print(result)
    print("___________________________-")
    shellsort(result)
