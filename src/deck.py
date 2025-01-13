"""
This class will have the properties of the deck.
"""
from collections import deque
from src.card import Card
from random import shuffle
SUITS = ["Diamonds", "Clubs", "Spades", "Hearts"]
RANKS = ["Ace", "2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King"]

class Deck:
    def __init__(self, packs):
        self._card_stack = deque()
        self._num_packs = packs
        self.create_deck()
        pass

    def add_card(self, card):
        self._card_stack.append(card)


    def get_card(self):
        if int(self.get_num_cards()) < 1:
            raise IndexError("Deck is empty - no more cards to draw")
        else:
            return self._card_stack.pop()

    def shuffle_cards(self, cards):
        shuffle(cards)
        return cards

    def create_card_list(self):
        all_cards = []
        for i in range(self._num_packs):
            for suit in SUITS:
                for rank in RANKS:
                    all_cards.append(Card(rank, suit))
        return all_cards

    def create_deck(self, cards_to_add=None):
        if cards_to_add == None:
            cards_to_add = self.create_card_list()
        for card in self.shuffle_cards(cards_to_add):
            self.add_card(card)

    def set_deck(self, card_list):
        self._card_stack.clear()
        self.create_deck(card_list)
        

    def get_num_cards(self):
        return len(self._card_stack)

