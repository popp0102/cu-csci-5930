import pdb
import os
import json
import matplotlib.pyplot as plt

class Analyzer(object):
    RUNS_DIR = 'runs'
    os.makedirs(RUNS_DIR, exist_ok=True)

    def __init__(self, name, season):
        self.name     = name
        self.season   = season
        self.cwd      = Analyzer.RUNS_DIR + '/' + name + '/' + season
        self.rewards  = []
        self.episodes = []
        self.moves    = []
        os.makedirs(self.cwd, exist_ok=False)

    def run(self, digest):
        self.save_digest(digest)
        self.unpack_digest(digest)

        self.moves_vs_episodes()
        self.rewards_vs_episodes()

    def save_digest(self, digest):
        digest = {
            "name": self.name,
            "season": self.season,
            "facts": digest.facts,
        }
        with open(self.cwd + '/' + 'digest.json', 'w') as fp:
            json.dump(digest, fp, indent=1)

    def unpack_digest(self, digest):
        for fact in digest.facts:
            self.rewards.append(fact["reward"])
            self.episodes.append(fact["episode"])
            self.moves.append(fact["moves"])

    def rewards_vs_episodes(self):
        plt.figure()
        self.plot_y_vs_x('rewards', self.rewards, 'episodes', self.episodes)
        plt.draw()
        plt.savefig(self.cwd + '/' + 'rewards_vs_episodes')

    def moves_vs_episodes(self):
        plt.figure()
        self.plot_y_vs_x('moves', self.moves, 'episodes', self.episodes)
        plt.draw()
        plt.savefig(self.cwd + '/' + 'moves_vs_episodes')

    def plot_y_vs_x(self, y_label, y_data, x_label, x_data):
        title = "{} vs {} ({} / {})".format(y_label, x_label, self.name, self.season)
        plt.title(title)
        plt.plot(x_data, y_data, 'bo')
        plt.ylim(bottom=0)
        plt.xlabel(x_label)
        plt.ylabel(y_label)

