"""
This class will contain all necessary functions for displaying the game logic to the terminal.

The main game logic is separated from this to ensure that additional implementations (such as a GUI) could be added
without refactoring the rest of the code.

"""
from src.game_logic import GameLogic
from src.player import Player

class Display:
    def __init__(self):
        self.display_text_art()
        self.pause()
        # player input for the number of players and packs to use
        self._num_players = self.get_entered_num_players()
        self._num_packs = self.get_entered_num_packs()
        # create list of player objects with corrent names/bets
        self._all_players = self.create_players()
        # create GameLogic instance with entered info
        self._game = GameLogic(self._all_players, self._num_packs)

    def get_game(self):
        """
        Returns:
            Game object: the game instance of the display
        """
        return self._game
    
    def begin_game(self):
        """
        This function plays the whole game. I wanted to split it up further, 
        however it seemed to make more logical sense this way.
        """
        # give players/dealer their opening hand
        self._game.opening_hands()
        # print each player's opening hand
        for player in self._game.get_players():
            print(player.get_name() + "'s opening hand:")
            hand = player.get_hand_ascii()
            print('\n'.join(hand))
            self.pause()
        # show dealer opening hand
        print("Dealer's opening hand:")
        dealer_hand = self._game.get_dealer_revealed_ascii()
        print('\n'.join(dealer_hand))
        self.pause()
        # gets all player choices for all players
        # after this, there are no more players to take their turns
        self.make_play_choice()
        # print dealer hand
        print("############### DEALER TURN ###############")
        dealer_hand = self._game.get_dealer_full_hand_ascii()
        print('\n'.join(dealer_hand))
        while not self._game.game_done():
            self.dealer_turn()
        

        print("############## GAME ENDED #################")
        for player in self._game.get_players():
            if not self._game.is_bust_dealer():
                dealer_total = self._game.get_dealer_total()
            else:
                dealer_total = 0

            if player.player_wins(dealer_total):
                print(player.get_name() + " wins, recieves "+ str(player.get_bet()*2))
            else:
                print(player.get_name() + " loses, recieves 0")

    def dealer_turn(self):
        """
        The dealer takes their turn (automatically) and their cards/score 
        is shown to the users
        """
        self._game.take_dealer_turn()
        # ascii art
        dealer_hand = self._game.get_dealer_full_hand_ascii()
        print('\n'.join(dealer_hand))
        # print score and determine if bust
        total = self._game.get_dealer_total()
        print("score:" + str(total))
        if total > 21:
            print("############ DEALER BUST ###############")

    def display_text_art(self):
        """
        Show 'blackjack' in big ascii art text at the beginning
        """
        with open("src/ascii_art/blackjack_text.txt", "r") as text:
            to_show = text.readlines()
        print(''.join(to_show))

    def create_players(self):
        """
        For each o the specified players, ask for their name and bet, 
        then instantiate a Player object for them

        Returns:
            [Player object]: The list of instantiated players
        """
        all_players = []
        for x in range(self._num_players):
            name, bet = self.get_player_name_bet(x+1)
            all_players.append(Player(name, bet))
        return all_players

    def get_player_name_bet(self, player_num):
        """
        Args:
            player_num (int): index of player (to print 'Player [1]' etc.)

        Returns:
            (str, int): Player name, player bet
        """
        # prompted to enter name
        player_name = self.get_player_name(player_num)
        # prompted to enter bet
        player_bet = self.get_player_bet(player_name)
        return (player_name, player_bet)

    def pause(self):
        """
        The user must press enter to continue, slows down the flow of the program so that 
        everything can be observed as appropriate
        """
        input("")

    def get_number_input(self, message, min, max):
        """
        

        Args:
            message (str): The prompt to give
            min (int): the minimum accepted value
            max (int): the maximum accepted value

        Returns:
            int: the number that the user correctly entered
        """
        invalid = True
        number = 0
        print(message)
        while invalid:
            number = input(">>")
            try:
                number = int(number)
                if (number >= min) and (number <= max):
                    # valid number
                    invalid = False
                else:
                    print("Invalid option - please enter a number between "
                        + str(min) + " and " + str(max))
            except Exception as e:
                # catches if a non-integer was entered
                print("Invalid option - please enter a number between "
                        + str(min) + " and " + str(max))
        # returns accepted number
        return int(number)

    # get num players
    def get_entered_num_players(self):
        """
        Returns:
            int: Number of players
        """
        message = "Enter number of players (1-7):"
        # number of players between 1 and 7 inclusive
        return self.get_number_input(message, 1, 7)

    def get_player_name(self, num):
        """
        Prompts the user to enter the name of the specified player.

        Args:
            num (int): The player number

        Returns:
            str: The entered name
        """
        print("Please enter player " + str(num) + "'s name")
        name = input(">>")
        if name == "":
            return "Player"
        return name

    def get_player_bet(self, name):
        """
        Prompts the user to enter the bet amount of the player.
        Allows integers between 1 and 100 inclusive.

        Args:
            name (str): the player name to be formatted to the displayed string

        Returns:
            int: player's bet
        """
        message = "Enter " + name +"'s bet:"
        # number of players between 1 and 7 inclusive
        return self.get_number_input(message, 1, 100)

    # get num packs used
    def get_entered_num_packs(self):
        """
        Returns:
            int: Number of packs of cards
        """
        message = "Enter the number of packs to use (1-6)"
        # number of players between 1 and 7 inclusive
        return self.get_number_input(message, 1, 6)

    # display player's cards
    def show_current_player_cards(self):
        """
        Returns:
            str: the ascii representation of the current player's cards
                    as one string.
        """
        return '\n'.join(self._game.get_current_player_ascii())

    def make_play_choice(self):
        """
        For all players, prompt them for all of their turns,
        calling appropriate functions for changing the state of their hand etc.
        """
        players_to_play = True
        # one iteration of this loop is one player's whole turn
        while players_to_play:
            print("########" + self._game.get_current_player_name().upper() + "'S TURN ########")
            self.show_player_details()
            finished_turn = False
            # one iteration of this loop is one player's single turn
            while not finished_turn:
                invalid = True
                print("(H)it, (S)tand, or (D)ouble down?")
                # oen iteration of this loop is one valid/invalid turn
                while invalid:
                    invalid = False
                    # get input
                    choice = input(">>").lower()
                    if choice in ["h", "s", "d"]:
                        # do required actions based on the choice
                        self._game.player_choice(choice)
                    else:
                        print("Please enter 'h', 's' or 'd'.")
                        invalid = True
                self.show_player_details()
                self.pause()
                # determine whether the player can take another turn
                finished_turn = self._game.get_turn_end()
            players_to_play = not(self._game.is_done())
            # if players still remain, get the next one!
            if players_to_play:
                self._game.set_next_player()


    def show_player_name(self):
        """
        Returns:
            str: representation of current player's name to print
        """
        name = self._game.get_current_player_name()
        return "Name: " + name

    def show_player_score(self):
        """
        Returns:
            str: representation of current player's score to print
        """
        score = self._game.get_current_player_total()
        return "Score: " + str(score)
    
    def show_player_bet(self):
        """
        Returns:
            str: representation of current player's bet to print
        """
        bet = self._game.get_current_player_bet()
        return "Bet: " + str(bet)
    
    def show_player_status(self):
        """
        Returns:
            str: representation of current player's status to print
        """
        # can be playing, standing or bust
        status = self._game.current_player_status()
        return "******STATUS: " + status + " ******"

    def show_player_details(self):
        """
        Gets and prints all information about the current player.
        This will be shown at the end of each turn.
        """
        # name
        name = self.show_player_name()
        # score
        score = self.show_player_score()
        # bet value
        bet = self.show_player_bet()
        # ascii representation
        cards = self.show_current_player_cards()
        # status
        status = self.show_player_status()

        print(name)
        print(score)
        print(bet)
        print(cards)
        print(status)
        