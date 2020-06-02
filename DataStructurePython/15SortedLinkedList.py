class SortedLinkedList:
    class Node:
        def __init__(self, item):
            self.value = item
            self.nextNoede = None

        def getValue(self):
            return self.value

        def getNextNode(self):
            return self.nextNoede

        def setValue(self, item):
            self.value = item

        def setNextNode(self, node):
            self.nextNoede = node

    def __init__(self):
        self.head = None

    def isEmpty(self):
        return self.head is None

    def size(self):
        count = 0
        current = self.head
        while current is not None:
            count = count + 1
            current = current.getNextNode()
        return count

    def contains(self, item):
        flag = False
        stop = False
        current = self.head
        while current is not None and not flag and not stop:
            if current.getValue() == item:
                flag = True
            else:
                if current.getValue() > item:
                    stop = True
                else:
                    current = current.getNextNode()
        return flag

    def add(self, item):
        node = SortedLinkedList.Node(item)
        previous = None
        current = self.head
        stop = False
        while current is not None and not stop:
            if current.getValue() > item:
                stop = True
            else:
                previous = current
                current = current.getNextNode()
        if previous is None:
            node.setNextNode(self.head)
            self.head = node
        else:
            node.setNextNode(current)
            previous.setNextNode(node)

    def remove(self, item):
        previous = None
        current = self.head
        flag = False
        while current is not None and not flag:
            if current.getValue() >= item:
                flag = True
            else:
                previous = current
                current = current.getNextNode()
        if previous is None:
            self.head = current.getNextNode()
        else:
            previous.setNext(current.getNext())

    def index(self, item):
        count = -1
        current = self.head
        while current.getNext() is not None:
            count = count + 1
            if current.getValue() == item:
                break
            current = current.getNext()
        if current.getNext() is None:
            print("not found")
        else:
            print(count)

    def pop(self):
        previous = None
        current = self.head
        while current is not None:
            previous = current
            current = current.getNext()
        previous.setNext(None)

    def travel(self):
        current = self.head
        while current is not None:
            print(current.getValue())
            current = current.getNext()


if __name__ == "__main__":
    list1 = SortedLinkedList()
    list1.add(1)
    list1.add(2)
    list1.add(3)
    print("size")
    print(list1.size())
    print("travel")
    list1.travel()
    print("remove")
    list1.remove(3)
    list1.travel()
    print("contains")
    print(list1.contains(5))
    print("search")
    list1.index(5)
    print("search")
    list1.index(4)
