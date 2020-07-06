import connexion
import six

from swagger_server.models.message import Message  # noqa: E501
from swagger_server import util


def get_message_by_id(messageId):  # noqa: E501
    """Find message by ID

    Returns a single message # noqa: E501

    :param messageId: ID of message to return
    :type messageId: str

    :rtype: Message
    """

    response = Message("A comprehensive journey into the PRESENT of Devops")

    return response
