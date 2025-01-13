"""
This class will have the properties of each card, including its suit, value, rank and name to display.


Encapsulation is used throughout - mainly to avoid modification of instance variables
accidentally outside of the class.

"""
SUITS = ["Diamonds", "Clubs", "Spades", "Hearts"]
RANKS = ["Ace", "2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King"]

class Card:
    def __init__(self, rank, suit):
        """Initialisation of Card

        Args:
            rank (str): The rank (value on card) of the card
            suit (str): The suit that the card belongs to
        """
        if rank in RANKS:
            self._rank = str(rank) # should be passed as string, but incase int
        else:  
            raise ValueError("Given rank: " + str(rank) + " is invalid.")
        if suit in SUITS:
            self._suit = suit
        else:  
            raise ValueError("Given suit: " + str(suit) + " is invalid.")
        self._name = None
        self.set_name()
        self._ascii_art = None
        self.set_ascii_art()

    def __str__(self):
        return f"{self._rank} of {self._suit}"
    
    def set_name(self):
        """
        Sets the name of the card according to the rank and suit 
        """
        self._name = self._rank + " of " + self._suit

    ### TODO: once CardImages is implemented
    def set_ascii_art(self):
        pass

    def get_name(self):
        return self._name

    def get_suit(self):
        return self._suit

    def get_ascii_art(self):
        if self._ascii_art:
            return self._ascii_art
        return None
    
    def get_card_value(self):
        if self._rank in ["Jack", "Queen", "King"]:
            return 10
        elif self._rank == "Ace":
            return 11
        else:
            return int(self._rank)
        




    