import tracker
import unittest
import json
from unittest.mock import Mock, patch


def load_file():
    with open("test_applications.json", "r") as file:
        return json.load(file)


class TestTracker(unittest.TestCase):   

    def test_get_interviews(self):
        applications = load_file()

        self.assertEqual(
            tracker.get_interviews(applications),
            ["OpenAI", "Amazon"]
        )
    def test_no_interviews(self):
        applications = [
        {"company": "Google", "status": "rejected"},
        {"company": "Meta", "status": "applied"},
        ]
        self.assertEqual(
            tracker.get_interviews(applications),
            []
        )
    def test_empty_list(self):
        applications = []
        self.assertEqual(tracker.get_interviews(applications),
            []
        )
    def test_find_applications(self):
        applications = [
            {"company": "Google", "role": "SWE", "status": "rejected"},
            {"company": "OpenAI", "role": "ML Engineer", "status": "interview"},
            {"company": "Google", "role": "Data Analyst", "status": "applied"},
        ]
        self.assertEqual(tracker.find_applications(applications, "Google"),
            [{"company": "Google", "role": "SWE", "status": "rejected"},
            {"company": "Google", "role": "Data Analyst", "status": "applied"}]
        )

    def test_find_empty_apps(self):
        applications = []
        self.assertEqual(tracker.find_applications(applications, "Google"),
            []
        )
    @patch("tracker.get_users")
    def test_get_usernames(self, mock_get_users):
        mock_get_users.return_value = [
        {"name": "Alice"},
        {"name": "Bob"}
        ]
        
        self.assertEqual(
        tracker.get_user_name(),
        ["Alice", "Bob"]
        )
        mock_get_users.assert_called_once()
        


if __name__ == "__main__":
    unittest.main()