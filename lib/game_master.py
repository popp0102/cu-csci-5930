from time import sleep
from .digest import Digest

class GameMaster(object):
    def __init__(self, env, agent):
        self.env   = env
        self.agent = agent

    def run_season(self, num_episodes):
        digest = Digest()
        for i in range(num_episodes):
            moves, score = self.run_episode(render=False)
            digest.add_fact(i, moves, score)

        return digest

    def run_episode(self, render):
        done         = False
        observation  = self.env.reset()
        total_reward = 0
        moves        = 0
        while not done:
            moves += 1
            if render:
                self.env.render()
                if moves % 30 == 0:
                    sleep(0.2)

            action = self.agent.select_action(observation)

            observation, reward, done, _ = self.env.step(action)
            total_reward += reward

            if done:
                break

        if render:
            print("Moves: {}, Reward: {}".format(moves, total_reward))

        return (moves, total_reward)

