class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node

    def prepend(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def search(self, key):
        current = self.head
        while current:
            if current.data == key:
                return True
            current = current.next
        return False

    def print_list(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")
        

# Create a linked list
ll = LinkedList()

# Append elements
ll.append(10)
ll.append(20)
ll.append(30)

ll.append({"name": "Alice", "age": 30})
ll.append({"name": "Bob", "age": 25})

# Prepend an element
ll.prepend(5)

# Print the list
ll.print_list()  # Output: 5 -> 10 -> 20 -> 30 -> None

# Search for an element
print(ll.search(20))  # Output: True
print(ll.search(100))  # Output: False