"""
This is only a partially complete solution

There is significantly less documentation than I would like (and no unit tests)
but I decided to include this work to demonstrate a working GUI.


"""
from tkinter import *
from PIL import Image, ImageTk
from src.game_logic import GameLogic
from src.player import Player
# path to card filenames
PATH = "src/images/"


class MainMenu():
    """
    The very first page that the user encounters, just has a continue button
    """
    def __init__(self, parent):
        self.parent = parent
        self.show_screen()

    def show_screen(self):
        """
        Main menu screen - 
        given more time would be centered with a nicer looking interface!

        """
        self.box = Frame(self.parent)
        self.box.grid(row=0, column=0, columnspan=2, padx=10, pady=10)
        title = Label(self.box, text="BLACKJACK")
        title.grid()
        start_button = Button(self.box, text="START", command=self.parent.go_to_settings)
        start_button.grid()
        pass


class OptionsScreen():
    """
    On this page, the player selects the number of players, and the 
    number of packs of cards to use for the deck 
    """
    def __init__(self, parent):
        self.parent = parent
        self.num_players = StringVar()
        self.num_packs = StringVar()
        # empty the screen before showing the options
        for widget in self.parent.winfo_children():
            widget.destroy()
        self.create_options()

    def create_options(self):
        """
        The input fields
        """
        players_label = Label(self.parent, text = 'Number of players:', font=('calibre',10, 'bold'))
        players_entry = Scale(self.parent, from_=1, to=6, orient=HORIZONTAL, variable=self.num_players)
        players_label.grid()
        players_entry.grid()
        # number of packs
        packs_label = Label(self.parent, text = 'Number of decks:', font=('calibre',10, 'bold'))
        packs_entry = Scale(self.parent, from_=1, to=4, orient=HORIZONTAL, variable=self.num_packs)
        packs_label.grid()
        packs_entry.grid()
        continue_button = Button(self.parent, text="SAVE SETTINGS", command=self.game_setup)
        continue_button.grid()

    def game_setup(self):
        """
        On button in this screen pressed, setup with the main class, and 
        move to the next menu
        """
        self.parent.set_num_packs(int(self.num_players.get()), int(self.num_packs.get()))


class PlayerNameBetScreen:
    """
    On this screen, the players pick their names and bet amounts
    """
    def __init__(self, parent, num_players):
        self.parent = parent
        self.player_entries = []
        self.num_players = num_players
        # destroy all other things on screen
        for widget in self.parent.winfo_children():
            widget.destroy()
        self.show_player_options()

    def show_player_options(self):
        """
        For each of the players, display input fields for their bet and name, with default values
        """
        for i in range(self.num_players):
            # player name label
            # player name field
            player_name = Label(self.parent, text="Player {num}'s name:".format(num=i+1))
            player_name.grid(row=2*i, column=0, rowspan=2)
            player_name_entry = StringVar()
            player_name_entry.set("Player {num}".format(num=i+1))
            player_name_field = Entry(self.parent, textvariable=player_name_entry)
            player_name_field.grid(row=2*i, column=1, rowspan=2, padx=10, pady=10)
            player_bet = Label(self.parent, text="Player {num}'s bet:".format(num=i+1))
            player_bet.grid(row=2*i, column=3, rowspan=2, padx=10, pady=10)
            player_bet_entry = StringVar()
            player_bet_entry.set("10")
            player_bet_field = Entry(self.parent, textvariable=player_bet_entry)
            player_bet_field.grid(row=2*i, column=4)
            self.player_entries.append((player_name_entry, player_bet_entry))

        submit_button = Button(command=self.get_player_values, text="CONTINUE")
        submit_button.grid(row=2*self.num_players, column=0, columnspan=4)

    def show_error_message(self, index):
        """
        Show errors on the screen for erroneous bet inputs

        Args:
            index (int): the index of the player with incorrect info
        """
        error = Label(self.parent, text="Bet must be a positive integer", foreground="red")
        error.grid(row=((index*2) + 1), column=4)
        pass

    def get_player_values(self):
        """
        Get input and determine if there are any errors. 
        If there are, remain on the screen and display them,
        else move to next menu.
        """
        player_info, errors = self.validate_player_options()
        if errors != []:
            for index in errors:
                self.show_error_message(index)
        else:
            self.parent.validated_players(player_info)

    def validate_player_options(self):
        #will hold the index of any bets which are erroneous
        player_options = []
        errors = []
        i = 0
        for player_name_entry, player_bet_entry in self.player_entries:
            # get value of the entry
            name = player_name_entry.get()
            bet = player_bet_entry.get()
            player_options.append((name, bet))
            if name == "":
                # set player name to default if empty
                name = "Player"+ int(i+1)
            try:
                bet = int(bet)
            except ValueError as e:
                # add an eroor
                errors.append(i)
            i+=1
        return (player_options, errors)
    


