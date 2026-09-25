class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def insert(root, data):
    if root is None:
        return Node(data)

    if data < root.data:
        root.left = insert(root.left, data)
    else:
        root.right = insert(root.right, data)

    return root


def inorder(root):
    stack = [None] * 100
    top = -1
    current = root

    while current is not None or top != -1:

        while current is not None:
            top = top + 1
            stack[top] = current
            current = current.left

        current = stack[top]
        top = top - 1

        print(current.data, end=" ")

        current = current.right


def preorder(root):
    if root is None:
        return

    stack = [None] * 100
    top = 0
    stack[top] = root

    while top != -1:
        current = stack[top]
        top = top - 1

        print(current.data, end=" ")

        if current.right is not None:
            top = top + 1
            stack[top] = current.right

        if current.left is not None:
            top = top + 1
            stack[top] = current.left


print("Create Binary Search Tree")

root = None

n = int(input("Enter number of nodes: "))

for i in range(n):
    data = int(input("Enter node value: "))
    root = insert(root, data)

print("\nInorder Traversal:")
inorder(root)

print("\nPreorder Traversal:")
preorder(root)