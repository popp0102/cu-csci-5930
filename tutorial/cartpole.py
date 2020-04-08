import numpy as np
import gym
import pdb

def run_episode(env, weights, render):
    observation  = env.reset()
    total_reward = 0
    for _ in range(200):
        if render:
            env.render()
        action = 0 if np.matmul(weights, observation) < 0 else 1
        observation, reward, done, info = env.step(action)
        total_reward += reward
        if done:
            break
    return total_reward

def train(env, type):
    bestweights = None
    bestreward  = 0
    weights     = np.random.rand(4) * 2 - 1
    for e in range(10000):
        if type == 'random':
            weights = np.random.rand(4) * 2 - 1
        elif type == 'hill':
            noise_scaling = 0.1
            weights = weights + (np.random.rand(4) * 2 - 1) * noise_scaling

        reward  = run_episode(env, weights, False)
        if reward > bestreward:
            bestreward  = reward
            bestweights = weights
            if reward == 200:
                print('Optimal Reward on Episode: {}'.format(e))
                break
    return bestweights

env          = gym.make('CartPole-v0')
bestweights  = train(env, 'random')
total_reward = run_episode(env, bestweights, True)
env.close()

print("Best weights: {}\nTotal Reward: {}".format(bestweights, total_reward))

