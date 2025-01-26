import networkx as nx
import matplotlib.pyplot as mp

# Constants for node colors
ORIGINAL_NODE_COLOR = "lightblue"
MST_NODE_COLOR = "lightgreen"


# helper function to build a graph from a list of edges
def build_graph(edges):
    graph = nx.Graph()
    graph.add_weighted_edges_from(edges)
    return graph


# helper function to draw a graph with labels
# to avoid code duplicates
def draw_graph(graph, node_positions, node_color):
    nx.draw(
        graph,
        node_positions,
        with_labels=True,
        node_color=node_color,
        node_size=500,
        font_size=10,
    )
    labels = nx.get_edge_attributes(graph, "weight")
    nx.draw_networkx_edge_labels(graph, node_positions, edge_labels=labels)
    mp.show()


# prim's algorithm to find the minimum spanning tree
def prim_mst(graph, start_node, node_positions):
    # initialize an empty graph to build the MST
    mst = nx.Graph()
    visited = set()
    # initialize the edges list with the starting node
    # having (weight, from_node, to_node)
    edges = [(0, start_node, start_node)]  

    while edges:
        # select the edge with the smallest weight using lambda function
        weight, from_node, to_node = min(edges, key=lambda x: x[0])
        # remove the selected edge from the list
        edges.remove((weight, from_node, to_node))

        # if the node has not been visited yet
        if to_node not in visited:
            visited.add(to_node)
            # add the edge to the MST if the nodes are different
            if from_node != to_node:
                mst.add_edge(from_node, to_node, weight=weight)

            # add all edges from the newly visited node to the edges list
            for next_node, attr in graph[to_node].items():
                if next_node not in visited:
                    edges.append((attr["weight"], to_node, next_node))

            # draw the MST after each new edge is added
            draw_graph(mst, node_positions, node_color=MST_NODE_COLOR)

    return mst


#  edges list with their weights to build the graph
edges = [
    ("A", "B", 1),
    ("A", "C", 5),
    ("A", "G", 10),
    ("B", "D", 3),
    ("C", "D", 8),
    ("C", "E", 6),
    ("C", "Z", 9),
    ("D", "F", 1),
    ("E", "Z", 1),
    ("F", "Z", 6),
    ("G", "E", 3),
]
graph = build_graph(edges)

# we  are using spring layout to maintain node positions
node_positions = nx.spring_layout(graph)

# first we show the original graph  with light blue color nodes
draw_graph(graph, node_positions, node_color=ORIGINAL_NODE_COLOR)

# then we generate the minimum spanning tree using Prim's algorithm
mst = prim_mst(graph, "A", node_positions)
