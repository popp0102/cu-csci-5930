import pdb
import random
import numpy as np
from .agent import Agent
from .memory import Memory
from .deep_q_neural_network import DeepQNeuralNetwork

class SpaceInvadersAgent(Agent):
    def __init__(self, num_actions, alpha, epsilon, gamma, fc_num_neurons, memory_capacity, batch_size):
        super().__init__(num_actions)

        self.epsilon = epsilon
        self.gamma   = gamma
        self.memory  = Memory(memory_capacity, batch_size)
        self.batch_size = batch_size

        self.policy_network = DeepQNeuralNetwork(num_actions, alpha, fc_num_neurons)
        self.target_network = DeepQNeuralNetwork(num_actions, alpha, fc_num_neurons)

    def select_action(self, observation, env):
        action = None
        if random.uniform(0,1) < self.epsilon:
            action = self.take_random_action()
        else:
            action_q_values = self.policy_network.model.predict(observation.reshape(1,210,160,3))
            action          = np.argmax(action_q_values)

        return action

    def remember(self, old_observation, new_observation, reward, action):
        self.memory.memorize(old_observation, new_observation, reward, action) # this is an experience

    def memory_is_full(self):
        return self.memory.is_full()

    def train(self):
        experiences = self.memory.recall()

        states      = experiences["states"]
        next_states = experiences["next_states"]
        rewards     = experiences["rewards"]
        actions     = experiences["actions"]

        q_current_values = self.policy_network.model.predict(states)
        q_next_values    = self.target_network.model.predict(next_states)
        q_target         = np.copy(q_current_values)

        first_dim_indices = np.arange(self.batch_size)
        q_target[first_dim_indices, actions] = rewards + self.gamma*np.max(q_next_values, axis=1) # Bellman Equation

        self.policy_network.model.train_on_batch(states, q_target) # update weights

        self.epsilon = self.epsilon - 0.00001
        if self.epsilon < 0.05:
            self.epsilon = 0.05

