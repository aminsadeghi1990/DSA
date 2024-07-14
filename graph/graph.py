class Node:
    def __init__(self, label):
        self.label = label


class Graph:

    def __init__(self):
        self.node_dictionary = {}
        self.adjacency_dictionary = {}

    def add_node(self, label):
        if label not in self.node_dictionary:
            self.node = Node(label)
            self.node_dictionary[label] = self.node
        if label not in self.adjacency_dictionary:
            self.adjacency_dictionary[label] = []

    def add_edge(self, fr: str, to: str):
        if fr not in self.node_dictionary:
            print(f"from node '{fr}' does not exist!!!")
            return
        if to not in self.node_dictionary:
            print(f"to node '{to}' does not exist!!!")
            return

        self.adjacency_dictionary[fr].append(to)
        self.adjacency_dictionary[to].append(fr)

    def print_nodes_connection(self):
        for key, values in self.adjacency_dictionary.items():
            for value in values:
                print(f"{key} is connected to {value}")


new_graph = Graph()
new_graph.add_node("amin")
new_graph.add_node("mobin")
new_graph.add_node("mehdi")
new_graph.add_node("shariat")
new_graph.add_node("epack")
new_graph.add_node("mahmoodhood")
new_graph.add_node("nosrat")

new_graph.add_edge("amin", "mobin")
new_graph.add_edge("amin", "mehdi")
new_graph.add_edge("mahmoodhood", "mobin")
new_graph.add_edge("amin", "nosrat")
new_graph.add_edge("mehdi", "mobin")
new_graph.add_edge("amin", "mobin")

new_graph.print_nodes_connection()

