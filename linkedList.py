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
            return

        current = self.head
        while current.next:
            current = current.next

        current.next = new_node

    def display(self):
        current = self.head
        while current:
            print(current.data)
            current = current.next

students = LinkedList()

students.append({
    "adm": 101,
    "name": "Alice",
    "grades": {"CIR 102": "A", "CIT 115": "B", "CIR 201": "A"}
})

students.append({
    "adm": 102,
    "name": "Brian",
    "grades": {"CIR 102": "B", "CIT 115": "A", "CIR 201": "B"}
})

students.append({
    "adm": 103,
    "name": "Cynthia",
    "grades": {"CIR 102": "A", "CIT 115": "A", "CIR 201": "A"}
})
students.display()
