import random
from .agent import Agent

class RandomAgent(Agent):
    def select_action(self):
        return random.choice(self.valid_actions)

