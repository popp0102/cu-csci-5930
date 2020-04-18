import random

class Memory(object):
    def __init__(self, memory_size, recall_size):
        self.memory_size  = memory_size
        self.memory       = [None] * memory_size
        self.memory_index = 0
        self.recall_size  = recall_size

    def memorize(self, old_observation, new_observation, reward, done, action):
        information               = (old_observation, new_observation, reward, done, action)
        self.memory[memory_index] = information
        memory_index              = (memory_index + 1) % self.memory_size

    def recall(self):
        start = random.randint(0, self.memory_size)
        end   = start + self.recall_size

        if end >= self.memory_size:
            start -= self.recall_size
            end   -= self.recall_size

        return self.memory[start:end]

