import random

class Agent(object):
    def __init__(self, num_actions):
        self.num_actions   = num_actions
        self.valid_actions = [x for x in range(num_actions)]

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

