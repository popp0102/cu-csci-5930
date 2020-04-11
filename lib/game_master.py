from .digest import Digest

class GameMaster(object):
    def __init__(self, env, agent):
        self.env   = env
        self.agent = agent

    def run_season(self, name, num_episodes, render=False):
        digest = Digest(name)
        for i in range(num_episodes):
            moves, reward = self.run_episode(render)
            digest.add_fact(i, moves, reward)

        self.env.close()
        return digest

    def run_episode(self, render=False):
        done         = False
        observation  = self.env.reset()
        total_reward = 0
        moves        = 0
        while not done:
            moves += 1
            if render:
                self.env.render()

            action = self.agent.select_action()

            observation, reward, done, _ = self.env.step(action)
            total_reward += reward

            if done:
                break

        return (moves, total_reward)

