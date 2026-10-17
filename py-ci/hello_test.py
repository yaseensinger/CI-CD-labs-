import unittest

from hello import say_hello

class TestHello(unittest.TestCase):
    def test_sayhello(self):
        self.assertEqual(say_hello(), "hello")