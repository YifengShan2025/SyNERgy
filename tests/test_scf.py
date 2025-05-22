import pytest
from scf.agent import Agent
from scf.interaction_graph import InteractionGraph

def test_agent_creation():
    agent = Agent(name="Nurse", capabilities=["record", "alert"])
    assert agent.name == "Nurse"
    assert "alert" in agent.capabilities

def test_interaction_graph():
    graph = InteractionGraph()
    agent1 = Agent("Doctor", ["diagnose"])
    agent2 = Agent("Pharmacist", ["dispense"])
    graph.add_agent(agent1)
    graph.add_agent(agent2)
    graph.add_interaction(agent1, agent2, weight=0.75)
    assert graph.graph.has_edge("Doctor", "Pharmacist")
