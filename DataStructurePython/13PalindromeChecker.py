def checker(string):
    dequeue = []
    for ele in string:
        dequeue.append(ele)
    while len(dequeue) > 1:
        right = dequeue.pop()
        left = dequeue.pop(0)
        if right != left:
            return False
    # if len(dequeue) & 1:
    #     while len(dequeue) != 1:
    #         right = dequeue.pop()
    #         left = dequeue.pop(0)
    #         if right != left:
    #             return False
    # else:
    #     while len(dequeue) != 0:
    #         right = dequeue.pop()
    #         left = dequeue.pop(0)
    #         if right != left:
    #             return False
    return True


if __name__ == "__main__":
    print(checker("121"))
    print(checker("toot"))
    print(checker("123"))
