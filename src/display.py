"""
This class will contain all necessary functions for displaying the game logic to the terminal.

The main game logic is separated from this to ensure that additional implementations (such as a GUI) could be added
without refactoring the rest of the code.


Handles I/O
"""
from src.game_logic import GameLogic
from src.player import Player

class Display:
    def __init__(self):
        self.display_text_art()
        self.pause()
        self.num_players = self.get_entered_num_players()
        self.num_packs = self.get_entered_num_packs()
        self.all_players = self.create_players()
        self.game = GameLogic(self.all_players, self.num_packs)
        pass

    def begin_game(self):
        self.game.opening_hands()
        for player in self.game.get_players():
            print(player.get_name() + "'s opening hand:")
            hand = player.get_hand_ascii()
            print('\n'.join(hand))
            self.pause()
        print("Dealer's opening_hand:")
        dealer_hand = self.game.get_dealer_revealed_ascii()
        print('\n'.join(dealer_hand))

        self.make_play_choice()
        while not self.game.game_done():
            self.dealer_turn()

        print("Dealer final hand:")
        dealer_hand = self.game.get_dealer_full_hand_ascii()
        print('\n'.join(dealer_hand))

        print("Winners:")
        for player in self.game.get_players():
            if player.player_wins(self.game.get_dealer_total()):
                # assume return on bet is *2 if wins
                print(player.get_name() + " wins, recieves: " + player.get_bet()*2)
            else:
                print(player.get_name() + " loses, recieves 0")
        
        input("END")


    def dealer_turn(self):
        self.game.take_dealer_turn()
        dealer_hand = self.game.get_dealer_full_hand_ascii()
        print('\n'.join(dealer_hand))



    # display the 'blackjack' text art at the beginning
    def display_text_art(self):
        with open("src/ascii_art/blackjack_text.txt", "r") as text:
            to_show = text.readlines()
        print(''.join(to_show))

    def create_players(self):
        all_players = []
        for x in range(self.num_players):
            name, bet = self.get_player_name_bet(x+1)
            all_players.append(Player(name, bet))
        return all_players

    def get_player_name_bet(self, player_num):
        player_name = self.get_player_name(player_num)
        player_bet = self.get_player_bet(player_name)
        return (player_name, player_bet)

    def pause(self):
        """
        The user must press enter to continue, slows down the flow of the program so that 
        everything can be observed as appropriate
        """
        input("**** PRESS ENTER TO CONTINUE ****")

    def get_number_input(self, message, min, max):
        invalid = True
        number = 0
        print(message)
        while invalid:
            number = input(">>")
            try:
                number = int(number)
                if (number >= min) and (number <= max):
                    invalid = False
                else:
                    print("Invalid option - please enter a number between "
                        + str(min) + " and " + str(max))
            except Exception as e:
                print("Invalid option - please enter a number between "
                        + str(min) + " and " + str(max))

        return int(number)

    # get num players
    def get_entered_num_players(self):
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
        message = "Enter the number of packs to use (1-6)"
        # number of players between 1 and 7 inclusive
        return self.get_number_input(message, 1, 6)

    # display player's cards
    def show_current_player_cards(self):
        return '\n'.join(self.game.get_current_player().get_hand_ascii())

    # display all players' cards
    def show_all_players_cards(self):
        pass

    # display dealers' cards
    # may just be show_single_player_cards()?

    # get choice 'h', 's', 'd'
    def make_play_choice(self):
        while not self.game.is_done(): # misses last iteration
            self.show_player_details()
            finished = False
            while not finished:
                invalid = True
                print("(H)it, (S)tand, or (D)ouble down?")
                while invalid:
                    invalid = False
                    choice = input(">>").lower()
                    if choice in ["h", "s", "d"]:
                        self.game.player_choice(choice)
                    else:
                        invalid = True
                self.show_player_details()
                finished = self.game.end_turn
            self.game.set_next_player()


    def show_player_name(self):
        name = self.game.get_current_player().get_name()
        return "Name: " + name

    def show_player_score(self):
        score = self.game.get_current_player().get_hand_total()
        return "Score: " + str(score)
    
    def show_player_bet(self):
        bet = self.game.get_current_player().get_bet()
        return "Bet: " + str(bet)
    
    def show_player_status(self):
        # can be playing, standing or bust
        status = self.game.current_player_status()
        return "******STATUS: " + status + " ******"

    def show_player_details(self):
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
        self.pause()
        



    def show_finished_game(self):
        pass


