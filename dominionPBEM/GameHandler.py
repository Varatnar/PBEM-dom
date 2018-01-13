import os

from . import Constants


class GameHandler:

    base_reference_path = ''
    potential_games = []

    def __init__(self):
        self.look_for_reference_file()
        self.find_all_dominion_game()

    def look_for_reference_file(self):
        """

        :return:
        """
        ref_file_dir = os.path.join(Constants.HOME_DIR_PATH, Constants.REFERENCE_DIR)

        if not os.path.exists(ref_file_dir):
            os.mkdir(ref_file_dir)

        self.base_reference_path = ref_file_dir

    def find_all_dominion_game(self):
        directory_potential_game = []

        for entry in os.listdir(Constants.DEFAULT_SAVE_PATH):
            if os.path.isdir(Constants.DEFAULT_SAVE_PATH + "/" + entry):
                directory_potential_game.append(entry)

        self.potential_games = directory_potential_game

        return directory_potential_game

    def create_game_reference(self, game_name):
        """
        Create a reference file for a game, the file will contain information about turns

        :param str game_name:
        :return:
        """

        os.mkdir(os.path.join(self.base_reference_path, game_name))
