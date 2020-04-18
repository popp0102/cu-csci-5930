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
            action = self.take_random_action()
        else:
            # get action from neural network
            action = self.take_random_action()
        return action

    def remember(self, old_observation, new_observation, reward, done, action):
        self.memory.memorize(old_observation, new_observation, reward, done, action)

    def memory_is_full(self):
        return self.memory.is_full()

    def train(self):
        return

