import networkx as nx
import matplotlib.pyplot as plt


class Graph:

    def __init__(self, details):
        self.name = details[0]
        try:
            if self.contains_bipartite(details):
                self.is_bipartite = True
                self.num_nodes_1 = int(details[2])
                self.num_nodes_2 = int(details[3])
            else:
                self.is_bipartite = False
                self.num_nodes = int(details[1])
        except TypeError:
            raise TypeError("Number of nodes must be an integer.")

    @staticmethod
    def contains_bipartite(details):
        return "bipartite" in details

    circular = ["complete", "cycle"]
    others = ["ladder", "path", "star", "wheel"]

    def draw(self):
        if self.is_bipartite:
            if self.name == "complete":
                graph = nx.complete_bipartite_graph(self.num_nodes_1, self.num_nodes_2)
                top = nx.bipartite.sets(graph)[0]
                nx.draw(graph, nx.bipartite_layout(graph, top))
        else:
            if self.name in self.circular:
                exec(f"nx.draw_circular(nx.{self.name}_graph(self.num_nodes))")
            elif self.name in self.others:
                exec(f"nx.draw(nx.{self.name}_graph(self.num_nodes))")
            else:
                print("That graph is not recognised.")
        plt.show()

    def colour(self):
        pass

    def save(self):
        pass
