"""
Testing the functionality of the Card class.
Include getter/setters
"""

from src.card import Card
import unittest

PATH = "src/images/"

class CardTestCase(unittest.TestCase):
    def setUp(self):
        # don't automatically set up an instance of Card() as some tests require
        # testing specific card types
        pass
    
    def tearDown(self):
        pass

    def test_invalid_rank(self):
        # 'A' should be 'Ace' to be valid
        with self.assertRaises(ValueError):
            self.card = Card("A", "Diamonds") 

    def test_invalid_suit(self):
        # 'Diamond' should be 'Diamonds' to be valid
        with self.assertRaises(ValueError):
            self.card = Card("Ace", "Diamond") 

    def test_set_name(self):
        """
        Given a card is instantiated, the correct rank and suit is used to make it's name.
        """
        self.card = Card("Ace", "Diamonds")
        # method is called in __init__, but reset it here
        self.card.set_name()
        self.assertEqual(self.card.get_name(), "Ace of Diamonds")

    def test_set_ascii_art(self):
        """
        Given a card is instantiated, ascii art fo rthat card can be set.
        """
        self.card = Card("Ace", "Spades")
        self.card.set_ascii_art()
        self.assertNotEqual(None, self.card.get_ascii_art())

    def test_get_name(self):
        """
        Given a card is instantiated, it has the correct name property
        """
        self.card = Card("4", "Hearts")
        self.assertEqual(self.card.get_name(), "4 of Hearts")
        pass

    def test_get_rank(self):
        """
        Given a card is instantiated, it has the correct name property
        """
        self.card = Card("4", "Hearts")
        self.assertEqual(self.card.get_rank(), "4")
        pass

    def test_get_suit(self):
        """
        Given a card is instantiated, it has the correct suit property.
        """
        self.card = Card("4", "Hearts")
        self.assertEqual(self.card.get_suit(), "Hearts")

    def test_get_ascii_art(self):
        ### TODO: Write test
        pass


    def test_get_card_value_num(self):
        """ For a number card, test that the points value of the card matches """
        this_card = Card("4", "Diamonds")
        self.assertEqual(this_card.get_card_value(), 4)

    def test_get_card_value_face(self):
        """ For a face card (K,Q,J) check that the points value of the card is 10 """
        this_card = Card("King", "Diamonds")
        self.assertEqual(this_card.get_card_value(), 10)

    def test_get_card_value_ace(self):
        """ For an ace card, check that the default points value is 11"""
        this_card = Card("Ace", "Diamonds")
        self.assertEqual(this_card.get_card_value(), 11)