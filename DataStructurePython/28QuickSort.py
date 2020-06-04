def quicksort(nums: list, first: int, last: int) -> list:
    if first < last:
        splitpoint = partition(nums, first, last)
        quicksort(nums, first, splitpoint)
        quicksort(nums, splitpoint + 1, last)
    return nums


def partition(nums: list, first: int, last: int) -> int:
    pivot = nums[first]
    leftmark = first
    rightmark = last
    for i in range(leftmark + 1, rightmark):
        if nums[i] < pivot:
            nums[i], nums[leftmark] = nums[leftmark], nums[i]
            leftmark = leftmark + 1
    pivot, nums[leftmark] = nums[leftmark], pivot
    return leftmark


if __name__ == "__main__":
    import numpy as np

    ls = np.random.normal(4, 2, 10)
    result = [int(x) for x in ls]
    print(result)
    print("_________________________")
    print(quicksort(result, 0, len(result) - 1))
