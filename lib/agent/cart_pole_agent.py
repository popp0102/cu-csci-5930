import random
import numpy as np
from .agent import Agent

class CartPoleAgent(Agent):
    def __init__(self, max_action):
        super().__init__(max_action)
        self.best_weights = np.random.rand(4) * 2 - 1

    def select_action(self, observation):
        action = 0 if np.matmul(self.best_weights, observation) < 0 else 1
        return action

    def save(self):
        return { "best_weights": self.best_weights.tolist() }

    def load(self, training):
        if training != None:
            self.best_weights = training["best_weights"]

    def train(self, env, episodes):
        best_reward = 0
        for episode in range(episodes):
            weights = np.random.rand(4) * 2 - 1
            reward  = self.run_training_episode(weights, env)

            if reward > best_reward:
                best_reward       = reward
                self.best_weights = weights
                if reward == 200:
                    break

    def run_training_episode(self, weights, env):
        done         = False
        observation  = env.reset()
        total_reward = 0
        while not done:
            action = 0 if np.matmul(weights, observation) < 0 else 1
            if not self.is_valid_action(action):
                raise ValueError("Invalid action taken: {}".format(action))

            observation, reward, done, _ = env.step(action)
            total_reward += reward

            if done:
                break

        return total_reward

