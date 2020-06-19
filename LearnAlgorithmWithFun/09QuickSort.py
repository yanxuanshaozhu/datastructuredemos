def quicksort(nums: list, first: int, last: int) -> list:
    if first < last:
        splitpoint = partition(nums, first, last)
        quicksort(nums, first, splitpoint - 1)
        quicksort(nums, splitpoint + 1, last)
    return nums


def partition(nums: list, first: int, last: int) -> int:
    mid = (first + last) // 2
    index = last
    if nums[first] < nums[mid] < nums[last]:
        index = mid
    if nums[first] < nums[last]:
        index = first
    pivot = nums[index]
    nums[index], nums[first] = nums[first], nums[index]
    border = first
    for i in range(first, last + 1):
        if nums[i] < pivot:
            border += 1
            nums[i], nums[border] = nums[border], nums[i]
    nums[first], nums[border] = nums[border], nums[first]
    return border


if __name__ == "__main__":
    ls = [30, 24, 5, 58, 18, 36, 12, 42, 39]
    print(ls)
    print("_________________________")
    print(quicksort(ls, 0, len(ls) - 1))
