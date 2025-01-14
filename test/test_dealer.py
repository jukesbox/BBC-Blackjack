
from src.player import Player, Dealer
from src.deck import Deck
from src.card import Card
import unittest


class PlayerTestCase(unittest.TestCase):
    def setUp(self):
        self.dealer = Dealer()
        self.deck = Deck(1)
        pass
    
    def tearDown(self):
        pass


    def test_dealer_opening_hand(self):
        """
        Given the dealer is dealt an opening hand,
        When the dealer's hand is revealed,
        Then only one card is shown.
        """
        self.dealer.opening_hand(self.deck)
        self.assertEqual(len(self.dealer.get_partial_hand()), 1)

    def test_dealer_get_partial_hand(self):
        """
        Given the dealer has been dealt cards,
        When the dealer's partial hand is requested,
        Then the partial hand contains only the first card dealt.
        """
        self.dealer.opening_hand(self.deck)
        self.assertEqual(self.dealer.get_partial_hand()[0], self.dealer.get_hand()[0])

    def test_dealer_take_turn(self):
        """
        Given the dealer's hand total is less than 17,
        When the dealer takes a turn,
        Then the dealer hits until the hand total is at least 17.
        """
        self.dealer.set_hand([Card("2", "Hearts"), Card("3", "Diamonds")])
        self.dealer.take_turn(self.deck)
        self.assertGreaterEqual(self.dealer.get_hand_total(), 17)

    def test_dealer_stand(self):
        """
        Given the dealer's hand total is 17 or more,
        When the dealer takes a turn,
        Then the dealer stands and does not take any more cards.
        """
        self.dealer.set_hand([Card("10", "Hearts"), Card("7", "Diamonds")])
        self.dealer.take_turn(self.deck)
        self.assertEqual(self.dealer.get_hand_total(), 17)
        num_cards = self.dealer.get_num_cards()
        self.dealer.take_turn(self.deck)
        self.assertEqual(self.dealer.get_num_cards(), num_cards)