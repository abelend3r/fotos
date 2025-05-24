import unittest
from unittest.mock import patch, MagicMock
import google.generativeai # Required for the patch decorator to work correctly
from agent import TimeAgent

class TestTimeAgent(unittest.TestCase):

    def setUp(self):
        self.agent = TimeAgent(api_key="test_key")

    @patch('google.generativeai.GenerativeModel.generate_content')
    def test_get_local_time_success(self, mock_generate_content):
        # Configure the mock to return an object with a 'text' attribute
        mock_response = MagicMock()
        mock_response.text = "The local time in Paris is 2:00 PM"
        mock_generate_content.return_value = mock_response

        response = self.agent.get_local_time("Paris")
        self.assertEqual(response, "The local time in Paris is 2:00 PM")
        mock_generate_content.assert_called_once_with("What is the current local time in Paris?")

    @patch('google.generativeai.GenerativeModel.generate_content')
    def test_get_local_time_api_error(self, mock_generate_content):
        # Configure the mock to raise an exception
        mock_generate_content.side_effect = Exception("Simulated API Error")

        response = self.agent.get_local_time("UnknownVille")
        self.assertEqual(response, "Error: Could not retrieve time from API.")
        mock_generate_content.assert_called_once_with("What is the current local time in UnknownVille?")

    @patch('google.generativeai.GenerativeModel.generate_content')
    def test_get_local_time_fictional_city(self, mock_generate_content):
        # Configure the mock for a fictional city response
        mock_response = MagicMock()
        mock_response.text = "Sorry, I cannot find the time for FictionalCity."
        mock_generate_content.return_value = mock_response

        response = self.agent.get_local_time("FictionalCity")
        self.assertEqual(response, "Sorry, I cannot find the time for FictionalCity.")
        mock_generate_content.assert_called_once_with("What is the current local time in FictionalCity?")

if __name__ == '__main__':
    unittest.main()
