import random

class Agent(object):
    def __init__(self, max_action):
        self.valid_actions = [x for x in range(max_action)]

    def is_valid_action(self, action):
        return action in self.valid_actions

    def take_random_action(self):
        return random.choice(self.valid_actions)

    def save():
        raise NotImplementedError

    def load():
        raise NotImplementedError

    def select_action(observation):
        raise NotImplementedError

    def train(self):
        raise NotImplementedError

