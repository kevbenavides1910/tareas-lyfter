class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class Stack:
    def __init__(self):
        self._top = None
        self._size = 0

    def push(self, value):
        new_node = Node(value)
        new_node.next = self._top
        self._top = new_node
        self._size += 1

    def pop(self):
        if self.is_empty():
            raise IndexError("Pop from empty stack")
        removed_value = self._top.value
        self._top = self._top.next
        self._size -= 1
        return removed_value

    def peek(self):
        if self.is_empty():
            raise IndexError("Peek from empty stack")
        return self._top.value

    def is_empty(self):
        return self._top is None

    def size(self):
        return self._size

    def print_stack(self):
        if self.is_empty():
            print("Stack is empty")
            return
        print("Stack (top → bottom):")
        current = self._top
        while current is not None:
            marker = " ← TOP" if current is self._top else ""
            print(f"  [{current.value}]{marker}")
            current = current.next


if __name__ == "__main__":
    s = Stack()
    s.push(10)
    s.push(20)
    s.push(30)
    s.print_stack()
    print(f"Popped: {s.pop()}")
    s.print_stack()
