"""
Testing the functionality of the Player class.
Include getter/setters
"""

from src.player import Player
from src.deck import Deck
from src.card import Card
import unittest

class PlayerTestCase(unittest.TestCase):
    def setUp(self):
        self.player = Player()
        self.deck = Deck()
        pass
    
    def tearDown(self):
        pass


    def test_opening_hand(self):
        """
        * test case specified in candidate instructions *
        Given I play a game of blackjack
        When I am dealt my opening hand
        Then I have two cards
        """
        self.player.opening_hand()
        self.assertEqual(self.player.get_num_cards(), 2)

    def test_hit(self):
        """
        * test case specified in candidate instructions *
        Given I have a valid hand of cards
        When I choose to ‘hit’
        Then I receive another card
        And my score is updated
        """
        previous_total = self.player.get_hand_total()
        self.player.hit()
        self.assertGreater(self.player.get_hand_total(), previous_total)

    def test_stand(self):
        """
        * test case specified in candidate instructions *
        Given I have a valid hand of cards
        When I choose to ‘stand’
        Then I receive no further cards
        And my score is evaluated
        """
        previous_hand = self.get_hand()
        self.player.stand()
        self.assertEqual(previous_hand, self.player.get_hand())

    def test_double_down_bet(self):
        """
        Given my score is valid and I choose 
        to double down, my bet is doubled.
        """
        previous_bet = self.player.get_bet()
        self.player.double_down()
        self.assertEqual(previous_bet*2, self.player.get_bet())

    def test_double_down_cards(self):
        """
        Given my score is valid and I choose to 
        double down, I am given one additional card.
        """
        num_cards = self.player.get_num_cards()
        self.player.double_down()
        self.assertEqual(num_cards+1, self.player.get_num_cards())

        
    def test_double_down_finish(self):
        """
        Given my score is valid and I choose to double
        down, I cannot take another card after this.
        """    
        self.player.double_down()
        num_cards = self.player.get_num_cards()
        self.player.hit()
        self.assertEqual(num_cards, self.player.get_num_cards())


    def test_score_under_21(self):
        """
        * test case specified in candidate instructions *
        Given my score is updated or evaluated
        When it is 21 or less
        Then I have a valid hand
        """
        # score is automatically updated within this method
        self.player.set_hand([Card("King", "Diamonds"), 
                              Card("8", "Hearts")])
        self.assertEqual(self.player.is_bust(), True)
        

    def test_score_over_21(self):    
        """
        * test case specified in candidate instructions *
        Given my score is updated
        When it is 22 or more 
        Then I am ‘bust’ and do not have a valid hand
        """
        # score is automatically updated within this method
        self.player.set_hand([Card("King", "Diamonds"), 
                              Card("Queen", "Spades"),
                              Card("8", "Hearts")])
        self.assertEqual(self.player.is_bust(), True)
        
    def test_score_King_Ace(self):
        """
        * test case specified in candidate instructions *
        Given I have a king and an ace
        When my score is evaluated
        Then my score is 21
        """
        self.player.set_hand([Card("King", "Diamonds"), 
                              Card("Ace", "Spades")])
        self.assertEqual(self.player.get_hand_total(), 21)

        
    def test_score_K_Q_Ace(self):
        """
        * test case specified in candidate instructions *
        Given I have a king, a queen, and an ace
        When my score is evaluated
        Then my score is 21
        """
        self.player.set_hand([Card("King", "Diamonds"), 
                              Card("Queen", "Spades"), 
                              Card("Ace", "Hearts")])
        self.assertEqual(self.player.get_hand_total(), 21)


    def test_score_9_A_A(self):
        """
        * test case specified in candidate instructions *
        Given that I have a nine, an ace, and another ace
        When my score is evaluated
        Then my score is 21	
        """
        self.player.set_hand([Card("9", "Diamonds"), 
                              Card("Ace", "Spades"), 
                              Card("Ace", "Hearts")])
        self.assertEqual(self.player.get_hand_total(), 21)

    def test_turn_ended(self):
        """
        Given I have ended my turn,
        (doubled down/invalid hand/stood),
        any subsequent attempts to take a turn have 
        no effect.
        """
        self.player.stand()
        previous_cards = self.player.get_hand()
        self.player.hit()
        self.assertEqual(previous_cards, self.player.get_hand())