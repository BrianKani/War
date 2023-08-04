from random import shuffle

class Card:
    suits = ["spades","hearts","diamonds","clubs"]
    values = [None,None, "2","3","4","5","6","7","8","9","10", "Jack","Queen",
              "King","Ace"]
    
    def __init__(self,value,suit):
       """suits and values should be integers"""
       self.value = value
       self.suit = suit

    def __lt__(self, other):
        """comparing the cards of each player"""

        if self.value < other.value:
            return True
        if self.value == other.value:
            if self.suit < other.suit:
                return True
            else:
                return False
            
    def __gt__(self, other):
        if self.value > other.value:
            return True
        if self.value == other.value:
            if self.suit > other.suit:
                return True
            else:
                return False
        return False
    
    def __repr__(self):
        return self.values[self.value] + " of " + self.suits[self.suit]
    
class Deck:
    def __init__(self):
        self.cards =[]
        for i in range (2 , 15):
            for j in range (4):
                self.cards.append(Card(i,j))
        shuffle(self.cards)
        
    def remove_card(self):
        if len (self.cards) == 0 :
            return
        return self.cards.pop()
    
class Player:
    def __init__(self, name):
        self.name = name
        self.cards = None
        self.wins =  0

class Game:
    def __init__(self):
        name1 = input("Player 1 name: ")
        name2 = input("player 2 name: ")
        
        self.deck = Deck()
        self.player1 = Player(name1)
        self.player2 = Player(name2)

    def play_game(self):
        cards = self.deck.cards
        print ("Starting War!")
        response = None
        while len(cards) >= 2  and response != 'q':
            response = input ("Press any key to play or q to quit")
            player1_card = self.deck.remove_card()
            player2_card = self.deck.remove_card()

            print ("{} drew {} {} drew {}".format(self.player1.name, player1_card, self.player2.name, player2_card))
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

game = Game()
game.play_game()