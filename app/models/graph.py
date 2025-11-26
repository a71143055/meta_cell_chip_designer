import networkx as nx

def circuit_graph_from_primitives(primitives):
    g = nx.Graph()
    for i, p in enumerate(primitives):
        g.add_node(i, kind=p.kind, value=p.value)
        if i > 0:
            g.add_edge(i-1, i)
    return g
