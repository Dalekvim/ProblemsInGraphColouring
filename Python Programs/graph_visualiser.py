# Graph Visualiser
# By Vimal Vinod

import networkx as nx
import matplotlib.pyplot as plt


def draw(graph_name, num_nodes):
    if graph_name == "complete":
        nx.draw_circular(nx.complete_graph(int(num_nodes)))
    if graph_name == "cycle":
        nx.draw_circular(nx.cycle_graph(int(num_nodes)))
    if graph_name == "ladder":
        nx.draw(nx.ladder_graph(int(num_nodes)))
    if graph_name == "path":
        nx.draw(nx.path_graph(int(num_nodes)))
    if graph_name == "star":
        nx.draw(nx.star_graph(int(num_nodes)))
    if graph_name == "wheel":
        nx.draw(nx.wheel_graph(int(num_nodes)))
    


def draw_bipartite(graph_name, m, n):
    if graph_name == "complete":
        G = nx.complete_bipartite_graph(int(m), int(n))
        top = nx.bipartite.sets(G)[0]
        nx.draw(G, nx.bipartite_layout(G, top))


print("""Welcome to Graph Visualiser Version 1.0.0.
Type "help" to know more about how this works.
""")

while True:
    instruction = input("\n>>> ").lower()

    if instruction == "help":
        print("""This graph visualiser is implemented using networkx.
Instructions should be entered in the following order:

command graph_name [graph_type] num_nodes [num_nodes_bipartite]

More information can be found in the short documentation I've placed in the same directory.
""")

    command = instruction.split(" ")


    if command[0] == "draw":
        # Format:
        # command[0] = command E.g. draw
        if "bipartite" in command:
            draw_bipartite(command[1], command[3], command[4])
        else:
            # Format:
            # command[1] = graph name E.g. complete, cycle, path
            # command[2] = # verticies E.g. 1, 2, 3,...
            draw(command[1], command[2])
        plt.show()
