import random

class Memory(object):
    def __init__(self, capacity):
        self.memory       = [None] * capacity
        self.capacity     = capacity
        self.memory_place = 0

    def memorize(self, old_observation, new_observation, reward, done, action):
        information               = (old_observation, new_observation, reward, done, action)
        self.memory[memory_place] = information
        memory_place              = (memory_place + 1) % self.capacity

    def recall(self, batch_size):
        start = random.randint(0, self.capacity)
        end   = start + batch_size

        if end >= capacity:
            start -= batch_size
            end   -= batch_size

        return self.memory[start:end]

