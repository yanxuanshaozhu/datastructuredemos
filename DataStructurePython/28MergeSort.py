def mergesort(nums: list) -> list:
    if len(nums) > 1:
        mid = len(nums) // 2
        left = nums[:mid]
        right = nums[mid:]
        mergesort(left)
        mergesort(right)

        i = 0
        j = 0
        k = 0
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                nums[k] = left[i]
                i = i + 1
            else:
                nums[k] = right[j]
                j = j + 1
            k = k + 1
        while i < len(left):
            nums[k] = left[i]
            i = i + 1
            k = k + 1
        while j < len(right):
            nums[k] = right[j]
            j = j + 1
            k = k + 1
    return nums


if __name__ == "__main__":
    import numpy as np

    ls = np.random.normal(4, 2, 10)
    result = [int(x) for x in ls]
    print(result)
    print("++++++++++++++++++")
    print(mergesort(result))
