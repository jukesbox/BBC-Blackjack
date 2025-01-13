"""
Testing the functionality of the GameLogic class.
Include getter/setters
"""

from src.game_logic import GameLogic
import unittest

class GameLogicTestCase(unittest.TestCase):
    def setUp(self):
        self._game = GameLogic()
        pass
    
    def tearDown(self):
        pass

    def test_start_game(self):
        """
        Given all settings have been established, each player and the dealer can be given their opening hand.
        """
        pass

    def test_get_winners(self):
        """
        Given the game has finished, the winners should be 
        correctly identified and returned in a list
        """
        pass

    