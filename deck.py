"""
Cribbage2
Erica Chesley
Winter/Spring 2020

Cribbage game program written for Hackbright Academy Phenomenal Women Scholarship application.
Run from main.py; see README.txt for more information.
"""

import random

from card import *

class Deck:
    def __init__(self):
        self.ranks = ['A', 2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K']
        self.suits = ['♦', '♥', '♠', '♣']
        self.used = []
        self.played = []
        self.setLength = 1
        self.values = {             #for counting
            'A':1,
            2:2,
            3:3,
            4:4,
            5:5,
            6:6,
            7:7,
            8:8,
            9:9,
            10:10,
            'J':10,
            'Q':10,
            'K':10
        }
        self.equivs = {             #for sorting
            'A':1,
            2:2,
            3:3,
            4:4,
            5:5,
            6:6,
            7:7,
            8:8,
            9:9,
            10:10,
            'J':11,
            'Q':12,
            'K':13
        }
        
    #draw new card from deck (randomly select rank & suit and check if already drawn)
    def draw(self):
        while True:
            rank = self.ranks[random.randint(0, len(self.ranks)-1)]
            suit = self.suits[random.randint(0, len(self.suits)-1)]
            newCard = Card(rank, suit, self)
            taken = False
            for card in self.used:
                if card.rank == newCard.rank and card.suit == newCard.suit:
                    taken = True
                    break
            if not taken:
                self.used.append(newCard)
                return newCard
            
    #deal new hand of 6 cards to player
    def deal(self, player):
        while (len(player.hand) < 6):
            card = self.draw()
            player.hand.append(card)
            
    #check for pairs during play/go phase
    def checkPair(self):
        if len(self.played) < 2:
            return False
        elif self.played[-2].rank == self.played[-1].rank:
            return True
        else: 
            return False
        
    #check if given set of cards is a run
    def checkRun(self, cards):
        for i in range(1, len(cards)):
            if cards[i].equiv != cards[i-1].equiv+1:
                return False
        return True
    
    #check for runs in consecuitve cards during play/go phase
    def checkRunLastN(self, n):
        if len(self.played) >= n and self.setLength == 1:
            last = self.played[-n:]
            last = sorted(last, key=lambda x:x.equiv)
            return self.checkRun(last)
        else:
            return False
            
