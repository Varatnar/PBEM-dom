from dominionPBEM.Reference import Reference
from dominionPBEM.GameHandler import GameHandler
import dominionPBEM.gg_api.input as gg_api


gameAPI = GameHandler()

test = Reference()

test.add_game("testGame2", 1)
test.add_game("testGame4", 4)
test.add_game("testGame3", 5)

test.debug()

test.create_json()
test.read_json()

test.debug()

gg_api.get_list_mail_dominion()
