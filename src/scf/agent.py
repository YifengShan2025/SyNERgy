class Agent:
    def __init__(self, name, capabilities):
        self.name = name
        self.capabilities = capabilities
        self.state = {}

    def contribute(self, task):
        # Logic for agent's contribution to task
        return f"{self.name} contributes to {task}"
