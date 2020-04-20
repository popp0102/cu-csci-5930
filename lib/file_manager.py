import os
import json
from pathlib import Path

class FileManager(object):
    def __init__(self, game, season):
        self.cwd = "runs/{}/season_{}".format(game, season)
        os.makedirs(self.cwd, exist_ok=True)

    def save(self, data, filename):
        filename_path = self.get_fullpath(filename)
        path          = Path(filename_path)

        if path.exists():
            print("!!! Warning - not saving file ", filename_path, " because it already exists !!!")
            return

        with open(filename_path, 'w') as fp:
            json.dump(data, fp, indent=1) 

    def load(self, filename):
        filename_path = self.get_fullpath(filename)
        path          = Path(filename_path)

        if not path.exists():
            return None

        with open(filename_path) as fp:
            data = json.load(fp)

        return data

    def get_fullpath(self, filename):
        return "{}/{}".format(self.cwd, filename)
