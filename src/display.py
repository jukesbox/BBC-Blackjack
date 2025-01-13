"""
This class will contain all necessary functions for displaying the game logic to the terminal.

The main game logic is separated from this to ensure that additional implementations (such as a GUI) could be added
without refactoring the rest of the code.


Handles I/O
"""
from src.game_logic import GameLogic

class Display:
    def __init__(self):
        self.num_players = self.get_entered_num_players()
        self.num_packs = self.get_entered_num_packs()
        self.game_instance = GameLogic()
        pass

    # display the 'blackjack' text art at the beginning
    def display_text_art(self):
        pass

    # get num players
    def get_entered_num_players(self):
        pass
    # get num packs used
    def get_entered_num_packs(self):
        pass

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


