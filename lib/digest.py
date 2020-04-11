class Digest(object):
    def __init__(self, name):
        self.name  = name
        self.facts = []

    def add_fact(self, episode, moves, reward):
        self.facts.append({
            "episode": episode,
            "reward":  reward,
            "moves":   moves
        })

