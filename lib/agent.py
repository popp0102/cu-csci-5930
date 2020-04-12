class Agent(object):
    def __init__(self, max_action):
        self.valid_actions = [x for x in range(max_action)]

    def train(self, env, episodes):
        raise NotImplementedError

    def is_valid_action(self, action):
        return action in self.valid_actions

    def type():
        raise NotImplementedError

    def select_action(observation):
        raise NotImplementedError

