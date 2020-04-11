import pdb
import os
import matplotlib.pyplot as plt

class Analyzer(object):
    RUNS_DIR = 'runs'
    os.makedirs(RUNS_DIR, exist_ok=True)

    def __init__(self, name):
        self.name     = name
        self.cwd      = Analyzer.RUNS_DIR+'/'+name
        self.rewards  = []
        self.episodes = []
        self.moves    = []
        os.makedirs(self.cwd, exist_ok=False)

    def run(self, digest):
        self.unpack_digest(digest)

        self.moves_vs_episodes()
        self.rewards_vs_episodes()

    def unpack_digest(self, digest):
        for fact in digest.facts:
            self.rewards.append(fact["reward"])
            self.episodes.append(fact["episode"])
            self.moves.append(fact["moves"])

    def rewards_vs_episodes(self):
        self.plot_y_vs_x('rewards', self.rewards, 'episodes', self.episodes)
        plt.savefig(self.cwd + '/rewards_vs_episodes')

    def moves_vs_episodes(self):
        self.plot_y_vs_x('moves', self.moves, 'episodes', self.episodes)
        plt.savefig(self.cwd + '/moves_vs_episodes')

    def plot_y_vs_x(self, y_label, y_data, x_label, x_data):
        plt.title(y_label + " vs " + x_label)
        plt.plot(x_data, y_data, 'bo')
        plt.xlabel(x_label)
        plt.ylabel(y_label)

