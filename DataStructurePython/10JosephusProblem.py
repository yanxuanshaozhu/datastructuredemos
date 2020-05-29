def safe(namelist, numskipped):
    queue = []
    for name in namelist:
        queue.append(name)
    while len(queue) > 1:
        for i in range(numskipped):
            temp = queue[0]
            del queue[0]
            queue.append(temp)
        del queue[0]
    result = queue[0]
    del queue[0]
    return result


if __name__ == "__main__":
    ls = ["Bill", "David", "Susan", "Jane", "Kent", "Brad"]
    num = 7
    print(safe(ls, num))
