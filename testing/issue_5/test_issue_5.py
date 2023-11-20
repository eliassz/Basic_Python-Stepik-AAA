import unittest
from unittest.mock import MagicMock, patch

from issue_5 import what_is_year_now


@patch("issue_5.urllib.request.urlopen")
class TestWhatIsYearNow(unittest.TestCase):
    def mock_urlopen(self, mock_urlopen, return_value):
        mock_response = MagicMock()
        mock_response.read.return_value = return_value
        mock_urlopen.return_value.__enter__.return_value = mock_response

    def test_format_yyyy_mm_dd(self, mock_urlopen):
        self.mock_urlopen(mock_urlopen, '{"currentDateTime": "2023-11-09"}')
        self.assertEqual(what_is_year_now(), 2023)

    def test_format_dd_mm_yyyy(self, mock_urlopen):
        self.mock_urlopen(mock_urlopen, '{"currentDateTime": "09.11.2023"}')
        self.assertEqual(what_is_year_now(), 2023)

    def test_invalid_format(self, mock_urlopen):
        self.mock_urlopen(mock_urlopen, '{"currentDateTime": "2023/11/09"}')
        with self.assertRaises(ValueError):
            what_is_year_now()


if __name__ == "__main__":
    unittest.main()
