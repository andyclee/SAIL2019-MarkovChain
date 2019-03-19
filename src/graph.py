class Vertex:
    """
    Vertex in Graph
    """

class Edge:
    """
    Edge in Graph
    """

class Graph:
    """
    Modified Graph structure, creates the chain from list of WordTokens
    """

    def __init__(self, tokens):
        self.tokens = tokens
        self.graph = self.create_graph()

    def create_graph(self):
