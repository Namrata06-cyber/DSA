class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def inorder(root):
    if root:
        inorder(root.left)
        print(root.data, end=" | ")
        inorder(root.right)


def preorder(root):
    if root:
        print(root.data, end=" | ")
        preorder(root.left)
        preorder(root.right)


def postorder(root):
    if root:
        postorder(root.left)
        postorder(root.right)
        print(root.data, end=" | ")



root = Node("DSA")
root.left = Node("DBMS")
root.right = Node("Python")

root.left.left = Node("C++")
root.left.right = Node("Java")

root.right.left = Node("HTML")
root.right.right = Node("SQL")


print("Library Catalog - Inorder:")
inorder(root)

print("\n\nLibrary Catalog - Preorder:")
preorder(root)

print("\n\nLibrary Catalog - Postorder:")
postorder(root)