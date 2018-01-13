from enum import Enum
import os

DEFAULT_SAVE_PATH = os.getenv('APPDATA') + "\Dominions5\savedgames"
HOME_DIR_PATH = os.path.expanduser('~')
REFERENCE_DIR = ".dominionPBEM"
REFERENCE_FILE = ".baseReference"
NEW_TURN_IDENTIFIER = "New turn file"
TURN_RECEIVED_IDENTIFIER = "received for"


class MessageType(Enum):
    TURN_RECEIVED_CONFIRMATION = ('r', 'Confirmation for received turn message')
    NEW_TURN = ('n', 'New turn message')
    ERROR = ('e', 'ERROR')

    def __init__(self, code, message):
        self.code = code
        self.message = message
