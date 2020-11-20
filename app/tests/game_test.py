import unittest

from app.models.game import *
from app.models.player import *

class GameTest(unittest.TestCase):

    def setUp(self):
        self.player_1a = Player("Dick Turpin", "rock")
        self.player_2a = Player("Robin Hood", "scissors")
        self.game_1 = Game(self.player_1a, self.player_2a)

        self.player_1b = Player("Dick Turpin", "scissors")
        self.player_2b = Player("Robin Hood", "rock")
        self.game_2 = Game(self.player_1b, self.player_2b)


    def test_player_1_wins(self):
        # test rock beats scissors
        self.game_1.check_winner()
        self.assertEqual(True, self.game_1.check_winner())
    

    def test_player_1_loses(self):
        # test rock beats scissors
        self.game_2.check_winner()
        self.assertEqual(False, self.game_2.check_winner())