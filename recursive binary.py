class Node:
    def _init_(self, value):
        self.value = value
        self.left = None
        self.right = None


def create_tree():
    value = input("Enter value for node (or -1 for no node): ")

    if value == "-1":
        return None

    root = Node(int(value))

    print(f"Enter left child of {root.value}")
    root.left = create_tree()

    print(f"Enter right child of {root.value}")
    root.right = create_tree()

    return root


def inorder(root):
    if root:
        inorder(root.left)
        print(root.value, end=" ")
        inorder(root.right)


def preorder(root):
    if root:
        print(root.value, end=" ")
        preorder(root.left)
        preorder(root.right)


def postorder(root):
    if root:
        postorder(root.left)
        postorder(root.right)
        print(root.value, end=" ")


print("Create Binary Tree")
root = create_tree()

print("\nInorder Traversal:")
inorder(root)

print("\nPreorder Traversal:")
preorder(root)

print("\nPostorder Traversal:")
postorder(root)