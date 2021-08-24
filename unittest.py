from unittest import TestCase
from promtest import get_response


class TestUpTimeCheck(TestCase):

    up_url = "https://httpstat.us/200"
    down_url = "https://httpstat.us/503"

    def assert_response_time(self, response_time):
        self.assertGreater(response_time, 0, "Response time should be greater than 0.")
        self.assertLess(response_time, 10000, "Response time should be less than 10,000")

    def test_get_response(self):
        status, response_time  = get_response(self.up_url)
        self.assertEqual(status, 1, "get_response() should return status 1 when URL is up.")
        self.assert_response_time(response_time)
        status, response_time  = get_response(self.down_url)
        self.assertEqual(status, 0, "get_response() should return status 0 when URL is down.")
        self.assert_response_time(response_time)
