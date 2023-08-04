from Deck import Deck
from player import Player

class Game(object):
    def __init__(self):
        name1 = input("Player 1 name: ")
        name2 = input("player 2 name: ")
        
        self.deck = Deck()
        self.Player1 = Player(name1)
        self.player2 = Player(name2)

    def play_game(self):
        cards = self.deck.cards
        print ("Starting War!")
        response = None
        while len(cards) >= 2  and response != 'q':
            response = input ("Press any key to play or q to quit")
            player1_card = self.deck.remove_card()
            player2_card = self.deck.remove_card()

            print ("{} drew {} {} drew {}".format(self.Player1.name, player1_card, self.player2.name, player2_card))
            if player1_card > player2_card:
                self.player1.wins += 1
                print("{} wins this Round".format(self.player1.name))
            else:
                self.player2.wins += 1
                print("{} wins this round".format(self.player2.name))
        print ("The War is over. {} Wins".format(self.winner(self.player1, self.player2)))

    def winner(self, player1, player2):
        if player1.wins > player2.wins:
            return player1.name
        if player1.wins < player2.wins:
            return player2.name
        return "It was a tie ! stalemate"







