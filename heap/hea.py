class Heap:
    def __init__(self) -> None:
        self.my_list = [None] * 10
        self.size = 0

    def swap(self, first, second):
        temp = self.my_list[first]
        self.my_list[first] = self.my_list[second]
        self.my_list[second] = temp

    def insert(self, value):
        if self.size == len(self.my_list):
            return "List is FULL!!!"
        else:
            self.my_list[self.size] = value
            self.size += 1
            self.bubble_up()
            
    def remove(self):
        
        if self.size == 0:
            return "List is EMPTY !!!!"
        else:
            self.my_list[0] = self.my_list[self.size - 1]
            index = 0
            while index <= self.size and not self.is_valid_parent(index):
                
                larger_child_index = self.larger_child_index(index)
                self.swap(index, larger_child_index)
                index = larger_child_index
            
        
    def leftchild_index(self, index):
        return index*2 +1
    
    def rightchild_index(self, index):
        return index*2 +2
        
    def leftchild(self, index):
        return self.my_list[self.leftchild_index(index)]
    
    def rightchild(self, index):
        return self.my_list[self.rightchild_index(index)]
    
    def is_valid_parent(self, index) -> bool:
        return self.my_list[index] >= self.leftchild(
            index) or self.my_list[index] >= self.rightchild(index)
        
    def larger_child_index(self, index):
        if self.leftchild(index) > self.rightchild(index):
            return self.leftchild_index(index)
        else:
            return self.rightchild_index(index)

    def bubble_up(self):
        index = self.size - 1
        while index > 0:
            parent_index = (index - 1) // 2
            if self.my_list[index] > self.my_list[parent_index]:
                self.swap(index, parent_index)
                index = parent_index
            else:
                break
  


heap = Heap()

heap.insert(4)
heap.insert(96)
heap.insert(10)
heap.insert(2)
heap.insert(17)
heap.insert(5)
heap.insert(8)
heap.insert(33)
heap.insert(12)
heap.insert(15)

print(heap.my_list)
