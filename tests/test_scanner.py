import unittest
from scanner.tcp_scanner import scan_tcp_ports
from scanner.udp_scanner import scan_udp_ports

class TestPortScanner(unittest.TestCase):
    def test_tcp_scan_known_open(self):
        results = scan_tcp_ports("google.com", 80, 80)
        self.assertTrue(any("TCP Port 80 is open" in r for r in results))

    def test_tcp_scan_closed(self):
        results = scan_tcp_ports("google.com", 65432, 65432)
        self.assertFalse(any("TCP Port 65432 is open" in r for r in results))

    def test_udp_scan_ntp(self):
        results = scan_udp_ports("time.google.com", 123, 123)
        self.assertTrue(any("UDP Port 123 is open" in r for r in results))

if __name__ == "__main__":
    unittest.main()
