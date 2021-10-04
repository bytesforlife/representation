# coding: utf-8

from __future__ import absolute_import
import unittest

from flask import json
from six import BytesIO

from openapi_server.models.schema_error import SchemaError  # noqa: E501
from openapi_server.models.unknownbasetype import UNKNOWN_BASE_TYPE  # noqa: E501
from openapi_server.test import BaseTestCase


class TestDefaultController(BaseTestCase):
    """DefaultController integration test stubs"""

    def test_class_instance_member_call(self):
        """Test case for class_instance_member_call

        call member function of an instance of a server-side class
        """
        unknown_base_type = openapi_server.UNKNOWN_BASE_TYPE()
        headers = { 
            'Accept': 'application/json',
            'Content-Type': 'application/json',
        }
        response = self.client.open(
            '/classes/{class_uuid}/instances/{instance_uuid}/members/{member}/call'.format(class_uuid='class_uuid_example', instance_uuid='instance_uuid_example', member='member_example'),
            method='POST',
            headers=headers,
            data=json.dumps(unknown_base_type),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_class_member_call(self):
        """Test case for class_member_call

        call static member function of a server-side class
        """
        unknown_base_type = openapi_server.UNKNOWN_BASE_TYPE()
        headers = { 
            'Accept': 'application/json',
            'Content-Type': 'application/json',
        }
        response = self.client.open(
            '/classes/{class_uuid}/members/{member}/call'.format(class_uuid='class_uuid_example', member='member_example'),
            method='POST',
            headers=headers,
            data=json.dumps(unknown_base_type),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_classes_list(self):
        """Test case for classes_list

        list server-side classes
        """
        headers = { 
            'Accept': 'application/json',
        }
        response = self.client.open(
            '/classes/list',
            method='POST',
            headers=headers)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_classes_select(self):
        """Test case for classes_select

        select a server-side class
        """
        unknown_base_type = openapi_server.UNKNOWN_BASE_TYPE()
        headers = { 
            'Accept': 'application/json',
            'Content-Type': 'application/json',
        }
        response = self.client.open(
            '/classes/select',
            method='POST',
            headers=headers,
            data=json.dumps(unknown_base_type),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    unittest.main()
