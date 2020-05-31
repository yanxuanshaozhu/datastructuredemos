class UnsortedLinkedList:
    class Node:
        def __init__(self, item):
            self.value = item
            self.nextNode = None

        def getValue(self):
            return self.value

        def setValue(self, item):
            self.value = item

        def getNext(self):
            return self.nextNode

        def setNext(self, node):
            self.nextNode = node

    def __init__(self):
        self.head = None

    def add(self, item):
        temp = UnsortedLinkedList.Node(item)
        temp.setNext(self.head)
        self.head = temp

    def isEmpty(self):
        return self.head is None

    def size(self):
        count = 0
        current = self.head
        while current is not None:
            count = count + 1
            current = current.getNext()
        return count

    def contains(self, item):
        current = self.head
        flag = False
        while current is not None and not flag:
            if current.getValue == item:
                flag = True
            else:
                current = current.getNext()
        return flag

    def remove(self, item):
        current = self.head
        previous = None
        flag = False
        while not flag:
            if current.getValue() == item:
                flag = True
            else:
                previous = current
                current = current.getNext()
        if previous is None:
            self.head = current.getNext()
        else:
            previous.setNext(current.getNext())

    def append(self, item):
        current = self.head
        while current is not None:
            current = current.getNext()
        current.setValue(item)
        current.setNext(None)

    def insert(self, index, item):
        temp = UnsortedLinkedList.Node(item)
        previous = None
        current = self.head
        if index == 0:
            temp.setNext(self.head)
            self.head = temp
        else:
            for i in range(index):
                previous = current
                current = current.getNext()
            previous.setNext(temp)
            temp.setNext(current)

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
    list1 = UnsortedLinkedList()
    list1.add(1)
    list1.add(2)
    list1.add(3)
    list1.travel()
    print("remove")
    list1.remove(3)
    list1.travel()
    print("insert")
    list1.insert(1, 4)
    list1.travel()
    print("contains")
    print(list1.contains(5))
    print("search")
    list1.index(5)
    print("search")
    list1.index(4)
