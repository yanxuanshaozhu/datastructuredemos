class Stack:
    def __init__(self):
        self.items = []

    def pop(self):
        temp = self.items[-1]
        self.items = self.items[0:len(self.items) - 1]
        return temp

    def push(self, item):
        self.items.append(item)

    def peek(self):
        return self.items[-1]

    def isEmpty(self):
        return self.items == []

    def size(self):
        return len(self.items)


if __name__ == "__main__":
    stack = Stack()
    print("1:isEmpty", stack.isEmpty())
    print("2:size", stack.size())
    stack.push(2)
    stack.push(3)
    stack.push(4)
    print("3:peek", stack.peek())
    print("4:display")
    stack.display()
    print("5:pop", stack.pop())
    print("6:peek", stack.peek())
