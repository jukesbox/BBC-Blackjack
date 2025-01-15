"""
This class holds the property of a card, including its suit, value, rank, name and image to display.
"""
from src.card_images import CardImages
from colorama import Fore, Back 

# suits and ranks to ensure all cards are accounted for
SUITS = ["Diamonds", "Clubs", "Spades", "Hearts"]
RANKS = ["Ace", "2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King"]
# the appropriate colours for different cards to be printed as...
# to be added to the front/back of every card's line
RED_SUIT = Fore.RED + Back.WHITE
BLACK_SUIT = Fore.BLACK + Back.WHITE 
DEFAULT = Fore.WHITE + Back.BLACK
# instance of CardImages - to take values from the dictionaries
ascii_art = CardImages()

class Card:
    def __init__(self, rank, suit):
        """Create card instance
        raises error if incorrent rank/suit given

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
        self._colour = None
        # set colour depending on suit
        if self._suit in ["Hearts", "Diamonds"]:
            self._colour = RED_SUIT
        else:
            self._colour = BLACK_SUIT
    
    def set_name(self):
        """
        Sets the name of the card according to the rank and suit 
        """
        self._name = self._rank + " of " + self._suit

    def set_ascii_art(self):
        """
        Gets the relevant ASCII art for the card
        """
        self._ascii_art = ascii_art.get_image_by_name(self._rank + "_of_" + self._suit)
        self._partial_ascii_art = ascii_art.get_partial_image_by_name(self._rank + "_of_" + self._suit)


    def get_ascii_art_colourised(self):
        """
        for each line, add the relevant colour to it
        (return to default colour at the end of the line)
        """
        new_lines = []
        for line in self._ascii_art:
            new_lines.append(self._colour + line + DEFAULT)
        return new_lines
    
    def get_ascii_partial_colourised(self):
        """
        for each line, add the relevant colour to it
        (return to default colour at the end of the line)
        """
        new_lines = []
        for line in self._partial_ascii_art:
            new_lines.append(self._colour + line + DEFAULT)
        return new_lines

    def get_name(self):
        """
        Returns:
            str: The name of the card e.g. ("Ace of Spades")
        """
        return self._name
    
    def get_rank(self):
        """
        Returns:
            str: The rank of the card e.g. ("King")
        """
        return self._rank

    def get_suit(self):
        """
        Returns:
            str: The suit of the card e.g. ("Spades")
        """
        return self._suit

    def get_ascii_art(self):
        """
        Returns:
            [str]: list of art lines
        """
        if self._ascii_art:
            return self._ascii_art
        return None
    
    def get_colour(self):
        """
        Returns:
            str: colour code to be printed to terminal
        """
        return self._colour
    
    def get_partial_ascii_art(self):
        """
        Returns:
            [str]: list of art lines
        """
        if self._partial_ascii_art:
            return self._partial_ascii_art
        return None
    
    def get_card_value(self):
        """Returns the value of the card - 10 for face cards, 
        11 for Ace, the number on the card otherwise

        Returns:
            int: the card value
        """
        if self._rank in ["Jack", "Queen", "King"]:
            return 10
        elif self._rank == "Ace":
            return 11
        else:
            return int(self._rank)
        
    def get_card_filename(self):
        """
        Returns:
            str: filename of card (for tkniter implementation)
        """
        return self._rank + "_of_Hearts.png"
        




    