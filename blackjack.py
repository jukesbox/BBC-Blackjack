"""
The program should be run from this file.
If any additional implementations were added, they should 
be added as an option here.
"""

from src.display import Display
from src.tkinter_ui import BlackjackApp

if __name__ == "__main__":
    graphical = True
    if graphical:
        app = BlackjackApp()
        app.mainloop()
    else:
        display = Display()
        display.begin_game()