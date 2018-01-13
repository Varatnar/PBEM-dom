import re
from pprint import pprint

from . import utils
from .. import Constants
from ..Constants import MessageType


def get_list_mail_dominion():
    service = utils.create_base_query()

    results = service.users().messages().list(userId='me', q="label:dominion after:2018-01-10").execute()
    messages = results.get('messages', [])

    list_message = []

    if not messages:
        print("Error, no messages found")
    else:
        for message in messages:

            current_message = service.users().messages().get(userId='me', id=message['id']).execute()

            temp_message_info = parse_dominion_message(current_message)

            if temp_message_info['messageType'] is not MessageType.ERROR:
                list_message.append(parse_dominion_message(current_message))

        pprint(list_message)


def parse_dominion_message(message):
    """
    Given a google message object, extract the relevant data from it

    :param message: Google API message object
    :return: A game dictionary with information about the game
    """

    game = dict()

    for header in message['payload']['headers']:
        if header['name'] == "Subject":
            game = parse_dominion_message_subject(header['value'])

    return game


def parse_dominion_message_subject(message_subject):
    """
    Find out relevant information about the game from the title

    :param str message_subject:  The raw content of the message's subject
    :return: Dictionary with the relevant information
    """

    game = dict()

    # todo: Replace this weird if with a try-catch ?
    if Constants.NEW_TURN_IDENTIFIER in message_subject:
        regex = re.search('New turn file: (\w+), (\w+) turn (\d+)', message_subject)

        game_name = regex.group(1)
        game_current_turn = regex.group(3)
        game_played_nation = regex.group(2)
        message_type = MessageType.NEW_TURN

    elif Constants.TURN_RECEIVED_IDENTIFIER in message_subject:

        regex = re.search('(\w+): Turn (\d+) received for (\w+)', message_subject)

        game_name = regex.group(1)
        game_current_turn = regex.group(2)
        game_played_nation = regex.group(3)
        message_type = MessageType.TURN_RECEIVED_CONFIRMATION

    else:
        game_name = "ERROR"
        game_current_turn = "ERROR"
        game_played_nation = "ERROR"
        message_type = MessageType.ERROR

    game['name'] = game_name
    game['currentTurn'] = game_current_turn
    game['playedNation'] = game_played_nation
    game['messageType'] = message_type

    return game


def is_message_new(message):
    for labelsId in message['labelIds']:
        if labelsId == "UNREAD":
            return True

    return False
