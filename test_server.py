from server import dict_to_bytes, bytes_to_dict
import unittest

message = {
    'action': 'presence',
    'user': 'gSom'
}

bmessage = dict_to_bytes(message)


class TestDictToBytes(unittest.TestCase):

    def test_dict_to_bytes(self):
        self.assertEqual(type(dict_to_bytes(message)), bytes)

class TestBytesToDict(unittest.TestCase):

    def test_bytes_to_dict(self):
        self.assertEqual(type(bytes_to_dict(bmessage)), dict)

if __name__ == '__main__':
    unittest.main()