class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
class BinaryTree:
    def __init__(self, data=None, node=None):
        if node:
            self.root = node
        elif data:
            node = Node(data)
            self.root = node
        else:
            self.root = None

    def inorder_traversal(self, node=None, values=None):
        if values is None:
            values = []
        if node is None:
            node = self.root
        if node.left:
            self.inorder_traversal(node.left, values)
        values.append(node.data)
        if node.right:
            self.inorder_traversal(node.right, values)
        return values

if __name__ == "__main__":
    tree = BinaryTree(7)
    tree.root.left = Node(3)
    tree.root.right = Node(14)
    tree.root.left.right = Node(6)
    tree.root.right.left = Node(10)
    tree.root.right.right = Node(20)

    print(tree.inorder_traversal())
