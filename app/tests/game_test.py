import unittest

from app.models.game import *
from app.models.player import *

class GameTest(unittest.TestCase):

    def setUp(self):
        self.player_1_rock = Player("Dick Turpin", "rock")
        self.player_1_scissors = Player("Dick Turpin", "scissors")
        self.player_1_paper = Player("Dick Turpin", "paper")
        self.player_2_rock = Player("Robin Hood", "rock")
        self.player_2_scissors = Player("Robin Hood", "scissors")
        self.player_2_paper = Player("Robin Hood", "paper")

        # rock draws with rock
        self.game_rr = Game(self.player_1_rock, self.player_2_rock)

        # scissors draws with rock
        self.game_ss = Game(self.player_1_scissors, self.player_2_scissors)

        # paper draws with paper
        self.game_pp = Game(self.player_1_paper, self.player_2_paper)

        # rock beats scissors
        self.game_rs = Game(self.player_1_rock, self.player_2_scissors)
        self.game_sr = Game(self.player_1_scissors, self.player_2_rock)

        # scissors beats paper
        self.game_sp = Game(self.player_1_scissors, self.player_2_paper)
        self.game_ps = Game(self.player_1_paper, self.player_2_scissors)

        # paper beats rock
        self.game_pr = Game(self.player_1_paper, self.player_2_rock)
        self.game_rp = Game(self.player_1_rock, self.player_2_paper)


    # === Test draws ===

    def test_payer_1_draws_r(self):
        # both players have rock
        self.assertIsNone(self.game_rr.check_winner())

    def test_payer_1_draws_s(self):
        # both players have scissors
        self.assertIsNone(self.game_ss.check_winner())

    def test_payer_1_draws_p(self):
        # both players have paper
        self.assertIsNone(self.game_pp.check_winner())


    # === Test rock beats scissors ===

    def test_player_1_wins_rs(self):
        # test rock beats scissors
        self.assertEqual(True, self.game_rs.check_winner())
    
    def test_player_1_loses_sr(self):
        # test scissors loses to rock
        self.assertEqual(False, self.game_sr.check_winner())


    # === Test scissors beats paper ===

    def test_player_1_wins_sp(self):
        # test scissors beats paper
        self.assertEqual(True, self.game_sp.check_winner())

    def test_player_1_loses_ps(self):
        # test paper loses to scissors
        self.assertEqual(False, self.game_ps.check_winner())


    # === Test paper beats rock ===

    def test_player_1_wins_pr(self):
        # test paper beats rock
        self.assertEqual(True, self.game_pr.check_winner())
    

    def test_player_1_loses_rp(self):
        # test rock loses to paper
        self.assertEqual(False, self.game_rp.check_winner())


