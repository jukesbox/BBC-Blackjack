"""
Testing the functionality of the Display class.

There are several points where blank input has to be mocked (for where pauses are in the program)
I couldn't really find a way around that unfortuately!
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

    def test_show_player_name(self):
        """
        The player's name can be shown.
        """
        with patch.object(self.display._game, 'get_current_player_name', return_value="Player1"):
            name = self.display.show_player_name()
            self.assertEqual(name, "Name: Player1")

    @patch("src.display.input", return_value="")
    def test_pause(self, mock_input):
        """
        The pause function should wait for user input.
        """
        self.display.pause()
        mock_input.assert_called_once()

    @patch("src.display.input", return_value="3")
    def test_get_number_input_valid(self, mock_input):
        """
        Given I enter a valid number within the range, that number is returned.
        """
        number = self.display.get_number_input("Enter a number between 1 and 5:", 1, 5)
        self.assertEqual(number, 3)

    @patch("src.display.input", side_effect=["10", "0", "3"])
    def test_get_number_input_invalid(self, mock_inputs):
        """
        Given I enter invalid response(s), the accepted value is the first acceptable response that I enter.
        """
        number = self.display.get_number_input("Enter a number between 1 and 5:", 1, 5)
        self.assertEqual(number, 3)

    def test_show_player_score(self):
        """
        The player's score can be shown.
        """
        with patch.object(self.display._game, 'get_current_player_total', return_value=21):
            score = self.display.show_player_score()
            self.assertEqual(score, "Score: 21")

    def test_show_player_bet(self):
        """
        The player's bet can be shown.
        """
        with patch.object(self.display._game, 'get_current_player_bet', return_value=50):
            bet = self.display.show_player_bet()
            self.assertEqual(bet, "Bet: 50")

    def test_show_player_status(self):
        """
        The player's status can be shown.
        """
        with patch.object(self.display._game, 'current_player_status', return_value="PLAYING"):
            status = self.display.show_player_status()
            self.assertEqual(status, "******STATUS: PLAYING ******")

    def test_show_current_player_cards(self):
        """
        The player's cards can be shown in ascii art format.
        """
        with patch.object(self.display._game, 'get_current_player_ascii', 
                          return_value=[" ______________ ",
                                        "|2♠|3♠         |",
                                        "|  |     ♠     |",
                                        "|  |           |",
                                        "|  |     ♠     |",
                                        "|  |           |",
                                        "|  |     ♠     |",
                                        "|__|_________3♠|"]):
            cards = self.display.show_current_player_cards()
            self.assertEqual(cards, " ______________ \n|2♠|3♠         |\n|  |     ♠     |\n|  |           |\n|  |     ♠     |\n|  |           |\n|  |     ♠     |\n|__|_________3♠|")