"""
The Player and Dealer class will be defined in this file.
The Dealer is a subclass of Player, as it shares some functionality but has additional restrictions (such as having a minimum hand value)

"""

class Player:
    def __init__(self, name, bet):
        self._name = name
        self._bet = bet
        self._hand = []
        self._standing = False
    
    def set_hand(self, hand):
        pass
    
    def opening_hand(self):
        pass

    def get_num_cards(self):
        pass

    def get_name(self):
        pass

    def get_hand(self):
        pass

    def get_hand_total(self):
        pass

    def get_bet(self):
        pass

    def is_bust(self):
        pass

    def hit(self):
        pass

    def stand(self):
        pass

    def double_down(Self):
        pass






class Dealer(Player):
    def __init__(self):
        super().__init__(self)