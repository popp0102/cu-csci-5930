import random
import numpy as np
from .agent import Agent

class SpaceInvadersAgent(Agent):
    def save(self):
        return

    def load(self, training):
        return

    def select_action(self, observation):
        return random.choice(self.valid_actions)

    def train(self, env, episodes):
        return
