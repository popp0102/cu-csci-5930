import os
import json
import matplotlib.pyplot as plt

class Analyzer(object):
    RUNS_DIR = 'runs'
    os.makedirs(RUNS_DIR, exist_ok=True)

    def __init__(self, name, season):
        self.name     = name
        self.season   = season
        self.cwd      = "{}/{}/{}".format(Analyzer.RUNS_DIR, name, season)
        self.scores   = []
        self.episodes = []
        self.moves    = []
        os.makedirs(self.cwd, exist_ok=False)

    def run(self, digest):
        self.save_digest(digest)
        self.unpack_digest(digest)

        self.plot_moves_vs_episodes()
        self.plot_scores_vs_episodes()

    def save_digest(self, digest):
        digest = {
            "name": self.name,
            "season": self.season,
            "facts": digest.facts,
        }
        filename = "{}/{}".format(self.cwd, 'digest.json')
        with open(filename, 'w') as fp:
            json.dump(digest, fp, indent=1)

    def unpack_digest(self, digest):
        for fact in digest.facts:
            self.scores.append(fact["score"])
            self.episodes.append(fact["episode"])
            self.moves.append(fact["moves"])

    def plot_scores_vs_episodes(self):
        self.plot_y_vs_x('scores', self.scores, 'episodes', self.episodes)

    def plot_moves_vs_episodes(self):
        self.plot_y_vs_x('moves', self.moves, 'episodes', self.episodes)

    def plot_y_vs_x(self, y_label, y_data, x_label, x_data):
        title    = "{} vs {} ({} / {})".format(y_label, x_label, self.name, self.season)
        filename = "{}/{}_vs_{}".format(self.cwd, y_label, x_label)

        plt.figure()
        plt.title(title)
        plt.xlabel(x_label)
        plt.ylabel(y_label)
        plt.plot(x_data, y_data, 'bo')
        plt.ylim(bottom=0)
        plt.draw()
        plt.savefig(filename)

