import unittest
from unittest.mock import MagicMock, patch
from neo4j import GraphDatabase

# Import the function from your actual file
from scanner.neo4j_reader import get_discovered_ips

class TestNeo4jReader(unittest.TestCase):
    @patch("scanner.neo4j_reader.GraphDatabase.driver")
    def test_get_discovered_ips(self, mock_driver):
        # Mock session and result
        mock_session = MagicMock()
        mock_result = [{"address": "192.168.0.1"}, {"address": "192.168.0.2"}]

        # Configure mocks
        mock_session.run.return_value = mock_result
        mock_driver.return_value.session.return_value.__enter__.return_value = mock_session

        # Run the function
        ips = get_discovered_ips()

        # Assert
        self.assertEqual(ips, ["192.168.0.1", "192.168.0.2"])
        mock_session.run.assert_called_once()

if __name__ == "__main__":
    unittest.main()
