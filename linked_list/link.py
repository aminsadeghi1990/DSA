
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

    def append_to_last(self, value):
        new_node = Node(value)
        if self.is_empty():
            self.first = self.last = new_node
        else:
            self.last.next = new_node
            self.last = new_node
            
    def remove_first(self):

        if self.is_empty():
            raise Exception("List is empty")

        second = self.first.next
        self.first.next = None
        self.first = second
        
        
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
    
    def append_to_first(self,value):
        new_node = Node(value)
        if self.is_empty():
            self.first = self.last = new_node
        else:
            new_node.next = self.first
            self.first = new_node
        
    
        
        
            

            
            


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
