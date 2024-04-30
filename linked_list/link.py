
class Node:

  def __init__(self, value):
    self.value = value
    self.next = None  

class LinkedList:

    def __init__(self):
        self.first = None
        self.last = None

    def is_empty(self):

        if self.first == None:
            return True

    def append(self, value):
        new_node = Node(value)
        if self.is_empty():
            self.first = self.last = new_node
        else:
            self.last.next = new_node
            self.last = new_node
            
    def remove_first(self):

        if self.is_empty():
            raise Exception("List is empty")

        removed_value = self.first.value
        self.first = self.first.next 
        if self.first is None:  
            self.last = None
            return removed_value
        
    def remove_last(self):

        if self.is_empty():
            raise Exception("List is empty")

        if self.first == self.last: 
            removed_value = self.first.value
            self.first = self.last = None
            return removed_value

  
        current = self.first
        while current.next.next:
            current = current.next

        removed_value = current.next.value
        current.next = None  
        self.last = current
        return removed_value

            
            


linked_list = LinkedList()
linked_list.append(10)
linked_list.append(20)
linked_list.append(30)
linked_list.append(40)
linked_list.append(50)
linked_list.append(60)
linked_list.remove_first()
#breakpoint()
current = linked_list.first

while current:
    print(current.value, end=" -> ")
    current = current.next

print("None")
