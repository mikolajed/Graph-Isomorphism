import os
import tkinter as tk
from tkinter import ttk
from tkinter.filedialog import askopenfilename
import networkx as nx
import matplotlib.pyplot as plt

# Function to handle the draw button click event
def draw_graph():
    # Get the selected file from the dropdown menu
    selected_file = askopenfilename(initialdir=os.getcwd(), title="Select Input File")
    
    # Read the input file
    with open(selected_file, 'r') as file:
        # Read the number of nodes and edges for the first graph
        line = file.readline().split()
        n1 = int(line[0])
        m1 = int(line[1])

        # Create an empty graph for the first graph
        G1 = nx.Graph()

        # Add nodes to the first graph
        nodes1 = range(0, n1)
        G1.add_nodes_from(nodes1)

        # Add edges to the first graph
        for _ in range(m1):
            u, v = map(int, file.readline().split())
            G1.add_edge(u, v)

        # Read the number of nodes and edges for the second graph
        line = file.readline().split()
        n2 = int(line[0])
        m2 = int(line[1])

        # Create an empty graph for the second graph
        G2 = nx.Graph()

        # Add nodes to the second graph
        nodes2 = range(0, n2)
        G2.add_nodes_from(nodes2)

        # Add edges to the second graph
        for _ in range(m2):
            u, v = map(int, file.readline().split())
            G2.add_edge(u, v)

    # Choose which graph to draw based on the selected option
    if selected_graph_var.get() == "First Graph":
        graph_to_draw = G1
    else:
        graph_to_draw = G2

    # Draw the graph
    pos = nx.spring_layout(graph_to_draw)  # Choose a layout for the graph
    nx.draw(graph_to_draw, pos, with_labels=True, node_color='lightblue', edge_color='gray', width=1, alpha=0.7)

    # Show the graph
    plt.show()

# Create the main window
root = tk.Tk()
root.title("Graph Drawing App")

# Create a frame for the graph display
graph_frame = tk.Frame(root)
graph_frame.grid(row=0, column=0)


# Create a frame for the controls
controls_frame = tk.Frame(root)
controls_frame.grid(row=0, column=1)

# Create a label for the graph selection
selected_graph_label = tk.Label(controls_frame, text="Select a graph:")
selected_graph_label.grid(row=0, column=0)

# Create a dropdown menu to select the graph
selected_graph_var = tk.StringVar()
graph_dropdown = ttk.Combobox(controls_frame, textvariable=selected_graph_var)
graph_dropdown['values'] = ('First Graph', 'Second Graph')
graph_dropdown.grid(row=1, column=0)

# Create a draw button
draw_button = tk.Button(controls_frame, text="Draw", command=draw_graph)
draw_button.grid(row=2, column=0)

# Run the GUI event loop
root.mainloop()
