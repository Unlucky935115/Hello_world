import unittest
from ip_validation import validate_ip

class TestValidateIP(unittest.TestCase):
    def test_valid_ipv4(self):
        self.assertEqual(validate_ip("192.168.1.1"), "Valid IPv4 address")
    
    def test_valid_ipv4_localhost(self):
        self.assertEqual(validate_ip("127.0.0.1"), "Valid IPv4 address")
    
    def test_valid_ipv6(self):
        self.assertEqual(validate_ip("2001:0db8:85a3:0000:0000:8a2e:0370:7334"), "Valid IPv6 address")
    
    def test_valid_ipv6_shortened(self):
        self.assertEqual(validate_ip("::1"), "Valid IPv6 address")
    
    def test_invalid_ip(self):
        self.assertEqual(validate_ip("999.999.999.999"), "Invalid IP address")
    
    def test_invalid_text(self):
        self.assertEqual(validate_ip("not an ip"), "Invalid IP address")
    
    def test_empty_string(self):
        self.assertEqual(validate_ip(""), "Invalid IP address")

if __name__ == '__main__':
    unittest.main()