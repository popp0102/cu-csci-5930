import os
import json
import matplotlib.pyplot as plt

class Analyzer(object):
    def __init__(self, cwd):
        self.cwd      = cwd
        self.scores   = []
        self.episodes = []
        self.moves    = []
        self.epsilons = []

    def create_graphs(self, digest, command):
        self.command = command

        self.unpack_digest(digest)

        self.plot_moves_vs_episodes()
        self.plot_scores_vs_episodes()
        self.plot_epsilon_vs_episodes()

    def unpack_digest(self, digest):
        for fact in digest.facts:
            self.scores.append(fact["score"])
            self.episodes.append(fact["episode"])
            self.moves.append(fact["moves"])
            self.epsilons.append(fact["epsilon"])

    def plot_epsilon_vs_episodes(self):
        self.plot_y_vs_x('epsilon', self.epsilons, 'episodes', self.episodes)

    def plot_scores_vs_episodes(self):
        self.plot_y_vs_x('scores', self.scores, 'episodes', self.episodes)

    def plot_moves_vs_episodes(self):
        self.plot_y_vs_x('moves', self.moves, 'episodes', self.episodes)

    def plot_y_vs_x(self, y_label, y_data, x_label, x_data):
        title    = "{} vs {}".format(y_label, x_label)
        filename = "{}/{}_vs_{}_{}".format(self.cwd, y_label, x_label, self.command)

        plt.figure()
        plt.title(title)
        plt.xlabel(x_label)
        plt.ylabel(y_label)
        plt.plot(x_data, y_data, 'bo')
        plt.ylim(bottom=0)
        plt.draw()
        plt.savefig(filename)

