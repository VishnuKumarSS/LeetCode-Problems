class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class MyQueue:
    def __init__(self):
        self.length = 0
        self.first = None
        self.last = None

    def print(self):
        temp = self.first
        print("first, last", self.first.value, self.last.value)
        print('Queue:')
        while temp is not None:
            print(temp.value)
            temp = temp.next

    def push(self, x: int) -> None:
        new_node = Node(x)
        if self.length == 0:
            self.first = new_node
            self.last = new_node
        else:
            temp = self.last
            self.last = new_node
            temp.next = self.last
        self.length += 1
    
    def pop(self) -> int:
        if self.length == 0:
            return None
        temp = self.first
        self.first = self.first.next
        temp.next = None
        self.length -= 1
        return temp.value

    def peek(self) -> int:
        return self.first.value

    def empty(self) -> bool:
        if self.length == 0:
            return True
        return False


my_queue = MyQueue()
my_queue.push(3)
my_queue.push(7)
my_queue.push(56)
my_queue.push(88)
my_queue.print()
print('popped:', my_queue.pop())
print('popped:', my_queue.pop())
# my_queue.push(6)
# my_queue.print()
my_queue.print()

