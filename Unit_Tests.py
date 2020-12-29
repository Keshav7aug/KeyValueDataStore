from Testt import *
import unittest
class TestKeyValueStore(unittest.TestCase):
    def test_create(self):
        self.assertEqual(create('a',2),"Key Created")
        self.assertEqual(create('abc',2,2),"Key Created")
        self.assertEqual(create('new_key','abcdef'),"Key Created")
        self.assertEqual(create(['123'],7),"Key is not a string")
        self.assertEqual(create('abcdefghijklmnopqrstuvwxyzqwertyu',7),
        "Size of key string is greater than 32")
    def test_read(self):
        time.sleep(2)
        self.assertEqual(read('abc'),"Time to LIVE is Over")
        self.assertEqual(read('a'),2)
        self.assertEqual(read('kljn'),"Key does not Exist")
    def test_delete(self):
        self.assertEqual(delete('aa'),"Key does not Exist")
        self.assertEqual(delete('new_key'),"Key-Value pair Deleted")
unittest.main()