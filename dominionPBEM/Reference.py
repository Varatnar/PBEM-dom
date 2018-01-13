import os
import json
import datetime
import pprint

from . import Constants


class Reference:

    data = dict()

    def __init__(self):
        self.data['lastUpdated'] = str(datetime.datetime.now())
        self.data['trackedGames'] = []

    def create_json(self):

        path = os.path.join(Constants.HOME_DIR_PATH, Constants.REFERENCE_DIR, Constants.REFERENCE_FILE)

        with open(path, 'w') as refFile:
            json.dump(self.data, refFile, indent=4)

    def read_json(self):

        path = os.path.join(Constants.HOME_DIR_PATH, Constants.REFERENCE_DIR, Constants.REFERENCE_FILE)

        with open(path, 'r') as refFile:
            temp_data = json.load(refFile)

        self.__init__()
        self.data['trackedGames'] = temp_data['trackedGames']

    def add_game(self, game_name, turn):

        game = dict()
        game['name'] = game_name
        game['turn'] = turn

        self.data['trackedGames'].append(game)

    def debug(self):

        pprint.pprint(self.data)
