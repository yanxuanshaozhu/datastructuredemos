class Dqueue:
    def __init__(self):
        self.items = []

    def addFront(self, item):
        self.items.append(item)

    def addRear(self, item):
        self.items.insert(0, item)

    def removeFront(self):
        return self.items.pop()

    def removeRear(self):
        return self.items.pop(0)

    def isEmpty(self):
        return len(self.items) == 0

    def size(self):
        return len(self.items)


if __name__ == "__main__":
    dqueue = Dqueue()
    print(dqueue.isEmpty())
    dqueue.addRear(4)
    dqueue.addRear('dog')
    dqueue.addFront('cat')
    dqueue.addFront(True)
    print(dqueue.size())
    print(dqueue.removeRear())
    print(dqueue.removeFront())
