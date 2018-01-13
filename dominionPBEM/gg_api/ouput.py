from . import utils

import base64
from email.mime.audio import MIMEAudio
from email.mime.base import MIMEBase
from email.mime.image import MIMEImage
from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import mimetypes
import os

from apiclient import errors

SELF_EMAIL = "me"
TURN_EMAIL = "turns@llamaserver.net"
TEMP_FILE_PATH = "resources/simpleAttachment.data"
TEMP_FILE_NAME = "simpleAttachment.data"


def create_message_content(sender, receiver, content='', subject=''):
    message = MIMEText(content)
    message['to'] = receiver
    message['from'] = sender
    message['subject'] = subject
    return {'raw': base64.urlsafe_b64encode(message.as_bytes()).decode()}


def create_turn_message_object():
    message = MIMEMultipart()

    message['to'] = TURN_EMAIL
    message['from'] = SELF_EMAIL
    message['subject'] = 'Renaissance'
    message.attach(MIMEText(""))

    with open(TEMP_FILE_PATH, "rb") as file:
        part = MIMEApplication(
            file.read(),
            Name=TEMP_FILE_NAME
        )

    part.add_header('Content-Disposition', 'attachment', filename=TEMP_FILE_NAME)

    message.attach(part)

    return {'raw': base64.urlsafe_b64encode(message.as_bytes()).decode()}


def send_turn_mail():
    service = utils.create_base_query()

    service.users().messages().send(userId='me', body=create_turn_message_object()).execute()
