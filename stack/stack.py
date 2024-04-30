

class Stack():
    
    def __init__(self, capacity) -> None:
        self.capacity = capacity
        self.count = 0
        self.items = []
        
    def insert(self, item):
        if(self.count >= self.capacity):
            raise Exception ("Stack is full")
            
        self.items.append(item)
        self.count +=1
        
    def get_stack(self):
        return self.items
     
    def read_last(self):
        return self.items[self.count-1]
    def is_empty(self):
        return self.count == 0
    def is_full(self):
        return self.count >= self.capacity
    def remove(self):
        if self.is_empty():
            raise Exception ("Stack is empty")
        self.count -=1
        return self.items.pop()
    
    def get_index(self, index):
        if index >= self.count:
            raise Exception ("Index out of range")
        return self.items[index]
    def reverse(self):

        if self.is_empty():
            return []
        if self.count == 1:
            return self.items
        
        temp_stack = Stack(self.capacity)
        
        while not self.is_empty():
            temp_stack.insert(self.remove())
        
        return temp_stack.get_stack()    
            
    
        
    





