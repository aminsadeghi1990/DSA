import networkx as nx
import matplotlib.pyplot as plt


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
            while current != None:
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
        while current != None:
            if value < current.value:
                current = current.leftchild
            elif value > current.value:
                current = current.rightchild
            else:
                return True
        return False

    def pre_order_traverse(self):
        self._pre_order_traverse(self.root)

    def _pre_order_traverse(self, node):
        if node == None:
            return
        print(node.value)
        self._pre_order_traverse(node.leftchild)
        self._pre_order_traverse(node.rightchild)

    def post_order_traverse(self):
        self._post_order_traverse(self.root)

    def _post_order_traverse(self, node):
        if node == None:
            return
        self._post_order_traverse(node.leftchild)
        self._post_order_traverse(node.rightchild)
        print(node.value)

    def height(self):
        return self._height(self.root)

    def _height(self, node):
        if node is None:
            return -1
        left_height = self._height(node.leftchild)
        right_height = self._height(node.rightchild)
        return 1 + max(left_height, right_height)

    def to_graph(self):
        G = nx.DiGraph()
        nodes = [self.root]
        while nodes:
            node = nodes.pop(0)
            if node is not None:
                G.add_node(node.value)
                if node.leftchild is not None:
                    G.add_edge(node.value, node.leftchild.value)
                    nodes.append(node.leftchild)
                if node.rightchild is not None:
                    G.add_edge(node.value, node.rightchild.value)
                    nodes.append(node.rightchild)
        return G


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

print("Pre-order traversal:")
new_tree.pre_order_traverse()
print("####################################")
print("Height of the tree:", new_tree.height())
print("####################################")
print("Post-order traversal:")
new_tree.post_order_traverse()

G = new_tree.to_graph()
nx.draw(G, with_labels=True)
plt.show()
