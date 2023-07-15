class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            current_node = self.head
            while current_node.next is not None:
                current_node = current_node.next
            current_node.next = new_node

    def prepend(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def insert_after(self, prev_node, data):
        if prev_node is None:
            print("Previous node does not exist.")
            return
        new_node = Node(data)
        new_node.next = prev_node.next
        prev_node.next = new_node

    def delete(self, data):
        if self.head is None:
            print("Linked list is empty.")
            return

        if self.head.data == data:
            self.head = self.head.next
            return

        current_node = self.head
        while current_node.next is not None:
            if current_node.next.data == data:
                current_node.next = current_node.next.next
                return
            current_node = current_node.next

    def display(self):
        current_node = self.head
        while current_node is not None:
            print(current_node.data, end=" ")
            current_node = current_node.next
        print()


# Create a new linked list
my_list = LinkedList()

# Append some elements
my_list.append(10)
my_list.display()
my_list.append(20)
my_list.display()
my_list.append(30)
my_list.display()
# Prepend an element
my_list.prepend(5)
my_list.display()
# Insert after a specific node
my_list.insert_after(my_list.head.next, 15)
my_list.display()
# Display the linked list
my_list.display()  # Output: 5 10 15 20 30

# Delete an element
my_list.delete(15)
print(my_list)
# Display the updated linked list
my_list.display()  # Output: 5 10 20 30
