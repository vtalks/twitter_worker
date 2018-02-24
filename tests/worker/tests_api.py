import mock
import unittest

from tests.tests_data import fake_talk_json
from worker.api import API


def mocked_requests_get(*args, **kwargs):
    class MockResponse:
        def __init__(self, json_data, status_code):
            self.json_data = json_data
            self.status_code = status_code

        def json(self):
            return self.json_data

    return MockResponse(fake_talk_json, 200)


class APITest(unittest.TestCase):

    @mock.patch('requests.get', side_effect=mocked_requests_get)
    def test_get_random_talk(self, mock_get):
        api = API()
        talk_json = api.get_random_talk()
        self.assertIsNotNone(talk_json)
        self.assertIsInstance(talk_json, dict)
