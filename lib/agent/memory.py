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

    def memorize(self, state, new_state, reward, action):
        experience                     = (state, new_state, reward, action)
        self.memory[self.memory_index] = experience
        self.memory_index              = (self.memory_index + 1) % self.memory_capacity

    def recall(self):
        # random samples to break any sequential correlation
        memory_batch = random.sample(self.memory, self.recall_size)
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

