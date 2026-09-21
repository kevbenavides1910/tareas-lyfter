class Node:
    def __init__(self, value):
        self.value = value
        self.prev = None
        self.next = None


class Deque:
    def __init__(self):
        self._head = None
        self._tail = None
        self._size = 0

    def _is_empty(self):
        return self._head is None

    def push_left(self, value):
        new_node = Node(value)
        if self._is_empty():
            self._head = new_node
            self._tail = new_node
        else:
            new_node.next = self._head
            self._head.prev = new_node
            self._head = new_node
        self._size += 1

    def push_right(self, value):
        new_node = Node(value)
        if self._is_empty():
            self._head = new_node
            self._tail = new_node
        else:
            new_node.prev = self._tail
            self._tail.next = new_node
            self._tail = new_node
        self._size += 1

    def pop_left(self):
        if self._is_empty():
            raise IndexError("Pop from empty deque")
        removed_value = self._head.value
        if self._head is self._tail:
            self._head = None
            self._tail = None
        else:
            self._head = self._head.next
            self._head.prev = None
        self._size -= 1
        return removed_value

    def pop_right(self):
        if self._is_empty():
            raise IndexError("Pop from empty deque")
        removed_value = self._tail.value
        if self._head is self._tail:
            self._head = None
            self._tail = None
        else:
            self._tail = self._tail.prev
            self._tail.next = None
        self._size -= 1
        return removed_value

    def size(self):
        return self._size

    def print_deque(self):
        if self._is_empty():
            print("Deque is empty")
            return
        print("Deque (left → right):")
        current = self._head
        parts = []
        while current is not None:
            parts.append(str(current.value))
            current = current.next
        print("  HEAD → " + " ↔ ".join(parts) + " ← TAIL")


if __name__ == "__main__":
    d = Deque()
    d.push_right(10)
    d.push_right(20)
    d.push_left(5)
    d.push_left(1)
    d.print_deque()
    print(f"Pop left: {d.pop_left()}")
    print(f"Pop right: {d.pop_right()}")
    d.print_deque()
