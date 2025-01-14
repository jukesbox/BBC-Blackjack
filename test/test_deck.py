"""
Testing the functionality of the Deck class.
Include getter/setters
"""

from src.deck import Deck
from src.card import Card
import unittest

SUITS = ["Diamonds", "Clubs", "Spades", "Hearts"]
RANKS = ["Ace", "2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King"]

class DeckTestCase(unittest.TestCase):
    def setUp(self):
        num_packs = 1
        self.deck = Deck(num_packs)
        pass
    
    def tearDown(self):
        pass

    def test_add_card(self):
        """
        Given a card is added to the deck, 
        the size of the deck increases by one
        """
        old_size = self.deck.get_num_cards()
        self.deck.add_card(Card("Ace", "Spades"))
        self.assertEqual(old_size+1, self.deck.get_num_cards())

    def test_num_cards(self):
        """
        Given only one pack of cards is used in the deck,
        there are 52 cards before removing from the stack.
        """
        self.assertEqual(self.deck.get_num_cards(), 52)

    def test_num_cards_2packs(self):
        """
        Given two packs of cards are used in the 
        deck, there are 104 cards before any are removed.
        """
        new_deck = Deck(2)
        self.assertEqual(new_deck.get_num_cards(), 52*2)

    def test_get_card(self):
        """
        The last card to be added to the stack is returned when a card 
        is requested.
        """
        card_to_add = Card("Ace", "Hearts")
        self.deck.add_card(card_to_add)
        self.assertEqual(card_to_add, self.deck.get_card())

    def test_get_card_empty(self):
        """
        If a card is requested from the deck but there are no 
        cards left, must raise an IndexError
        """
        with self.assertRaises(IndexError):
            self.deck.set_deck([]) # set the deck to be empty
            self.deck.get_card()

    def test_shuffle_cards(self):
        """
        Given a list of cards, the shuffle_cards method should return
        a list of the same cards but in a different order.
        """
        cards = [Card(rank, suit) for suit in SUITS for rank in RANKS]
        shuffled_cards = self.deck.shuffle_cards(cards.copy())
        self.assertNotEqual(cards, shuffled_cards)
        self.assertCountEqual(cards, shuffled_cards)

    def test_set_deck(self):
        """
        Given a list of cards, the set_deck method should replace the current
        deck with the new list of cards.
        """
        new_cards = [Card("Ace", "Spades"), Card("King", "Hearts")]
        self.deck.set_deck(new_cards)
        self.assertEqual(self.deck.get_num_cards(), len(new_cards))
        self.assertEqual(self.deck.get_card(), new_cards[-1])
        self.assertEqual(self.deck.get_card(), new_cards[-2])

    def test_create_card_list(self):
        """
        The create_card_list method should return a list of 52 cards for one pack.
        """
        cards = self.deck.create_card_list()
        self.assertEqual(len(cards), 52)
        self.assertTrue(all(isinstance(card, Card) for card in cards))

    def test_create_deck_with_custom_cards(self):
        """
        Given a custom list of cards, the create_deck method should initialize
        the deck with those cards.
        This shouldn't be used, but allows for added implementation later.
        """
        custom_cards = [Card("Ace", "Spades"), Card("King", "Hearts")]
        self.deck.create_deck(custom_cards)
        self.assertEqual(self.deck.get_num_cards(), len(custom_cards))
        self.assertEqual(self.deck.get_card(), custom_cards[-1])
        self.assertEqual(self.deck.get_card(), custom_cards[-2])


