from time import sleep
from .digest import Digest

class GameMaster(object):
    def __init__(self, env, agent):
        self.env    = env
        self.agent  = agent
        self.frames = 0

    def run_season(self, num_episodes, training, render):
        self.fill_agent_memory()

        digest = Digest()
        for i in range(num_episodes):
            moves, score = self.run_episode(i, training, render)
            digest.add_fact(i, moves, score)

        return digest

    def run_episode(self, episode, training, render):
        current_observation = self.env.reset()
        self.frames         = 0
        done                = False
        score               = 0
        moves               = 0
        while not done:
            action                               = self.agent.select_action(current_observation, self.env)
            next_observation, reward, done, info = self.env.step(action)
            self.agent.remember(current_observation, next_observation, reward, action)
            current_observation                  = next_observation

            score       += reward
            moves       += 1
            self.frames += 1

            if training:
                self.agent.train()

            if render:
                self.render_game()

        print("Episode: {}   Moves: {}   Score: {}   Epsilon: {}".format(episode, moves, score, self.agent.epsilon))

        return (moves, score)

    def fill_agent_memory(self):
        current_observation = self.env.reset()
        while (not self.agent.memory_is_full()):
            action                               = self.agent.take_random_action()
            next_observation, reward, done, info = self.env.step(action)
            self.agent.remember(current_observation, next_observation, reward, action)
            current_observation                  = next_observation

    def render_game(self):
        self.env.render()
        if self.frames % 30 == 0:
            sleep(0.2)

