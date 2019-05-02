import unittest
from bacteria import screen , day ,t


class TestBacteria(unittest.TestCase):
    def test_screen(self):
        pass
        #self.assertTrue(screen)

    def test_day(self):
        day = 93, 155, 155
        self.assertEqual(screen, day)

    def test_energy(self):

        self.assertEqual(100, t)