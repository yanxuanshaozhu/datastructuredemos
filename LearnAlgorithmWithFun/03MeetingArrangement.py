# There are several meetings, each has a starting time and an ending time, there is also a time period to arrange
# the meetings, arrange the meetings so that most meetings can be held


def arrange(starts: list, ends: list, start: int, end: int) -> tuple:
    meetings = zip(starts, ends)
    meetings = sorted(meetings, key=lambda x: x[1])
    result = []
    amount = 0
    item = meetings.pop(0)
    if item[0] >= start and item[1] <= end:
        result.append(item)
        start = item[1]
        amount += 1
        while start < end:
            item = meetings.pop(0)
            if item[0] >= start and item[1] <= end:
                result.append(item)
                start = item[1]
                amount += 1
    else:
        return None
    return result, amount


if __name__ == "__main__":
    a, b = arrange([3, 1, 5, 2, 5, 3, 8, 6, 8, 12], [6, 4, 7, 5, 9, 8, 11, 10, 12, 14], 1, 14)
    print(a)
    print(b)
