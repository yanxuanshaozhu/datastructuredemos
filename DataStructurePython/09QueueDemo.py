class Queue(object):
    def __init__(self):
        self.items = []

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        temp = self.items[0]
        del self.items[0]
        return temp

    def isEmpty(self):
        return len(self.items) == 0

    def size(self):
        return len(self.items)


if __name__ == "__main__":
    queue = Queue()
    print("1:isEmpty: ", str(queue.isEmpty()))
    queue.enqueue(1)
    queue.enqueue(2)
    print("2:queueSize: ", queue.size())
    print("3:dequeue: ", queue.dequeue())
    print("4:dequeue: ", queue.dequeue())
