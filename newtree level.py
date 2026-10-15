from collections import deque

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


def print_level_wise(root):
    if root is None:
        return

    queue = deque([root])

    while queue:
        node = queue.popleft()
        print(node.data, end=" ")

        if node.left:
            queue.append(node.left)

        if node.right:
            queue.append(node.right)

    print()


def height(root):
    if root is None:
        return 0

    return 1 + max(height(root.left), height(root.right))


def print_leaf_nodes(root):
    if root is None:
        return

    if root.left is None and root.right is None:
        print(root.data, end=" ")
        return

    print_leaf_nodes(root.left)
    print_leaf_nodes(root.right)



employee_ids = [50, 30, 70, 20, 40, 60, 80]

root = None
for emp_id in employee_ids:
    root = insert(root, emp_id)

print("Original BST (Level-wise):")
print_level_wise(root)


new_root = None
for emp_id in employee_ids:
    new_root = insert(new_root, emp_id)

print("New BST (Level-wise):")
print_level_wise(new_root)

print("Height of BST:", height(root))


print("Leaf Nodes:", end=" ")
print_leaf_nodes(root)
print()