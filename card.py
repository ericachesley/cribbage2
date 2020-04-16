"""
Cribbage2
Erica Chesley
Winter/Spring 2020

Cribbage game program written for Hackbright Academy Phenomenal Women Scholarship application.
Run from main.py; see README.txt for more information.
"""

class Card:
    def __init__(self, rank, suit, deck):
        self.rank = rank
        self.suit = suit
        self.value = deck.values[rank]      #for counting
        self.equiv = deck.equivs[rank]      #for sorting
        self.played = False