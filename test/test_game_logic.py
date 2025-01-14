"""
Testing the functionality of the GameLogic class.
Include getter/setters
"""

from src.game_logic import GameLogic
from src.player import Player, Dealer
from src.card import Card
import unittest
from unittest.mock import patch

class GameLogicTestCase(unittest.TestCase):
    def setUp(self):
        self.setup_players = [Player("Jamie", 10), Player("Software Developer", 20)]
        self._game = GameLogic(self.setup_players, 2)
        pass
    
    def tearDown(self):
        pass

    def test_first_player_first(self):
        """
        Given the game is instantiated, before any other actions are performed,
        the current player is the player at index zero.
        """
        self.assertEqual(self.setup_players[0], self._game.get_current_player())

    def opening_hands(self):
        """
        Deals the opening hand to every player, and to the dealer.
        """
        for player in self._game.get_players():
            self.assertEqual(player.get_num_cards(), 2)
        self.assertEqual(self._game.get_dealer.get_num_cards(), 2)

    
    def test_get_players(self):
        """
        The list of players in the game can be accessed.
        """
        players = self._game.get_players()
        for player in players:
            self.assertIsInstance(player, Player)
        self.assertEqual(self._game.get_players(), self.setup_players)
        

    def test_get_current_player(self):
        """
        The current player can be accessed
        """
        self._game.set_next_player()
        player = self._game.get_current_player()
        self.assertIsInstance(player, Player)
        self.assertEqual(player, self.setup_players[1])

    def test_set_next_player_valid(self):
        """
        Given the current player is not the last in the list, 
        the next player can be accessed.
        """
        self._game.set_next_player()
        self.assertEqual(self._game.get_current_player(), self.setup_players[1])

    def test_set_next_player_invalid(self):
        """
        If the current player is the last player, attempting
        to set the next player will raise an index error.
        """
        self._game.set_next_player()
        with self.assertRaises(IndexError):
            self._game.set_next_player()

    def test_is_done_true(self):
        """
        Given the current player is the last in the list, is_done() is True
        """
        self._game.set_next_player()
        self.assertEqual(self._game.is_done(), True)
    
    def test_test_is_done_false(self):
        """
        Given the current player is not the last in the list, is_done() is False
        """
        self.assertEqual(self._game.is_done(), False)
    
    def test_get_dealer(self):
        """
        Given the game is instantiated, the dealer can be accessed.
        """
        self.assertIsInstance(self._game.get_dealer(), Dealer)
    
    def test_get_dealer_revealed_ascii(self):
        """
        Gets the entire hand of the dealer (includes previously hidden card)
        """
        self._game.opening_hands()
        # 2 cards - 8 lines
        self.assertEqual(len(self._game.get_dealer_revealed_ascii()), 8)
    
    def test_get_dealer_full_hand_ascii(self):
        """
        Gets the entire hand of the dealer (includes previously hidden card)
        """
        self._game.opening_hands()
        # 2 cards - 8 lines
        self.assertEqual(len(self._game.get_dealer_full_hand_ascii()), 8)
    
    def test_get_dealer_total(self):
        """
        The dealer total is the sum of the values of the dealer's cards
        """
        self._game.opening_hands()
        hand = self._game.get_dealer().get_hand()
        total = 0
        for card in hand:
            total += card.get_card_value()
        self.assertEqual(self._game.get_dealer_total(), total)

    def test_take_dealer_turn_u17(self):
        """
        A card is added to the dealer's hand if their score is less than 17
        """
        # set to under 17
        total = self._game.get_dealer_total()
        self._game.take_dealer_turn()
        self.assertGreater(
            self._game.get_dealer_total(), total)
        

    def test_take_dealer_turn_17(self):
        """
        Given that the dealer's score is 17, they do not take another turn
        """
        # set to 17
        self._game.get_dealer().set_hand([Card("7", "Hearts"), Card("10", "Diamonds")])
        self._game.take_dealer_turn()
        self.assertEqual(
            self._game.get_dealer_total(), 17)
    
    def test_player_choice(self):
        """
        Perform the correct action on the Player's state based on the chosen action.

        Args:
            choice (str):  The choice (from 'hit', 'stand', 'double down') that the 
                            current player chose. 
        """
        pass
    
    def test_current_player_status_play(self):
        """
        Given the player has not ended their turn or gone bust, their current status is "PLAYING"
        """
        self.assertEqual("PLAYING", self._game.current_player_status())
        
    def test_current_player_status_stand(self):
        """
        Given the player has ended their turn (not bust), their current status is "STANDING"
        """
        self._game.on_stand()
        self.assertEqual("STANDING", self._game.current_player_status())

    def test_current_player_status_bust(self):
        """
        Given the player has ended their turn (not bust), their current status is "STANDING"
        """
        while self._game.get_current_player_total() <= 21:
            self._game.on_hit() # hit until bust
        self.assertEqual("BUST", self._game.current_player_status())
    
    def test_on_hit(self):
        """
        Add a new card to the current player's hand.
        """
        before_cards = self._game.get_current_player_total()
        self._game.on_hit()
        self.assertGreater(self._game.get_current_player_total(), before_cards)

    def test_on_hit_busts(self):
        """
        Add a new card to the current player's hand.
        """
        self._game.get_current_player().set_hand([Card("10", "Hearts"), 
                                                  Card("10", "Diamonds"), 
                                                  Card("Ace", "Spades")])
        before_cards = self._game.get_current_player_total()
        self._game.on_hit()
        self.assertGreater(self._game.get_current_player_total(), before_cards)
        self.assertEqual(self._game.get_turn_end(), True)
        

    def test_on_stand(self):
        """
        Sets the current player's _standing variable to True
        End the turn of the current player.
        """
        self._game.on_stand()
        self.assertEqual(self._game.get_turn_end(), True)

    def test_on_double_down(self):
        """
        Adds one more card to the player's hand, then stands
        Ends the turn of the current player.
        """
        before_cards = self._game.get_current_player_total()
        self._game.on_double_down()
        self.assertGreater(self._game.get_current_player_total(), before_cards)
        self.assertEqual(self._game.get_turn_end(), True)

    def test_set_turn_end(self):
        """
        Sets the current player's turn to ended
        """
        pass

