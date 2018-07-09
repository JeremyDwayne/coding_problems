class node:
    def __init__(self):
        self.next = None
        self.value = None


class linked_list:
    def __init__(self):
        self.head = None


    def add(self, current_node, value):
        new_node = node()
        new_node.value = value
        if current_node.next is not None:
            new_node.next = current_node.next
            current_node.next = new_node
        else:
            current_node.next = new_node


    def printl(self, temp_node):
        print(temp_node.value)
        if temp_node.next is not None:
            self.printl(temp_node.next)
