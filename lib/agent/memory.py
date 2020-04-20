import random
import numpy as np
import pdb

class Memory(object):
    def __init__(self, memory_capacity, recall_size):
        self.memory_capacity = memory_capacity
        self.memory          = [None] * memory_capacity
        self.memory_index    = 0
        self.recall_size     = recall_size
        self.memory_full     = False

    def is_full(self):
        return self.memory[-1] != None

    def memorize(self, old_observation, new_observation, reward, action):
        information                    = (old_observation, new_observation, reward, action)
        self.memory[self.memory_index] = information
        self.memory_index              = (self.memory_index + 1) % self.memory_capacity

    def recall(self):
        start = random.randint(0, self.memory_capacity)
        end   = start + self.recall_size

        if end >= self.memory_capacity:
            start -= self.recall_size
            end   -= self.recall_size

        memory_batch = self.memory[start:end]
        experiences  = self.transform(memory_batch)

        return experiences

    def transform(self, memory_batch):
        states      = []
        next_states = []
        actions     = []
        rewards     = []

        for mem_entry in memory_batch:
            states.append(mem_entry[0])
            next_states.append(mem_entry[1])
            rewards.append(mem_entry[2])
            actions.append(mem_entry[3])

        experiences = {
            "states" : np.array(states),
            "next_states" : np.array(next_states),
            "actions" : np.array(actions),
            "rewards" : np.array(rewards),
        }

        return experiences

