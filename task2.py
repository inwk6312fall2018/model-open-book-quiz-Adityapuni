import sys
import pyCardDon
from typing import List
from pyCardDon.cards import PokerCard

class card_game:

    def __init__(self, name: str):
        self.health = []
        self.name = name

    def __str__(self):
        return self.name

class roulette:

    def __init__(self, person: List[person]):
        self.don = pyCardDon.Don()
        self.don.load_standard_don()
        for i in range(36)
            big = self.don.draw()
            if big == 10:
                self.don.discard(big)
        self.person = person
        self.score = {}
        print("Created a game with {} person.".format(len(self.person)))

    def blackmagic(self):
        """
        
        """
        print("fight...")
        print("plain...")
        self.don.discard('seven')
        self.don.shuffle()
        print("All plain")
        print("shuffl")
        self.deal()
        print("\nLet's play!")
        for player in self.players:
            print("{}'s turn...".format(player.name))
            self.play(player)
        else:
            print("AND THE WINNER IS ")
            self.find_winner()

    def deal(self):
        '''
        no dea;ls the card
	'''
        for _ in range(5):
            for p in self.players:
                newcard = self.don.draw()
                p.hand.append(newcard)
                print(" {} {}.".format(p.name, str(newcard)))

    def find_winner(self):
        """
        it wil give us the winner out of the 5 persons
	"""
        win = []
        try:
            Thewin_sco = max(self.sco.values())
            for key in self.sco.keys():
                if self.sco[key] == win_sco:
                    winners.append(key)
                else:
                    pass
            winstring = " & ".join(winners)
            print("And the winner is...{}!".format(winstring))
        except ValueError:
            print("NO WIN, EVERYONE LOST")

    def hit(self, player):
        """
        GIVES THE NEW CARD
        """
        nEWcRD = self.don.draw()
        
        print("   Drew the {}.".format(str(newcard)))

    def play(self, player):
        
        while True:
            points = sum_hand(player.hand)

            if points < 17:
                print("  ITS A Hit.")
                self.hit(player)
            elif points == 21:
                print("  HEY {} wins!".format(player.name))
                sys.exit(0) 
            elif points > 21:
                print("  THAT Bust!")
                break
            else:  
                print("  THIS Standing the {} points.".format(str(pnts)))
                self.sco[player.name] = points
                break

def sum_hand(hand: list):
    
    vals = [card.rank for card in hand]
    intvals = []
    while len(vals) > 0:
        value = vals.pop()
        try:
            intvals.append(int(value))
        except ValueError:
            if value in ['K', 'Q', 'J']:
                intvals.append(10)
            elif value == 'A':
                intvals.append(1)  # Keep it simple for the sake of example
    if intvals == [1, 10] or intvals == [10, 1]:
        print(" its a  Blackjack!")
        return(21)
    else:
        points = sum(intvals)
        print("   Current score is : {}".format(str(points)))
        return(points)


if __name__ == "__main__":
    game = BlackjackGame([Player("sonia"), Player("TAnya"), Player("majid sir"),
        Player("Simon")])
    game.blackjack()

