# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from openapi_server.models.base_model_ import Model
from openapi_server import util


class InlineResponseDefault(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, code=None, message=None, stacktrace=None):  # noqa: E501
        """InlineResponseDefault - a model defined in OpenAPI

        :param code: The code of this InlineResponseDefault.  # noqa: E501
        :type code: int
        :param message: The message of this InlineResponseDefault.  # noqa: E501
        :type message: str
        :param stacktrace: The stacktrace of this InlineResponseDefault.  # noqa: E501
        :type stacktrace: str
        """
        self.openapi_types = {
            'code': int,
            'message': str,
            'stacktrace': str
        }

        self.attribute_map = {
            'code': 'code',
            'message': 'message',
            'stacktrace': 'stacktrace'
        }

        self._code = code
        self._message = message
        self._stacktrace = stacktrace

    @classmethod
    def from_dict(cls, dikt) -> 'InlineResponseDefault':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The inline_response_default of this InlineResponseDefault.  # noqa: E501
        :rtype: InlineResponseDefault
        """
        return util.deserialize_model(dikt, cls)

    @property
    def code(self):
        """Gets the code of this InlineResponseDefault.


        :return: The code of this InlineResponseDefault.
        :rtype: int
        """
        return self._code

    @code.setter
    def code(self, code):
        """Sets the code of this InlineResponseDefault.


        :param code: The code of this InlineResponseDefault.
        :type code: int
        """
        if code is None:
            raise ValueError("Invalid value for `code`, must not be `None`")  # noqa: E501

        self._code = code

    @property
    def message(self):
        """Gets the message of this InlineResponseDefault.


        :return: The message of this InlineResponseDefault.
        :rtype: str
        """
        return self._message

    @message.setter
    def message(self, message):
        """Sets the message of this InlineResponseDefault.


        :param message: The message of this InlineResponseDefault.
        :type message: str
        """
        if message is None:
            raise ValueError("Invalid value for `message`, must not be `None`")  # noqa: E501

        self._message = message

    @property
    def stacktrace(self):
        """Gets the stacktrace of this InlineResponseDefault.


        :return: The stacktrace of this InlineResponseDefault.
        :rtype: str
        """
        return self._stacktrace

    @stacktrace.setter
    def stacktrace(self, stacktrace):
        """Sets the stacktrace of this InlineResponseDefault.


        :param stacktrace: The stacktrace of this InlineResponseDefault.
        :type stacktrace: str
        """

        self._stacktrace = stacktrace