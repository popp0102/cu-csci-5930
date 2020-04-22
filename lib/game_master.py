import pdb
import cv2
import matplotlib.pyplot as plt
import numpy as np

from time import sleep
from .digest import Digest

NUM_FRAMES = 4

class GameMaster(object):
    def __init__(self, env, agent):
        self.env    = env
        self.agent  = agent
        self.frames = 0

    def run_season(self, season, num_episodes, training):
        self.agent.load_networks()

        if training:
            self.fill_agent_memory()

        digest     = Digest()
        best_score = -1
        for i in range(num_episodes):
            moves, score = self.run_episode(i, training)

            if score > best_score:
                best_score = score
                self.agent.save_networks()

            digest.add_fact(i, moves, score, self.agent.epsilon)

        return digest

    def run_episode(self, episode, training):
        self.env.reset()
        state, _, _, _ = self.create_experience(0)
        self.frames    = 0
        done           = False
        score          = 0
        moves          = 0
        while not done:
            action = self.agent.select_action(state, self.env)
            (next_state, reward, done, penalty) = self.create_experience(action)
            if training:
                self.agent.remember(state, next_state, reward - penalty, action, done)
            next_state = state

            score       += reward
            moves       += 1
            self.frames += 1

            if training:
                self.agent.train(episode)

        print("\n\nEpisode: {}   Moves: {}   Score: {}   Epsilon: {}   Loss: {}".format(episode, moves, score, self.agent.epsilon, self.agent.loss))

        return (moves, score)

    def fill_agent_memory(self):
        while (not self.agent.memory_is_full()):
            self.env.reset()
            state, _, _, _ = self.create_experience(0)
            done = False
            while not done:
                action = self.agent.take_random_action()
                (next_state, reward, done, penalty) = self.create_experience(action)
                self.agent.remember(state, next_state, reward - penalty, action, done)
                next_state = state

    def create_experience(self, action):
        state   = []
        reward  = 0
        done    = False
        penalty = 0
        for i in range(NUM_FRAMES):
            if not done:
                step_state, step_reward, step_done, info = self.env.step(action)
            if done and info['ale.lives'] == 0:
                penalty = 100

            processed_state = self.process_frame(step_state)
            state.append(processed_state)
            reward += step_reward
            done   |= step_done
        state = np.array(state)
        state = state.reshape(84,84,NUM_FRAMES)
        return (state, reward, done, penalty)

    def process_frame(self, observation):
        down_sample     = cv2.resize(observation, (84, 110)) # down sample as per the paper
        gray_scale      = cv2.cvtColor(down_sample, cv2.COLOR_BGR2GRAY) # change to grayscale
        obs_slice       = gray_scale[26:110,:] # slice out only the portion that matters
        _, normalize    = cv2.threshold(obs_slice,1,255,cv2.THRESH_BINARY)
        processed_state = np.reshape(normalize,(84,84))
        return processed_state

