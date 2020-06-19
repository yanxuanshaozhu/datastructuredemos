def mergesort(items: list) -> list:
    if len(items) > 1:
        mid = len(items) // 2
        left = items[:mid]
        right = items[mid:]

        mergesort(left)
        mergesort(right)

        i = 0
        j = 0
        k = 0
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                items[k] = left[i]
                i = i + 1
            else:
                items[k] = right[j]
                j = j + 1
            k = k + 1
        if i != len(left):
            while k < len(items) and i < len(left):
                items[k] = left[i]
                k = k + 1
                i = i + 1
        if j != len(right):
            while k < len(items) and j < len(right):
                items[k] = right[j]
                k = k + 1
                j = j + 1
    return items


if __name__ == "__main__":
    ls = [42, 15, 20, 6, 8, 38, 50, 12]
    print(mergesort(ls))
