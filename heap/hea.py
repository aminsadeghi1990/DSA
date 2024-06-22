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
            return "List is full!!!"
        else:
            self.my_list[self.size] = value
            self.size += 1
            self.bubble_up()

    def bubble_up(self):
        index = self.size - 1
        while index > 0:
            parent_index = (index - 1) // 2
            if self.my_list[index] > self.my_list[parent_index]:
                self.swap(index, parent_index)
                index = parent_index
            else:
                break


# Create an instance of the class
heap = Heap()

# Insert values into the heap
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

# Print the list to verify
print(heap.my_list)
