"""
Testing the functionality of the Display class.
Include getter/setters
"""

from src.display import Display
import unittest
from unittest.mock import patch

class DisplayTestCase(unittest.TestCase):
    # patch the input for initialisation of players/packs in the setup of Display
    @patch("src.display.input", side_effect=["", "1", "1", "Jamie", "10"])
    def setUp(self, mock_input):
        self.display = Display()
        pass
    
    def tearDown(self):
        pass

    @patch("src.display.input", side_effect=["1"])
    def test_get_entered_num_players(self, mock_input):
        """
        Given I enter a valid number of players, that number is returned.
        """
        num_players = self.display.get_entered_num_players()
        self.assertEqual(num_players, 1)

    @patch("src.display.input", side_effect=["-1", "0", "TotallyANumber", "8", "3"])
    def test_get_entered_players_invalid(self, mock_inputs):
        """
        Given I enter invalid response(s), the accepted
        value is the first acceptable response that I enter.
        """
        num_players = self.display.get_entered_num_players()
        # the first valid input is 3
        self.assertEqual(num_players, 3)

    @patch("src.display.input", return_value="Jamie J")
    def test_get_player_name(self, mock_input):
        """
        Given I enter a name when prompted, that name is returned
        """
        player_name = self.display.get_player_name(0)
        self.assertEqual(player_name, "Jamie J")

    @patch("src.display.input", return_value="")
    def test_get_player_name_empty(self, mock_input):
        """
        Given I do not enter anything for the player's name, it is set to "Player"
        """
        player_name = self.display.get_player_name(0)
        self.assertEqual(player_name, "Player")
        pass

    @patch("src.display.input", return_value="10")
    def test_get_player_bet(self, mock_input):
        """
        Given I enter a valid bet (a positive integer), that value is returned.
        """
        player_bet = self.display.get_player_bet("name")
        self.assertEqual(player_bet, 10)

    @patch("src.display.input", side_effect=["BBC", "0", "5"])
    def test_get_bet_invaid(self, mock_inputs):
        """
        Given I enter invalid response(s), the accepted
        value is the first acceptable response that I enter.
        """
        player_bet = self.display.get_player_bet("name")
        self.assertEqual(player_bet, 5)

    @patch("src.display.input", return_value="2")
    def test_get_entered_num_packs(self, mock_input):
        """
        Given I enter a valid number of packs, that number is returned.
        """
        num_packs = self.display.get_entered_num_packs()
        self.assertEqual(num_packs, 2)

    @patch("src.display.input", side_effect=["8", "0", "3"])
    def test_get_entered_packs_invalid(self, mock_inputs):
        """
        Given I enter invalid response(s), the accepted
        value is the first acceptable response that I enter.
        """
        num_packs = self.display.get_entered_num_packs()
        self.assertEqual(num_packs, 3)

    def test_show_current_player_cards(self):
        """
        The player's cards can be shown in ascii art format.
        """
        pass

    def test_show_all_players_cards(self):
        """
        The cards of all players can be shown in ascii format.
        """
        pass

    @patch("src.display.input", return_value="h")
    def test_make_play_choice(self, mock_input):
        """
        Given I enter 'h', 's' or 'd'...
        The choice that was made is returned
        """
        pass

    @patch("src.display.input", side_effect=["developer", " ", "s"])
    def test_make_play_choice_invalid(self, mock_inputs):
        """
        Given I enter invalid response(s), the accepted
        value is the first acceptable response that I enter.
        """
        pass