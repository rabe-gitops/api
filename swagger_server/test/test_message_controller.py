# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.message import Message  # noqa: E501
from swagger_server.test import BaseTestCase


class TestMessageController(BaseTestCase):
    """MessageController integration test stubs"""

    def test_get_message_by_id(self):
        """Test case for get_message_by_id

        Find message by ID
        """
        response = self.client.open(
            '/message/{messageId}'.format(messageId='messageId_example'),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