class BlackjackApp(Tk):
    """
    The main class.

    This does all of the display actions - instantiating the other classes for the menus
    at the beginning.

    This class is nowhere near as clean as I'd like it to be, 
    but it is sort of a minimum-working GUI.
    """
    def __init__(self):
        super().__init__()
        # Makes the window
        self.title("Blackjack")
        self.width = 800
        self.height = 500
        self.geometry(str(self.width) + "x" + str(self.height))
        self.num_packs = 1
        # Set the current player index to 0 (start with the first player)
        self.menu = None
        self.player_options = None
        # shows main menu
        self.titlescreen = MainMenu(self)
    
    def go_to_settings(self):
        """
        Called when the player presses start, moves to selecting number
        of players and decks to use
        """
        self.menu = OptionsScreen(self)
    

    def set_num_packs(self, num_players, num_packs):
        """
        Called when the number of packs and players 
        have been selected, moves to selecting the names and bets
        of each player.

        Args:
            num_players (int): the number of players 
            num_packs (int): the number of packs
        """
        self.num_packs = num_packs
        for widget in self.winfo_children():
            widget.destroy()
        self.current_player_index = 0
        self.player_options = PlayerNameBetScreen(self, num_players)


    def validated_players(self, player_list):
        """
        Called when the players have all entered valid name and bet values.

        Args:
            player_list [(str, int)]: list of tuples with name and bet
        """
        # Initialize the game with the selected number of players
        for widget in self.winfo_children():
            widget.destroy()
        player_objs = []
        for name, bet in player_list:
            player_objs.append(Player(name, bet))
        # initialise the game, with the players and number of packs
        self._game = GameLogic(player_objs, self.num_packs)
        self._game.opening_hands()  # Start the game

        # Create frames for layout with cards etc.
        self.create_widgets()
        # update the ui, set scores/cards etc.
        self.update_ui()

    def create_widgets(self):
        """
        Create the necessary widgets for the main game section layout - populating with the dealer and players' info.
        """
        # configures the grid layout such that the row/grid 
        self.grid_rowconfigure(0, weight=1, uniform=True)
        self.grid_columnconfigure(0, weight=2, uniform=True)
        self.grid_columnconfigure(1, weight=1, uniform=True)
        self.scroll_width = self.width // 3
        ###################### DEALER #########################
        self.dealer_full_frame = Frame(self, bg="green")
        self.dealer_full_frame.grid(row=0, column=0)
        self.dealer_full_frame.grid_columnconfigure(0, weight=1, uniform=True)
        self.dealer_full_frame.grid_rowconfigure(0, weight=1, uniform=True)

        # dealer's text-based list of cards go here
        self.dealer_label = Label(self.dealer_full_frame, text="")
        self.dealer_label.grid(row=0, column=0, padx=20, pady=20)

        # dealer's card graphics go here
        self.dealer_card_frame = Label(self.dealer_full_frame, bd=0, width=100, height=100)
        self.dealer_card_frame.grid(row=0, column=1, padx=20, pady=20)

        ####################### DECK ############################
        # an image of the back of the deck will be placed here
        self.deck = Label(self.dealer_full_frame, text="DECK HERE")
        self.deck.grid(row=0, column=2, padx=20, pady=20)

        ################# PLAYER LARGE FRAME ##############
        # frame encapsulating the elements of the active player
        self.player_full_frame = Frame(self, bg="green")
        self.player_full_frame.grid(row=1, column=0)

        # the current player's list of cards (text)
        self.player_label = Label(self.player_full_frame, text="")
        self.player_label.grid(row=0, column=0, padx=20, pady=20)

        # the current player's name
        self.player_name = Label(self.player_full_frame, text="NAME HERE")
        self.player_name.grid(row=0, column=1)

        # The current player's score
        self.score_display = Label(self.player_full_frame, text="Score:")
        self.score_display.grid(row=1, column=0)

        # The current player's hand (graphical images)
        self.card_frame = LabelFrame(self.player_full_frame, bd=0, width=100, height=100)
        self.card_frame.grid(row=0, column=1, padx=20, pady=20, rowspan=2)

        # a frame containing the buttons that a player can press
        self.button_frame = Frame(self.player_full_frame, bg="green")
        self.button_frame.grid(row=0, column=2, padx=20, pady=20, rowspan=2)

        # hit button
        self.hit_button = Button(self.button_frame, text="HIT", command=self.on_hit)
        self.hit_button.pack(side=TOP, padx=10, pady=10)

        # stand button
        self.stand_button = Button(self.button_frame, text="STAND", command=self.on_stand)
        self.stand_button.pack(side=TOP, padx=10, pady=10)

        # double down button
        self.double_button = Button(self.button_frame, text="DOUBLE DOWN", command=self.on_double)
        self.double_button.pack(side=TOP, padx=10, pady=10)

        # Scrollable list for other players' cards (on the right hand side)
        self.scrollable_frame = Frame(self, bg="green")
        self.scrollable_frame.grid(row=0, column=1, rowspan=2, padx=10, pady=10, sticky="nsew")

        # Canvas inside the scrollable frame
        self.canvas = Canvas(self.scrollable_frame, bg="green")
        # when the scrollbar is scrolled, move the canvas y-direction
        self.scrollbar = Scrollbar(self.scrollable_frame, orient="vertical", command=self.canvas.yview)
        self.canvas.configure(yscrollcommand=self.scrollbar.set)
        self.scrollable_canvas_frame = Frame(self.canvas, bg="green")

        # Create window inside the canvas and set anchor to the right (anchor=E) and adjust position
        self.canvas.create_window((0, 0), window=self.scrollable_canvas_frame, anchor=NW, width=self.scroll_width)

        # pack in the frame
        self.scrollbar.pack(side=RIGHT, fill=Y)
        self.canvas.pack(side=LEFT, fill=BOTH, expand=True)

        # add all the players inside the canvas
        self.update_player_list()

    def update_ui(self):
        """Update the UI with the current game state."""
        # update the dealer's cards
        self.update_dealer_cards()
        # update the current players' cards
        self.update_player_cards()
        # update all players' cards
        self.update_player_list()

    def update_dealer_cards(self):
        """Update the dealer's cards on the UI."""
        for widget in self.dealer_card_frame.winfo_children():
            widget.destroy()  # Clear the previous list of dealer's cards

        # text based cards
        dealer_cards_text = "\n".join([str(card.get_name()) for card in self._game.get_dealer().get_partial_hand()])
        self.dealer_label.config(text=f"Dealer's Cards:\n{dealer_cards_text}")
        # show dealer's cards graphically
        new_image_render = self.generate_stacked_cards(self._game.get_dealer_hand_files())
        image_label = Label(self.dealer_card_frame, image=new_image_render)
        image_label.image = new_image_render
        image_label.pack()
        
    def update_player_cards(self):
        """
        Update the current player's cards on the UI.
        
        """
        # clear the current player's card frame
        for widget in self.card_frame.winfo_children():
            widget.destroy()

        # get the player that is currently taking their turn 
        player = self._game.get_current_player()

        # lists the cards by name in the container
        player_cards_text = "\n".join([str(card.get_name()) for card in player.get_hand()])
        self.player_label.config(text=f"{player.get_name()}'s Cards:\n{player_cards_text}")

        self.score_display.config(text="Score: "+ str(player.get_hand_total()))

        # display the player's hand of cards
        new_image_render = self.generate_stacked_cards(player.get_hand_filenames())
        image_label = Label(self.card_frame, image=new_image_render)
        image_label.image = new_image_render
        image_label.pack()

    def update_player_list(self):
        """
        Update the list of other players' cards within the side panel
        
        Only one should changein any iteration, but updating just in case!!
        """
        for widget in self.scrollable_canvas_frame.winfo_children():
            widget.destroy()  # Clear the previous list of players' cards

        # for all of the players
        # would be more efficient to just get the current player
        for i, player in enumerate(self._game.get_players()):
            player_frame = Frame(self.scrollable_canvas_frame)
            player_frame.grid(row=i, column=0, padx=5, pady=5)

            player_label = Label(player_frame, text=player.get_name() + ":\n" + "\n".join([str(card.get_name()) for card in player.get_hand()]))
            player_label.pack()
            new_image_render = self.generate_stacked_cards(player.get_hand_filenames())
            player_card_frame = LabelFrame(player_frame, bd=0, width=200, height=100)
            player_card_frame.pack(side=TOP, padx=50, pady=10)
            image_label = Label(player_card_frame, image=new_image_render)
            image_label.image = new_image_render
            image_label.pack()

            # show the player's score
            player_score = Label(player_frame, text=("Score:" + str(player.get_hand_total())))
            player_score.pack()
            # shows the player's bet value
            player_bet = Label(player_frame, text=("Bet:" + str(player.get_bet())))
            player_bet.pack()

        self.scrollable_canvas_frame.update_idletasks()
        self.canvas.config(scrollregion=self.canvas.bbox("all"))

    def generate_stacked_cards(self, cards):
            cards_to_show = []
            card_resize_width = 100
            card_resize_height = 132
            for card in cards:
                cards_to_show.append(Image.open(PATH + card).resize((card_resize_width, card_resize_height)))

            # Number of cards to be shown in the stack
            num_cards = len(cards_to_show)

            # offset between each card - chosen to stack only vertically to fit best with the display.
            x_off, y_off = (0, 25)

            # Calculate window size
            window_size = (card_resize_width + (num_cards - 1) * x_off, card_resize_height + (num_cards - 1) * y_off)

            # Create blank image to put new card onto
            new_image = Image.new('RGB', (window_size), (255, 255, 255))

            # For each of the images, paste it onto the correctly-sized image
            for i, n in enumerate(cards_to_show):
                Image.Image.paste(new_image, n, (i*x_off, i*y_off))

            # Rendering
            return ImageTk.PhotoImage(new_image)

    def on_hit(self):
        """Handle the 'Hit' action."""
        self._game.on_hit()  # Update the player's state
        self.update_player_cards()  # Update the current player's cards 
        self.update_single_player()        
        if self._game.get_current_player_total() > 21:
            self.show_bust()
            self.on_stand()  # If player busts, automatically stay

    def on_double(self):
        """
        Handle double down action
        move to next player's turn 
        """
        self._game.on_double_down() 
        self.update_ui()
        # if there are no
        if not self._game.is_done():
            self.current_player_index += 1
            self._game.set_next_player()
            # wat for user to see their final score
            self.after(1000, self.update_ui())
        else:
            self.after(1000, self.dealer_turn())

    def on_stand(self):
        """
        Player has pressed 'stand' - update player's state
        and go to next player
        """
        # Move to the next player or dealer's turn
        if not self._game.is_done():
            self.current_player_index += 1
            self._game.set_next_player()
            self.update_ui()
        else:
            self.dealer_turn()

    def dealer_turn(self):
        """
        Add each card from the dealer's hand, waiting in between to let the player see the cards
        """
        while not self._game.game_done():
            self._game.take_dealer_turn()  # Dealer takes their turn
            self.after(500, self.update_ui())
        self.after(2000, self.show_result())

    def show_result(self):
        """Display the result after the dealer's turn.
        
        This should be in its own class, and with a better interface showing everyone's cards
        """
        results = self._game.get_winners()
        result_text = "\n".join(results)
        for widget in self.winfo_children():
            widget.destroy()
        self.result_label = Label(self, text=f"Game Over!\n{result_text}")
        self.result_label.grid(row=0, column=0, columnspan=2, padx=10, pady=10)
