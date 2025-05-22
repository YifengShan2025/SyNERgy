import networkx as nx

class InteractionGraph:
    def __init__(self):
        self.graph = nx.Graph()

    def add_agent(self, agent):
        self.graph.add_node(agent.name, agent=agent)

    def add_interaction(self, agent1, agent2, weight=1.0):
        self.graph.add_edge(agent1.name, agent2.name, weight=weight)
