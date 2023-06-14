import networkx as nx
import matplotlib.pyplot as plt

# Read the input
line = input().split()
n = int(line[0])
m = int(line[1])

# Create an empty graph
G = nx.Graph()

# Add nodes to the graph
nodes = range(0, n)
G.add_nodes_from(nodes)

# Add edges to the graph
for _ in range(m):
    u, v = map(int, input().split())
    G.add_edge(u, v)

# Draw the graph
pos = nx.spring_layout(G)  # Choose a layout for the graph
nx.draw(G, pos, with_labels=True, node_color='lightblue', edge_color='gray', width=1, alpha=0.7)

# Show the graph
plt.show()












