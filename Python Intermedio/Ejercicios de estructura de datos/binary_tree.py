class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BinaryTree:
    def __init__(self):
        self._root = None

    def insert(self, value):
        if self._root is None:
            self._root = Node(value)
        else:
            self._insert_recursive(self._root, value)

    def _insert_recursive(self, node, value):
        if value < node.value:
            if node.left is None:
                node.left = Node(value)
            else:
                self._insert_recursive(node.left, value)
        elif value > node.value:
            if node.right is None:
                node.right = Node(value)
            else:
                self._insert_recursive(node.right, value)

    def search(self, value):
        return self._search_recursive(self._root, value)

    def _search_recursive(self, node, value):
        if node is None:
            return False
        if value == node.value:
            return True
        if value < node.value:
            return self._search_recursive(node.left, value)
        return self._search_recursive(node.right, value)

    def print_tree(self):
        if self._root is None:
            print("Tree is empty")
            return
        print("Binary Tree (in-order: left → root → right):")
        self._print_visual(self._root, prefix="", is_left=True, is_root=True)

    def _print_visual(self, node, prefix, is_left, is_root):
        if node is None:
            return
        if is_root:
            connector = "Root── "
        elif is_left:
            connector = "├── L: "
        else:
            connector = "└── R: "
        print(prefix + connector + str(node.value))
        child_prefix = prefix if is_root else prefix + ("│   " if is_left else "    ")
        if node.left is not None or node.right is not None:
            self._print_visual(node.left,  child_prefix, is_left=True,  is_root=False)
            self._print_visual(node.right, child_prefix, is_left=False, is_root=False)

    def inorder_traversal(self):
        print("In-order traversal (sorted):", end=" ")
        self._inorder_recursive(self._root)
        print()

    def _inorder_recursive(self, node):
        if node is None:
            return
        self._inorder_recursive(node.left)
        print(node.value, end=" ")
        self._inorder_recursive(node.right)


if __name__ == "__main__":
    bt = BinaryTree()
    for value in [50, 30, 70, 20, 40, 60, 80]:
        bt.insert(value)
    bt.print_tree()
    bt.inorder_traversal()
    print(f"Search 40: {bt.search(40)}")
    print(f"Search 99: {bt.search(99)}")
