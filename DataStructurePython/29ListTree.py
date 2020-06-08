def ListTree(root: object) -> list:
    return [root, [], []]


def insertLeft(tree: list, newbranch: list) -> list:
    temp = tree.pop(1)
    if len(temp) > 1:
        tree.insert(1, [newbranch, temp, []])
    else:
        tree.insert(1, [newbranch, [], []])
    return tree


def insertRight(tree: list, newbranch: list) -> list:
    temp = tree.pop(2)
    if len(temp) > 1:
        tree.insert(2, [newbranch, [], temp])
    else:
        tree.insert(2, [newbranch, [], []])
    return tree


def getRootValue(tree: list) -> object:
    return tree[0]


def setRootValue(tree: list, val: list) -> list:
    tree[0] = val


def getLeftChildren(tree: list) -> list:
    return tree[1]


def getRightChildren(tree: list) -> list:
    return tree[2]


if __name__ == "__main__":
    tree = ListTree(3)
    print(tree)
    insertLeft(tree, 4)
    print(tree)
    insertLeft(tree, 5)
    print(tree)
    insertRight(tree, 6)
    print(tree)
    insertRight(tree, 7)
    print(tree)
