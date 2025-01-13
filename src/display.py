"""
This class will contain all necessary functions for displaying the game logic to the terminal.

The main game logic is separated from this to ensure that additional implementations (such as a GUI) could be added
without refactoring the rest of the code.


Handles I/O
"""
from src.game_logic import GameLogic

class Display:
    def __init__(self):
        # self.num_players = self.get_entered_num_players()
        # self.num_packs = self.get_entered_num_packs()
        # self.game_instance = GameLogic()
        pass

    # display the 'blackjack' text art at the beginning
    def display_text_art(self):
        pass

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
                        + str(min) + "and" + str(max))
            except Exception as e:
                print("Invalid option - please enter a number between "
                        + str(min) + " and " + str(max))

        return number

    # get num players
    def get_entered_num_players(self):
        message = "Enter number of players (1-7):"
        # number of players between 1 and 7 inclusive
        return self.get_number_input(message, 1, 7)

    def get_player_name(self):
        print("Please enter player name")
        name = input(">>")
        if name == "":
            return "Player"
        return name

    def get_player_bet(self):
        message = "Enter player bet:"
        # number of players between 1 and 7 inclusive
        return self.get_number_input(message, 1, 100)

    # get num packs used
    def get_entered_num_packs(self):
        message = "Enter the number of packs to use (1-6)"
        # number of players between 1 and 7 inclusive
        return self.get_number_input(message, 1, 6)

    # display player's cards
    def show_single_player_cards(self):
        pass

    # display all players' cards
    def show_all_players_cards(self):
        pass

    # display dealers' cards
    # may just be show_single_player_cards()?

    # get choice 'h', 's', 'd'
    def make_play_choice(self):
        pass

    def show_finished_game(self):
        pass


