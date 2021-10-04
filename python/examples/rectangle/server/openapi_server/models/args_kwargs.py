# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from openapi_server.models.base_model_ import Model
from openapi_server import util


class ArgsKwargs(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, args=None, kwargs=None):  # noqa: E501
        """ArgsKwargs - a model defined in OpenAPI

        :param args: The args of this ArgsKwargs.  # noqa: E501
        :type args: List[object]
        :param kwargs: The kwargs of this ArgsKwargs.  # noqa: E501
        :type kwargs: Dict[str, object]
        """
        self.openapi_types = {
            'args': List[object],
            'kwargs': Dict[str, object]
        }

        self.attribute_map = {
            'args': 'args',
            'kwargs': 'kwargs'
        }

        self._args = args
        self._kwargs = kwargs

    @classmethod
    def from_dict(cls, dikt) -> 'ArgsKwargs':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The ArgsKwargs of this ArgsKwargs.  # noqa: E501
        :rtype: ArgsKwargs
        """
        return util.deserialize_model(dikt, cls)

    @property
    def args(self):
        """Gets the args of this ArgsKwargs.


        :return: The args of this ArgsKwargs.
        :rtype: List[object]
        """
        return self._args

    @args.setter
    def args(self, args):
        """Sets the args of this ArgsKwargs.


        :param args: The args of this ArgsKwargs.
        :type args: List[object]
        """
        if args is None:
            raise ValueError("Invalid value for `args`, must not be `None`")  # noqa: E501

        self._args = args

    @property
    def kwargs(self):
        """Gets the kwargs of this ArgsKwargs.


        :return: The kwargs of this ArgsKwargs.
        :rtype: Dict[str, object]
        """
        return self._kwargs

    @kwargs.setter
    def kwargs(self, kwargs):
        """Sets the kwargs of this ArgsKwargs.


        :param kwargs: The kwargs of this ArgsKwargs.
        :type kwargs: Dict[str, object]
        """
        if kwargs is None:
            raise ValueError("Invalid value for `kwargs`, must not be `None`")  # noqa: E501

        self._kwargs = kwargs