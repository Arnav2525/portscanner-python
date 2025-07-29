import unittest
from unittest.mock import patch, MagicMock

# Import the function
from scanner.mongo_writer import save_scan_result

class TestMongoWriter(unittest.TestCase):
    @patch("scanner.mongo_writer.MongoClient")
    def test_save_scan_result(self, mock_client_class):
        # Setup mock MongoClient
        mock_client = MagicMock()
        mock_db = MagicMock()
        mock_collection = MagicMock()

        mock_client_class.return_value = mock_client
        mock_client.__getitem__.return_value = mock_db
        mock_db.__getitem__.return_value = mock_collection

        # Sample input
        ip = "192.168.1.100"
        open_ports = [{"port": 80, "protocol": "tcp", "service": "HTTP"}]

        # Run function
        save_scan_result(ip, open_ports)

        # Assertions
        mock_collection.update_one.assert_called_once_with(
            {"ip": ip},
            {"$set": {"open_ports": open_ports}},
            upsert=True
        )

if __name__ == "__main__":
    unittest.main()
