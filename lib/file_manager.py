import os
import json
from pathlib import Path

class FileManager(object):
    def __init__(self, game, season):
        self.cwd = "runs/{}/season_{}".format(game, season)
        os.makedirs(self.cwd, exist_ok=True)

    def save(self, data, filename):
        full_filename = self.get_fullpath(filename)
        path          = Path(filename)

        if path.exists():
            raise ValueError("{} already exists".format(full_filename))

        with open(full_filename, 'w') as fp:
            json.dump(data, fp, indent=1) 

    def load(self, filename):
        full_filename = self.get_fullpath(filename)
        path          = Path(full_filename)

        if not path.exists():
            return None

        with open(full_filename) as fp:
            data = json.load(fp)

        return data

    def get_fullpath(self, filename):
        return "{}/{}".format(self.cwd, filename)
