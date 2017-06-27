import unittest
from start import Song


class TestMusicPlayer(unittest.TestCase):
    def setUp(self):
        self.song = Song("Odin", "Manowar", "The Sons of Odin", "3:44")

    def test_str(self):
        self.assertEqual(str(self.song),
                         "Manowar - Odin from The Sons of Odin - 3:44")

if __name__ == '__main__':
    unittest.main()
