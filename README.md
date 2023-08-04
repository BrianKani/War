# Card War Game
This is a simple implementation of the classic card game "War" in Python. The game simulates a battle between two players, each drawing cards from a shuffled deck and comparing their values to determine the winner of each round.

# Features
Simulates a game of "War" between two players.
Uses a standard 52-card deck with four suits: spades, hearts, diamonds, and clubs.
Players draw cards from the deck and compare their values to determine the winner of each round.
Tracks the number of rounds won by each player.
Declares the overall winner at the end of the game.
# Classes
Card
Represents a playing card with a specific value and suit.

value: The value of the card (2 to 14, where 11=Jack, 12=Queen, 13=King, 14=Ace).
suit: The suit of the card (0=spades, 1=hearts, 2=diamonds, 3=clubs).
Deck
Represents a deck of playing cards.

cards: A list of Card objects representing the current deck.
Player
Represents a player in the game.

name: The name of the player.
cards: The cards drawn by the player.
wins: The number of rounds won by the player.
Game
Represents the game and controls its flow.

deck: An instance of the Deck class representing the game deck.
player1: An instance of the Player class for player 1.
player2: An instance of the Player class for player 2.
Methods
play_game(): Manages the gameplay loop, where players draw cards and compare them until the deck is empty or the game is quit.
winner(player1, player2): Determines the overall winner based on the number of rounds won by each player.

# Implementation
Run the script in a Python environment.
Enter the names of the two players.
Follow the prompts to play each round by pressing any key to draw cards or 'q' to quit.
The game will display the drawn cards and announce the winner of each round.
At the end of the game, the overall winner will be declared.
