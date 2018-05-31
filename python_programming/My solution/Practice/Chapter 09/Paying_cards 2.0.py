# Playing Cards 2.0
#
# Demostrates inheritance- class extention

class Card(object):
    """A Playing card."""
    RANKS = ["A",'1','2','3','4','5','6','7','8','9','10',
                     'J','Q','K']

    SUITS = ['c','d','h','s']

    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit

    def __str__(self):
        rep = self.rank + self.suit
        return rep

class Hand(object):
    """A hand of playing cards."""
    def __init__(self):
        self.cards =[]

    def __str__(self):
        if self.cards:
            rep =""
            for card in self.cards:
                rep += str(card) + " \t"
        else:
            rep = "<empty>"
        return rep

    def clear(self):
        self.cards =[]

    def add(self,card):
        self.cards.append(card)

    def give(self,card, other_hand):
        self.cards.remove(card)
        other_hand.add(card)

class Deck(Hand):
    """A deck of playing cards."""
    def populate(self):
        for suit in Card.SUITS:
            for rank in Card.RANKS:
                self.add(Card(rank,suit))

    def shuffle(self):
        import random
        random.shuffle(self.cards)

    def deal(self, hands, per_hand = 1):
        for round in range(per_hand):
            for hand in hands:
                if self.cards:
                    top_card = self.cards[0]
                    self.give(top_card, hand)
                else:
                    print("Can't continue deal. Out of cards!")
                    
# main

deck1 = Deck()
print("Created a new deck.")
print("Deck:")
print(deck1)

deck1.populate()
print("\nPopulated Deck.")
print("Deck:")
print(deck1)

deck1.shuffle()
print("\nShuffled the deck.")
print("Deck:")
print(deck1)

my_hand = Hand()
your_hand = Hand()
hands = [my_hand, your_hand]

deck1.deal(hands,per_hand = 5)
print("\nDealt 5 cards to my hand and your hands.")
print("My hand:")
print(my_hand)
print("Your hand:")
print(your_hand)
print("Deck:")
print(deck1)

deck1.clear()
print("\nCleared the deck.")
print("Deck:", deck1)

input("\n\nPress the enter key to exit.")


"""
      
card1 = Card(rank="A", suit='c')
print("printing a Cards Object:")
print(card1)
card2 = Card('B','c')
card3 = Card ('C','c')
card4 = Card('D','c')
card5 = Card('E','c')
print("\nPrinting rest of the objects individually:")
print(card2)
print(card3)
print(card4)
print(card5)

my_hand = Hand()
print("\nPrinting my hand before I add any cards:")
print(my_hand)
my_hand.add(card1)
my_hand.add(card2)
my_hand.add(card3)
my_hand.add(card4)
my_hand.add(card5)
print("\nPrinting my hand after adding 5 cards:")
print(my_hand)

your_hand = Hand()
print("\nYour hand initially is empty")
print(your_hand)
my_hand.give(card1,your_hand)
my_hand.give(card2,your_hand)
print("\nGave the first two cards frommy hand to your hand:")
print("Your Hand:")
print(your_hand)
print("My Hand:")
print(my_hand)

my_hand.clear()
print("Print my hand after clearing it:")
print(my_hand)

input("\n\npress the enter key to exit")

"""    
