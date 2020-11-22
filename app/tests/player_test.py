import unittest
from app.models.player import *

class TestPlayert(unittest.TestCase):
    def setUp(self):
        self.player = Player("Dick Turpin", "rock")

    
    def test_player_has_name(self):
        self.assertEqual("Dick Turpin", self.player.name)

    
    def test_player_has_hand(self):
        self.assertEqual("rock", self.player.hand)
