class Digest(object):
    def __init__(self, name):
        self.name  = name
        self.facts = []

    def add_fact(self, episode, moves, score):
        self.facts.append({
            "episode": episode,
            "score": score,
            "moves": moves
        })

