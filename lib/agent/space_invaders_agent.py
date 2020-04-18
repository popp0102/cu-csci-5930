import random
import numpy as np
from .agent import Agent
from .memory import Memory

class SpaceInvadersAgent(Agent):
    def __init__(self, max_action, alpha, epsilon, gamma, memory_size=50000, recall_size=32):
        super().__init__(max_action)

        self.alpha   = alpha
        self.epsilon = epsilon
        self.gamma   = gamma
        self.memory  = Memory(memory_size, recall_size)

    def select_action(self, observation):
        action = None
        if random.uniform(0,1) < self.epsilon:
            action = random.choice(self.valid_actions)
        else:
            # get action from neural network
            action = None
        return action

    def train(self, env, episodes):
        return
