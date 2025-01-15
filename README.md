# BBC Blackjack Implementation
 A terminal-based implementation of Blackjack for the BBC Assessment Centre technical interview


Welcome to my implementation of Blackjack :)
I decided to extend the given task to be a terminal-based fully playable game of blackjack.

# Setup
To run the tests: In the same folder as this README, run 'python3 -m unittest discover test"
To run the program: In the same folder as this README run 'python3 blackjack.py'


For this code, the following python libraries are required:
- colorama
- collections (deque)
- unittest

To install any that may be missing from your system, use 'pip install [package]'

# Design Considerations
- Separation of concerns between the IO/User Interface and the game logic allows
for further implementations to build upon the GameLogic (e.g. with a Tkinter GUI) 
without messing with the actual game logic too much.
- Testing - unit tests were created for each function in the program to ensure that everything
returned expected values/types etc. This also helped to make lots of small functions with one 
purpose - rather than huge sprawling functions that are incomprehensible (mostly)

# What have I learned?

I find that I learn something every time I write code.
Here, I have learned about printing in colour in the terminal with Python, and also
made my first ASCII art! 

# References
To consolidate my understanding of Blackjack's rules, I consulted:\
https://www.mastersofgames.com/rules/blackjack-rules.htm\
and chose to implement the 'Double Down' rule which was not present in the guidance document.\

This Python Implementation was mostly from my own previous knowledge, however supplemental research into 
specific functionalities listed below were conducted using the listed sources:
- Python Terminal Colour Printing: https://pypi.org/project/colorama/
- Python deque objects: https://docs.python.org/3/library/collections.html#collections.deque


