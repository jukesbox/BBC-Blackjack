"""
This class will contain the main game logic, such as determining what happens when "hit" is entered.

The players, deck and dealer will be instantiated inside this class, as all game logic should be performed here.
"""
from src.deck import Deck
from src.player import Dealer

class GameLogic:
    def __init__(self, player_list, num_packs):
        self._players = player_list
        self._dealer = Dealer()
        self._deck = Deck(num_packs)
        self._num_players = len(self._players)
        self._current_player = 0
        self._game_done = False
        self.end_turn = False

    def opening_hands(self):
        """
        Deals the opening hand to every player, and to the dealer.
        """
        for player in self._players:
            player.opening_hand(self._deck)
        self._dealer.opening_hand(self._deck)

    
    def get_players(self):
        """
        Returns the list of players in the game

        Returns:
            [Player (object)]: List of players
        """
        return self._players

    def get_current_player(self):
        """
        Returns the current player object

        Returns:
            Player (object): Current player
        """
        return self._players[self._current_player]
    
    def get_current_player_total(self):
        """
        Returns the current score of the player

        Returns:
            int: The current score of the player
        """
        return self.get_current_player().get_hand_total()

    def set_next_player(self):
        """
        Increments the index of _current_player, to start the turn of the next player.

        Raises:
            IndexError: Raised if next player attempted when _current_player was the last 
                        one in the list
        """
        self.end_turn = False
        if not self.is_done():
            self._current_player += 1
            print(self._current_player)
            print(self._num_players)
        else:
            raise IndexError("Attempt to get next player when no more exist")

    def is_done(self):
        """
        Determines whether there are more players that have not taken their turn.
        Returns true if the current player is the final player in the list.

        Returns:
            bool: current player is the last player
        """
        return (self._current_player+1 >= self._num_players)
    
    def get_dealer(self):
        """Gets the instantiated Dealer

        Returns:
            Dealer (object): the dealer in this game
        """
        return self._dealer
    
    def get_dealer_revealed_ascii(self):
        """
        Gets the revealed hand of the dealer (excludes one card at the beginning)

        Returns: [str]: list of ASCII art lines.
            
        """
        return self._dealer.show_revealed_hand()
    
    def get_dealer_full_hand_ascii(self):
        """
        Gets the entire hand of the dealer (includes previously hidden card)

        Returns: [str]: list of ASCII art lines.
            
        """
        return self._dealer.get_hand_ascii()
    
    def get_dealer_total(self):
        """
        Gets the current score of the dealer

        Returns:
            int: the dealer's score (hand total)
        """
        return self._dealer.get_hand_total()

    def take_dealer_turn(self):
        """
        A card is added to the dealer's hand if their score is less than 17
        """
        self._dealer.take_turn(self._deck)

    def game_done(self):
        """
        Whether the dealer's hand has reached the required hand total.

        Returns:
            bool: The dealer has finished drawing cards.
        """
        self._game_is_done =  (self._dealer.get_hand_total() > 16)
        return self._game_is_done

    
    def player_choice(self, choice):
        """
        Perform the correct action on the Player's state based on the chosen action.

        Args:
            choice (str):  The choice (from 'hit', 'stand', 'double down') that the 
                            current player chose. 
        """
        if choice == "h":
            self.on_hit()
        elif choice == "s":
            self.on_stand()
        else:
            self.on_double_down()
    
    def current_player_status(self):
        """
        Returns the status of the current player, depending on the 
        hand_total/whether they have chosen to stand

        Returns:
            str: one of: "BUST", "STANDING", "PLAYING"
        """
        if self.get_current_player().get_hand_total() > 21:
            return "BUST"
        elif self.get_current_player().is_standing():
            return "STANDING"
        return "PLAYING"
    

    def get_current_player_name(self):
        """
        Returns:
            str: the current player's name
        """
        return self.get_current_player().get_name()

    def get_current_player_total(self):
        """
        Returns:
            int: the current player's hand total
        """
        return self.get_current_player().get_hand_total()

    def get_current_player_bet(self):
        """
        Returns:
            int: the current player's  bet
        """
        return self.get_current_player().get_bet()
    
    def get_current_player_ascii(self):
        """
        Returns:
            [str]: the current player's hand in ascii art format.
        """
        return self.get_current_player().get_hand_ascii()
        
    
    # the display should never interact directly with the player instances,
    # all behaviour is managed through here
    # this ensures separation of concerns for if an additional 'frontend' 
    # implementation was added.
    def on_hit(self):
        """
        Add a new card to the current player's hand
        Ends the turn of the current player if they are bust.
        """
        self.get_current_player().hit(self._deck)
        if self.get_current_player().is_bust():
            self.set_turn_end()

    def on_stand(self):
        """
        Sets the current player's _standing variable to True
        End the turn of the current player.
        """
        self.get_current_player().stand()
        self.set_turn_end()

    def on_double_down(self):
        """
        Adds one more card to the player's hand, then stands
        Ends the turn of the current player.
        """
        self.get_current_player().double_down(self._deck)
        self.set_turn_end()

    def is_bust_dealer(self):
        """
        Returns True if dealer score > 21, else returns False
        """
        return self._dealer.is_bust()

    def set_turn_end(self):
        """
        Sets the current player's turn to ended
        """
        self.end_turn = True


    def get_turn_end(self):
        """
        Gets whether the current player's turn has ended
        """
        return self.end_turn

