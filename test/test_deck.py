"""
Testing the functionality of the Deck class.
Include getter/setters
"""

from src.deck import Deck
from src.card import Card
import unittest

class DeckTestCase(unittest.TestCase):
    def setUp(self):
        num_packs = 1
        self.deck = Deck(num_packs)
        pass
    
    def tearDown(self):
        pass

    def test_add_card(self):
        old_size = self.deck.get_num_cards()
        self.deck.add_card(Card("Ace", "Spades"))
        self.assertEqual(old_size+1, self.deck.get_num_cards())

    def test_num_cards(self):
        self.assertEqual(self.deck.get_num_cards(), 52)

    def test_num_cards_2packs(self):
        new_deck = Deck(2)
        self.assertEqual(new_deck.get_num_cards(), 52*2)

    def test_get_card(self):
        card_to_add = Card("Ace", "Hearts")
        self.deck.add_card(card_to_add)
        self.assertEqual(card_to_add, self.deck.get_card())

    def test_get_card_empty(self):
        with self.assertRaises(IndexError):
            self.deck.set_deck([]) # set the deck to be empty
            self.deck.get_card()

