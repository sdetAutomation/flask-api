import unittest

from unittest import mock

from api.aggregate import rest_call_to_another_other_api


class MockResponse:
    def __init__(self, content, status_code):
        self.content = content
        self.status_code = status_code


# This method will be used by the mock to replace requests.get
def mocked_requests_get(*args, **kwargs):
    if args[0] == "https://springboot-gradle.herokuapp.com/locations/v1":
        return MockResponse('[{"id":1,"state":"mn","capital":"st paul"}]', 200)
    return MockResponse(None, 404)


class IntegrationTest(unittest.TestCase):

    @mock.patch('requests.get', side_effect=mocked_requests_get)
    def test_tc0001_rest_call_to_another_other_api(self, mock_request):
        td_message = '{"id":1,"state":"mn","capital":"st paul"}'
        # call function that makes call to outside api
        response = rest_call_to_another_other_api()
        # assert if response matches expected
        if td_message not in response:
            print('FAIL: Not able to find td ' + td_message)
            assert False
