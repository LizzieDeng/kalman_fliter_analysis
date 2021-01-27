"""
A module providing a class for playing cards

This implementation is adapted from chapter 18 of the course text, _Think Python_,
by Allen B. Downey.

Authors: Walker White (wmw2), Steve Marschner (srm2), and Lillian Lee (ljl2)
Date:    October 20, 2019
"""


class Card(object):
    """
    A class to represent a standard playing card.

    Attribute suit: the suit of this particular card.
    Invariant: suit is an int in 0..NUM_SUITS-1
    The name of this suit is given by SUIT_NAMES[suit].

    Attribute rank: the rank of this particular card.
    Invariant: rank is an int in 1..NUM_RANKS
    The name of this rank is given by RANK_NAMES[rank].

    Attribute NUM_SUITS: The number of card suites
    Invariant: NUM_SUITS is an int. It is a CLASS
    ATTRIBUTE and should never be changed.

    Attribute NUM_RANKS: The number of card ranks
    Invariant: NUM_SUITS is an int. It is a CLASS
    ATTRIBUTE and should never be changed.

    Attribute SUIT_NAMES: The names of all four suits
    Invariant: SUIT_NAMES is a list of str. It is a CLASS
    ATTRIBUTE and should never be changed.

    Attribute RANK_NAMES: The names of the card ranks
    Invariant: RANK_NAMES is a list of str (or None). It
    is a CLASS ATTRIBUTE and should never be changed.

    Hence, if we execute c = Card(0, 12), SUIT_NAMES[c.suit]
    is 'Clubs' and RANK_NAMES[c.rank] is '12' and this
    card is the Queen of Clubs.
    """

    # CLASS ATTRIBUTES TO DEFINE CARD SUITS AND RANKS (Stored in Class Folder)
    SUIT_NAMES = ['Clubs', 'Diamonds', 'Hearts', 'Spades']
    NUM_SUITS  = len(SUIT_NAMES)

    # Starts at None so that we can treat RANK_NAMES as a translation table:
    # RANK_NAME[1] is 'Ace', RANK_NAME[13] is 'King', etc.
    RANK_NAMES = [None, 'Ace', '2', '3', '4', '5', '6', '7',
                  '8', '9', '10', 'Jack', 'Queen', 'King']
    NUM_RANKS  = 13


    def __init__(self, suit=0, rank=1, code=None):
        """
        Initializes a card whose with given suit and rank.

        The suits and rank are represented as integers.  Alternatively,
        suit and rank can be encodedvtogether in a two-character string like
        '3H' (3 of hearts) or 'KS' (king of spades).  Use 'T' for Ten.

        Example: if we execute c = Card(0, 12), then this card is the Queen of
        Clubs, since SUIT_NAMES[c.suit] is 'Clubs' and RANK_NAMES[c.rank] is 12.
        The same card could be created by Card('QC').

        Parameter suit: the suit encoding (optional)
        Precondition: suit is an int in 0..NUM_SUITS-1 (inclusive)

        Parameter rank: the rank encoding (optional)
        Precondition: rank is an int in 1..NUM_RANKS (inclusive)

        Parameter code: the card encoded as a string (optional)
        Precondition: code is a 2-char string with code[0] in 'A23456789TJQK'
        and card[1] in 'CDHS'.
        """
        if code:
            suit = 'CDHS'.index(code[1])
            rank = ' A23456789TJQK'.index(code[0])
        self.suit = suit
        self.rank = rank

    def __str__(self):
        """
        Returns a readable string representation of this card.

        Example: '2 of Hearts'
        """
        return self.RANK_NAMES[self.rank] + ' of ' + self.SUIT_NAMES[self.suit]

    def __eq__(self, other):
        """
        Returns True if other is an equivalent card; False otherwise

        Parameter other: the value to compare
        Precondition: NONE (other can be anything)
        """
        return (isinstance(other,Card) and
                (self.suit, self.rank) == (other.suit, other.rank))

    def __ne__(self, other):
        """
        Returns False if other is an equivalent card; True otherwise

        Parameter other: the value to compare
        Precondition: NONE (other can be anything)
        """
        return not self.__eq__(other)

    def __lt__(self, other):
        """
        Returns True if this card is less than other

        Cards are compared according to poker ordering, with Aces high.

        Parameter other: the value to compare
        Precondition: other is a Card
        """
        if (self.rank == other.rank):
            return self.suit < other.suit
        else:
            left = 14 if self.rank == 1 else self.rank
            rght = 14 if other.rank == 1 else other.rank
            return left < rght


# Related Functions
def full_deck():
    """
    Returns a list of the standard 52 cards
    """
    output = []  # list of cards so far to be returned
    for suit in range(Card.NUM_SUITS):
        for rank in range(1,Card.NUM_RANKS+1):  # skip the None value
            output.append(Card(suit,rank))
    return output


def print_cards(clist):
    """
    Prints the cards in list clist.

    Parameter clist: the card list
    Precondition:  clist is a list of Cards, possibly empty.
    """
    for c in clist:
        print(str(c))
