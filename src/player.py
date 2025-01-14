"""
The Player and Dealer class will be defined in this file.
The Dealer is a subclass of Player, as it shares some functionality but has additional restrictions (such as having a minimum hand value)

"""
from colorama import Fore, Back
DEFAULT_COLOUR = Fore.WHITE + Back.BLACK

class Player:
    def __init__(self, name, bet):
        self._name = name
        self._bet = int(bet)
        self._hand = []
        self._hand_total = 0
        self._standing = False
    
    def is_standing(self):
        return self._standing


    def set_hand(self, hand):
        self._hand = hand
    
    def opening_hand(self, deck):
        self.hit(deck)
        self.hit(deck)

    def get_num_cards(self):
        return len(self._hand)

    def get_name(self):
        return self._name

    def get_hand(self):
        return self._hand

    def get_hand_total(self):
        hand_of_cards = self._hand
        hand_total = 0
        ace_count = 0
        for card in hand_of_cards:
            # aces must be differentiated, as they are treated differently when counted
            if card.get_rank() == "Ace":
                ace_count += 1
            else:
                hand_total += card.get_card_value()
        
        ## for each ace, let their total be 10, unless that will
        while ace_count > 0:
            ace_count -= 1
            # this accounts for if there are more aces that would cause a bust if added after the currently
            # calculating card
            if hand_total <= 10 - ace_count:
                hand_total += 11
            else:
                hand_total += 1
        self._hand_total = hand_total
        return self._hand_total
    
    def get_hand_ascii(self):
        # for all but one card, get the ascii representation
        ascii_by_card = []
        for x in range(self.get_num_cards() - 1):
            ascii_by_card.append(self._hand[x].get_ascii_partial_colourised())
        ascii_by_card.append(self._hand[self.get_num_cards() - 1].get_ascii_art_colourised())
        # ascii_by_card contains each individual card's ascii art
        # rearrange to be by line...
        all_lines = []
        for y in range(8):
            this_line = ""
            for card in ascii_by_card:
                this_line += card[y]
            all_lines.append(this_line)
        return all_lines



    def get_bet(self):
        return self._bet

    def is_bust(self):
        if self.get_hand_total() > 21:
            return True
        return False

    def hit(self, deck):
        if not self._standing:
            self._hand.append(deck.get_card())

    def stand(self):
        self._standing = True

    def double_down(self, deck):
        self.hit(deck)
        self.double_bet()
        self.stand()

    def double_bet(self):
        self._bet *= 2

    def player_wins(self, dealer_score):
        if not self.is_bust():
            if self._hand_total > dealer_score:
                return True
        return False






class Dealer(Player):
    def __init__(self):
        super().__init__("Dealer", 0)
        self._revealed_hand = []

    def opening_hand(self, deck):
        super().opening_hand(deck)
        self._revealed_hand.append(self._hand[0])

    def get_partial_hand(self):
        return self._revealed_hand
    
    def get_hand(self):
        return self._hand

    def show_revealed_hand(self):
        return self._revealed_hand[0].get_ascii_art_colourised()

    def take_turn(self, deck):
        if self.get_hand_total() < 17:
            self.hit(deck)