class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class SinglyLinkedList:
    def __init__(self):
        self.head = None

    def insert_begin(self, value):
        new_node = Node(value)
        new_node.next = self.head
        self.head = new_node
        print("Book ID inserted successfully.")

    def display(self):
        if self.head is None:
            print("Linked List is Empty")
        else:
            temp = self.head
            print("Book IDs in the library:")
            while temp is not None:
                print(temp.data, end=" -> ")
                temp = temp.next
            print("NULL")


# Create an empty linked list
library = SinglyLinkedList()

while True:
    print("\n--- College Library Menu ---")
    print("1. Insert at Beginning")
    print("2. Display")
    print("3. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        value = int(input("Enter Book ID: "))
        library.insert_begin(value)

    elif choice == 2:
        library.display()

    elif choice == 3:
        print("Program Ended")
        break

    else:
        print("Invalid Choice")