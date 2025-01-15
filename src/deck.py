"""
This file contains the Deck class, which holds the cards that can be dealt to the players.

"""
from collections import deque
from src.card import Card
from random import shuffle
SUITS = ["Diamonds", "Clubs", "Spades", "Hearts"]
RANKS = ["Ace", "2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King"]

class Deck:
    def __init__(self, packs):
        # used a deque instead of implementing stack etc - for quick LIFO access
        self._card_stack = deque()
        self._num_packs = packs
        # add cards to deck
        self.create_deck()
        pass

    def add_card(self, card):
        """
        Adds a card to the deck

        Args:
            card (Card object): A single card to add to the deck
        """
        self._card_stack.append(card)


    def get_card(self):
        """
        Returns a card if the stack is not empty

        Raises:
            IndexError: If the deck is empty

        Returns:
            Card object: A card
        """
        if int(self.get_num_cards()) < 1:
            raise IndexError("Deck is empty - no more cards to draw")
        else:
            return self._card_stack.pop()

    def shuffle_cards(self, cards):
        """
        Shuffles the cards in place and returns the list of cards
        """
        shuffle(cards)
        return cards

    def create_card_list(self):
        """
        Create a card object for all 52 cards, multiplied by the number of packs

        Returns:
            [Card]: a list of all card objects to be added to the stack
        """
        all_cards = []
        for _ in range(self._num_packs):
            for suit in SUITS:
                for rank in RANKS:
                    all_cards.append(Card(rank, suit))
        return all_cards

    def create_deck(self, cards_to_add=None):
        """
        Creates a new deck - clearing any existing cards

        Args:
            cards_to_add (cards_to_add, optional): Specific cards. Defaults to None.
        """
        # clear any current deck items.
        self._card_stack.clear()
        if cards_to_add == None:
            # this will happen most of the time!!
            cards_to_add = self.create_card_list()
        for card in self.shuffle_cards(cards_to_add):
            self.add_card(card)

    def set_deck(self, card_list):
        """
        Clears the stack and creates a new deck with the passed cards

        Args:
            card_list (Card object): A list of cards
        """
        self._card_stack.clear()
        self.create_deck(card_list)
        

    def get_num_cards(self):
        """
        Returns:
            int: the current size of the deck
        """
        return len(self._card_stack)

