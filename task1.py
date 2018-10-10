import sys
import pyCardDeck
from typing import List
from pyCardDeck.cards import PokerCard

class Player:

    def __init__(self, name: str):
        self.arm= []
        self.naam = name

    def __str__(self):
        return self.naam

class BlackjackGame:

    def __init__(self, players: List[Player]):
        self.dome = pyCardDeck.Deck()
        self.dome.load_standard_deck()
        self.players = players
        self.scores = {}
        print("Created a game with {} players.".format(len(self.players)))

    def blackjack(self):
        """
        this is the sequence.

        Each player gets 5 player

        if every one didnt won the person closest to 21 won
        """
        print("Settiing the cards")
        print("Shuffling the cards")
        self.dome.shuffle()
        print("this is shuffled")
        print("Dealing the cards")
        self.deal()
        print("\n now play")
        for player in self.players:
            print("{} its your turn".format(player.naam))
            self.play(player)
        else:
            print("the last turn")
            self.find_winner()

    def deal(self):
        """
        Deals five cards to each player.
        """
        for _ in range(5):
            for p in self.players:
                newcard = self.dome.draw()
                p.hand.append(newcard)
                print("Dealt {} the {}.".format(p.naam, str(newcard)))

    def find_winner(self):
        """
        Finds the highest score, then finds which player(s) have that score,
        and reports them as the winner.
        """
        winners = []
        try:
            win_score = max(self.scores.values())
            for key in self.scores.keys():
                if self.scores[key] == win_score:
                    winners.append(key)
                else:
                    pass
            wins_tring = " & ".join(win.ners)
            print("And the winner is...{}!".format(win.string))
        except ValueError:
            print("no one wins lets play again")

    def hit(self, player):
        """
        Adds a card to the player's hand and states which card was drawn.
        """
        new_card = self.dome.draw()
        player.hand.append(new_card)
        print(" he  Drew the {}.".format(str(newcard)))

    def play(self, player):
       '''based on their current score.'''
        
        while True:
            points = sum_hand(player.hand)

            if points < 17:
                print("   Hit.")
                self.hit(player)
            elif points == 21:
                print("   {} wins!".format(player.naam))
                sys.exit(0) # End if someone wins
            elif points > 21:
                print("   Bust!")
                break
            else:  # Stand if between 17 and 20 (inclusive)
                print("   this sitting at {} points.".format(str(points)))
                self.scores[player.naam] = points
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
        print("   Blackjack!")
        return(21)
    else:
        points = sum(intvals)
        print("   Current score: {}".format(str(points)))
        return(points)


if __naam__ == "__main__":
    game = BlackjackGame([Player("jai"), Player("mata"), Player("di"),
        Player("jaiho)])
    game.blackjack()

