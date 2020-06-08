class BinaryHeap(object):
    def __init__(self):
        self.heapList = [0]
        self.heapSize = 0

    def isEmpty(self):
        return self.heapSize == 0

    def size(self):
        return self.heapSize

    def insert1(self, value):
        self.heapList.append(value)
        self.heapSize += 1
        exchange = True
        length = self.heapSize
        while length // 2 > 0 and exchange:
            exchange = False
            if self.heapList[length] < self.heapList[length // 2]:
                exchange = True
                self.heapList[length], self.heapList[length // 2] = self.heapList[length // 2], \
                                                                    self.heapList[length]
            length //= 2

    # This method is the one in the book,yet there would be redundancy in the loop when no exchange is needed
    def insert2(self, value):
        self.heapList.append(value)
        self.heapSize += 1
        length = self.heapSize
        while length // 2 > 0:
            if self.heapList[length] < self.heapList[length // 2]:
                self.heapList[length], self.heapList[length // 2] = self.heapList[length // 2], \
                                                                    self.heapList[length]
            length //= 2

    def delMin(self):
        val = self.heapList[1]
        self.heapList[1] = self.heapList[self.heapSize]
        self.heapSize = self.heapSize - 1
        self.heapList.pop(1)
        i = 1
        while 2 * i < self.heapSize:
            minChild = 2 * i if 2 * i + 1 > self.heapSize else (
                2 * i if self.heapList[2 * i] < self.heapList[2 * i + 1] else 2 * i + 1)
            if self.heapList[i] > self.heapList[minChild]:
                self.heapList[i], self.heapList[minChild] = self.heapList[minChild], self.heapList[i]
            i = minChild
        return val

    def buildHeap(self, alist):
        i = len(alist) // 2
        self.heapList = [0] + alist
        self.heapSize = len(alist)
        while i > 0:
            while 2 * i < self.heapSize:
                minChild = 2 * i if 2 * i + 1 > self.heapSize else (
                    2 * i if self.heapList[2 * i] < self.heapList[2 * i + 1] else 2 * i + 1)
                if self.heapList[i] > self.heapList[minChild]:
                    self.heapList[i], self.heapList[minChild] = self.heapList[minChild], self.heapList[i]
                i = minChild
            i = i - 1


if __name__ == "__main__":
    heap = BinaryHeap()
    print("The empty heap:")
    print(heap.heapList)
    print("The heap after insertion:")
    heap.insert1(1)
    heap.insert1(-2)
    heap.insert1(3)
    heap.insert1(0)
    heap.insert1(-10)
    print(heap.heapList)
    print("The smallest element in the heap:")
    print(heap.delMin())
    print("The remaining elements in the heap after deleting the smallest one:")
    print(heap.heapList)
