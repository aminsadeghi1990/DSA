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
            print(f"from node, '{fr}' does not exist!!!")
            return
        if to not in self.node_dictionary:
            print(f"to node, '{to}' does not exist!!!")
            return

        self.adjacency_dictionary[fr].append(to)
        self.adjacency_dictionary[to].append(fr)

    def print_nodes_connection(self):
        for key, values in self.adjacency_dictionary.items():
            for value in values:
                print(f"{key} is connected to {value}")
                
    def delete_edge(self, fr:str, to:str):
       
        if fr not in self.node_dictionary:
            print(f"from node, '{fr}' does not exist!!!")
            return
        if to not in self.node_dictionary:
            print(f"to node, '{to}' does not exist!!!")
            return
        if fr in self.adjacency_dictionary:
            for edge in self.adjacency_dictionary[fr]:
                if edge == to:
                    self.adjacency_dictionary[fr].remove(edge)
                    print(f"edge between {fr} and {to} is removed successfully")
            
            return
        
    def delete_node(self, label:str):

        keys_to_delete = [key for key, value in self.node_dictionary.items() if value == label]     
        for key in keys_to_delete:
            del self.node_dictionary[key]
        print(f"node {label} is removed from node dictionary")
        
        del self.adjacency_dictionary[label]
        for node in self.adjacency_dictionary.values():
            for i in node:
                if i == label:
                    node.remove(i)
                    print(f"node {i} is removed from from adjacency dictionary")
        return

        


new_graph = Graph()
new_graph.add_node("amin")
new_graph.add_node("mobin")
new_graph.add_node("mehdi")
new_graph.add_node("shariat")
new_graph.add_node("ahoora")
new_graph.add_node("epack")
new_graph.add_node("mahmoodhood")
new_graph.add_node("nosrat")


new_graph.add_edge("amin", "mehdi")
new_graph.add_edge("mahmoodhood", "mobin")
new_graph.add_edge("mahmoodhood", "amin")
new_graph.add_edge("amin", "nosrat")
new_graph.add_edge("mehdi", "mobin")
new_graph.add_edge("amin", "mobin")
new_graph.add_edge("chaghal", "mobin")
new_graph.add_edge("ahoora", "mobin")
new_graph.add_edge("ahoora", "amin")
new_graph.add_edge("mehdi", "ahoora")

new_graph.delete_edge("mehdi","ahoora")
new_graph.delete_node("amin")
new_graph.delete_node("mahmoodhood")
new_graph.print_nodes_connection()


