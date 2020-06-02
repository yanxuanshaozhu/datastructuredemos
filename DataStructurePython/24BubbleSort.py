def bubblesort1(nums: list) -> list:
    for i in range(len(nums) - 1, 0, -1):
        for j in range(i):
            if nums[j] > nums[j + 1]:
                nums[j], nums[j + 1] = nums[j + 1], nums[j]
    return nums


# If no exchange is conducted in one round, then the list has already  been sorted.
def bubblesort2(nums: list) -> list:
    exchange = True
    scale = len(nums) - 1
    while scale > 0 and exchange:
        exchange = False
        for i in range(scale):
            if nums[i] > nums[i + 1]:
                exchange = True
                nums[i], nums[i + 1] = nums[i + 1], nums[i]
        scale = scale - 1
    return nums


if __name__ == "__main__":
    import numpy as np

    ls = np.random.normal(4, 2, 10)
    result = [int(x) for x in ls]
    print(result)
    print("___________________")
    print(bubblesort1(result))
    print("___________________")
    print(bubblesort2(result))
