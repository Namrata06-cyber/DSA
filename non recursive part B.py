class Node:
    def __init__(self, roll, name):
        self.roll = roll
        self.name = name
        self.left = None
        self.right = None


def insert(root, roll, name):
    if root is None:
        return Node(roll, name)

    if roll < root.roll:
        root.left = insert(root.left, roll, name)
    else:
        root.right = insert(root.right, roll, name)

    return root


def inorder(root):
    stack = []
    current = root

    while stack or current:
        while current:
            stack.append(current)
            current = current.left

        current = stack.pop()
        print(current.roll, current.name)
        current = current.right


def preorder(root):
    if root is None:
        return

    stack = [root]

    while stack:
        current = stack.pop()
        print(current.roll, current.name)

        if current.right:
            stack.append(current.right)

        if current.left:
            stack.append(current.left)


root = None

n = int(input("Enter number of students: "))

for i in range(n):
    roll = int(input("Enter roll number: "))
    name = input("Enter student name: ")

    root = insert(root, roll, name)

print("\nInorder Traversal:")
inorder(root)

print("\nPreorder Traversal:")
preorder(root)