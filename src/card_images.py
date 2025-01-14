"""
This class deals with the generation of ASCII art for displaying the cards in the terminal.

The class should generate a dictionary of cards and their ascii art implementations, to be accessed
by the Card class which will return the ASCII art to display it.

"""
PATH = "src/ascii_art/"
SUITS = ["Diamonds", "Clubs", "Spades", "Hearts"]
RANKS = ["Ace", "2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King"]
unicode_suit = {"Diamonds":u"\u2666", "Clubs":u"\u2663", "Spades":u"\u2660", "Hearts":u"\u2665"}

class CardImages:
    def __init__(self):
        self._cards_list = self.get_cards_from_file()
        self._aces_list = self.get_aces_from_file()
        self._card_dict = {}
        # partial stores just the first 3 chars of each line... 
        # so that cards can be shown as stacked!
        self._card_partial_dict= {}
        # add all the cards to the dicts
        self.get_all_cards()

    def get_card_dict(self):
        """
        returns _card_dict

        Returns:
            dictionary {str:[str]}: Dictionary of cards and their lines of art.
        """
        return self._card_dict
    
    def get_card_partial_dict(self):
        """
        returns _card_partial_dict

        Returns:
            dictionary {str:[str]}: Dictionary of cards and their partial lines of art.
        """
        return self._card_partial_dict

    def split_lines(self, lines):
        """
        Group the lines from the file into the full cards (8 lines per card)
        Returns a list of lists of lines (Strings)

        Args:
            lines ([str]): List of lines from file

        Returns:
            [[str]]: The list of card image strings
        """
        split_lines = []
        for x in range(0, len(lines), 8):
            split_lines.append(lines[x:x+8])
        return split_lines

    def get_cards_from_file(self):
        """
        Split the file of card representations into individual cards.
        A total of 12 cards (excludes the Ace card)

        Returns:
            [[str]]: The list of card image strings
        """
        with open(PATH + "suit_exc_ace.txt", "r", encoding="UTF-8") as cards:
            card_lines =  cards.readlines()

        return self.split_lines(card_lines)
        
    def get_aces_from_file(self):
        """
        Split the file of card representations into individual cards.
        A total of 4 cards (each Ace card)

        Returns:
            [[str]]: The list of card image strings
        """
        with open(PATH + "aces.txt", "r", encoding="UTF-8") as aces:
            ace_lines = aces.readlines()
        
        return self.split_lines(ace_lines)
    
    def get_all_cards(self):
        self.get_not_aces()
        self.get_aces()

    def get_not_aces(self):
        """
        Add all cards to the two dictionaries (excluding aces)
        Enumerates over suits and ranks to add all of them,
        with respect to the layout of the ascii art file.
        """
        index = 1 # don't include aces here... they're stored separately
        for lst in self._cards_list:
            for suit in SUITS:
                changed_lst = []
                partial_lst = []
                for line in lst:
                    # replace the card suit character with the correct suit
                    # (teh cards in the file are all spades)
                    new_line = line.strip("\n").replace(u"\u2660", unicode_suit[suit])
                    new_line.replace("\t", "    ")
                    changed_lst.append(new_line)
                    partial_lst.append(new_line[:3])
                
                self._card_dict[RANKS[index] + "_of_" + suit] = changed_lst
                self._card_partial_dict[RANKS[index] + "_of_" + suit] = partial_lst
            index += 1

    def get_aces(self):
        """
        Add all aces to the two dictionaries.
        Enumerates over suits to add all of them,
        with respect to the layout of the ascii art file.
        """
        for ace in self._aces_list:
            for suit in SUITS:
                changed_lst = []
                partial_lst = []
                for line in ace:
                    new_line = line.strip("\n").replace(u"\u2660", unicode_suit[suit])
                    changed_lst.append(new_line)
                    partial_lst.append(new_line[:3])
                
                self._card_dict["Ace_of_" + suit] = changed_lst
                self._card_partial_dict["Ace_of_" + suit] = partial_lst

    def get_image_by_name(self, card_name):
        """
        Gets the list of art lines for the card

        Args:
            card_name str: The name of the card to find

        Raises:
            ValueError: If card name is incorrect (not in self._card_dict)

        Returns:
           [str]: List of lines of card art for given card.
        """
        if card_name in self._card_dict:
            return self._card_dict[card_name]
        raise ValueError("Card name not in dictionary")

    def get_partial_image_by_name(self, card_name):
        """
        Gets the list of partial art lines for the card
        (the first three characters of each full line)

        Args:
            card_name str: The name of the card to find

        Raises:
            ValueError: If card name is incorrect (not in self._card_partial_dict)

        Returns:
           [str]: List of lines of partial card art for given card.
        """
        if card_name in self._card_partial_dict:
            return self._card_partial_dict[card_name]
        raise ValueError("Card name not in dictionary")
    