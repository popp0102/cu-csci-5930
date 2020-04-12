import random
import numpy as np
from .agent import Agent

class RandomAgent(Agent):
    def type(self):
        return "random_agent"

    def select_action(self, observation):
        action = 0 if np.matmul(weights, observation) < 0 else 1
        return action

    def train(self, env, episodes):
        best_reward = 0
        weights     = []
        for episode in range(episodes):
            weights = np.random.rand(4) * 2 - 1
            reward  = self.run_training_episode(weights, env)

            if reward > best_reward:
                bestreward  = reward
                bestweights = weights
                if reward == 200:
                    break

        self.best_weights = weights
        return weights

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

