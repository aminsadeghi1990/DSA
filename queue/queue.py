

class Queue():

    def __init__(self, capacity) -> None:
        self.capacity = capacity
        self.count = 0
        self.items = []

    def insert(self, item):
        if (self.count >= self.capacity):
            raise Exception("Queue is full")

        self.items.append(item)
        self.count += 1

    def get_queue(self):
        return self.items

    def read_last(self):
        return self.items[self.count-1]

    def is_empty(self):
        return self.count == 0

    def is_full(self):
        return self.count >= self.capacity

    def remove(self):
        if self.is_empty():
            raise Exception("Queue is empty")
        self.count -= 1
        x = self.items[0]
        
        self.items = self.items[1::] 
        
        return x 

    def get_index(self, index):
        if index >= self.count:
            raise Exception("Index out of range")
        return self.items[index]

    def reverse(self):

        if self.is_empty():
            return []
        if self.count == 1:
            return self.items
        temp_arr = []
        
        while len(self.items):
            temp_arr.append(self.items.pop())
        return temp_arr


a = Queue(4)
a.insert(1)
a.insert(2)
a.insert(4)
a.insert(6)
print(a.get_queue())
print(a.reverse())