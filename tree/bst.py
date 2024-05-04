class Node():
    def __init__(self, value) -> None:
        self.value = value
        self.leftchild = None
        self.rightchild = None

class Tree():
    def __init__(self):
        self.root = None

    def insert(self, value):
        if self.root == None:
            self.root = Node(value)
        else:
            current = self.root
            while current!= None:
                if value < current.value:
                    if current.leftchild == None:
                        current.leftchild = Node(value)
                        break
                    else:
                        current = current.leftchild
                else:
                    if current.rightchild == None:
                        current.rightchild = Node(value)
                        break
                    else:
                        current = current.rightchild

    def lookup(self, value):
        current = self.root
        while current!= None:
            if value < current.value:
                current = current.leftchild
            elif value > current.value:
                current = current.rightchild
            else:
                return True
        return False
    
    def pre_order_traverse(self, current):
        print(current.value)
        pre_order_traverse(current.leftchild)
        pre_order_traverse(current.rightchild)
        pass
        

new_tree = Tree()
new_tree.insert(10)
new_tree.insert(15)
new_tree.insert(12)
new_tree.insert(11)
new_tree.insert(13)
new_tree.insert(4)
new_tree.insert(7)
new_tree.insert(17)
new_tree.insert(20)

print(new_tree.lookup(20))
print(new_tree.lookup(19))
print(new_tree.lookup(13))
print(new_tree.lookup(7))