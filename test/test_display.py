"""
Testing the functionality of the Display class.
Include getter/setters
"""

from src.display import Display
import unittest

class DisplayTestCase(unittest.TestCase):
    def setUp(self):
        pass
    
    def tearDown(self):
        pass

    def test_get_entered_num_players(self):
        """
        Given I enter a valid number of players, that number is returned.
        """
        pass

    def test_get_entered_players_invalid(self):
        """
        Given I enter invalid response(s), the accepted
        value is the first acceptable response that I enter.
        """
        pass

    def test_get_entered_num_packs(self):
        """
        Given I enter a valid number of packs, that number is returned.
        """
        pass

    def test_get_entered_packs_invalid(self):
        """
        Given I enter invalid response(s), the accepted
        value is the first acceptable response that I enter.
        """
        pass

    def test_show_single_player_cards(self):
        """
        The player's cards can be shown in ascii art format.
        """
        pass

    def test_show_all_players_cards(self):
        """
        The cards of all players can be shown in ascii format.
        """
        pass

    def test_make_play_choice(self):
        """
        Given I enter 'h', 's' or 'd'...
        """
        pass

    def test_make_play_choice_invalid(self):
        """
        Given I enter invalid response(s), the accepted
        value is the first acceptable response that I enter.
        """
        pass