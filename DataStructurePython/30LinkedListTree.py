class LinkedListTree(object):
    def __init__(self, root: object) -> list:
        self.key = root
        self.leftChildren = None
        self.rightChildren = None

    def getRootValue(self) -> object:
        return self.key

    def setRootValue(self, value: int) -> None:
        self.key = value

    def getLeftChildren(self):
        return self.leftChildren

    def getRightChildren(self):
        return self.rightChildren

    def insertLeft(self, newNode: object) -> None:
        if self.getLeftChildren() is None:
            self.leftChildren = LinkedListTree(newNode)
        else:
            left = LinkedListTree(newNode)
            left.leftChildren = self.leftChildren
            self.leftChildren = left

    def insertRight(self, newNode: object) -> None:
        if self.getRightChildren() is None:
            self.leftChildren = LinkedListTree(newNode)
        else:
            right = LinkedListTree(newNode)
            right.rightChildren = self.rightChildren
            self.rightChildren = right


if __name__ == "__main__":
    aTree = LinkedListTree('a')
    print(aTree.getRootValue())
    print(aTree.getLeftChildren())
    aTree.insertLeft('b')
    print(aTree.getLeftChildren)
    temp = aTree.getLeftChildren().getRootValue()
    print(temp)
