"""
A module providing a class to represent pokers hands.

Authors: Walker White (wmw2), Steve Marschner (srm2), and Lillian Lee (ljl2)
Date:    October 20, 2019
"""
import card
import random


class Hand(object):
    """
    A class to represent a hand in poker.

    Attribute cards: The cards in the poker hand
    Invariant: card is a list of Card objects.
    This list is sorted according to the ordering
    defined by the Card class.
    """

    def __init__(self, deck, n):
        """
        Initializes a hand of n cards.

        Parameter deck: The initital deck to draw from
        Precondition: deck is a list of >= n cards.
        Deck is assumed to be shuffled.

        Parameter n: The number of cards to draw
        Precondition: n is an int >= 0
        """
        self.cards = []
        for i in range(n):
            self.cards.append(deck.pop(0))
        self.cards.sort()
        #
        #cards = deck[0:n]
        #deck[0:n] = []

    def is_full_house(self):
        """
        Returns True if this hand is a 5-card full house.
        """
        pass # LEFT AS AN EXERCISE

    def is_flush(self):
        """
        Returns True if this hand is a 5-card flush.
        """
        pass # LEFT AS AN EXERCISE

    def is_pair(self):
        """
        Returns True if this hand contains a pair.
        """
        pass # LEFT AS AN EXERCISE

    def discard(self, k):
        """
        Discards the k-th card, counting from zero.

        Parameter k: the card to discard
        Precondition: Hand contains at least k+1 cards
        """
        pass # LEFT AS AN EXERCISE

    def __str__(self):
        """
        Returns: A string representation of this hand.
        """
        return ', '.join(map(str, self.cards))


def demo_hand():
    """
    Shows off hands in action
    """
    deck = card.full_deck()
    random.shuffle(deck)
    print(Hand(deck,5))


if __name__ == '__main__':
    demo_hand()
