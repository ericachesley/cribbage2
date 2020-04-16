"""
Cribbage2
Erica Chesley
https://github.com/ericachesley/cribbage2

Cribbage game program written for Hackbright Academy Phenomenal Women Scholarship application.
Run from main.py; see README.txt for more information.
"""

import time
from constants import PRINT_SPEED

class Teacher:
    def __init__(self):
        self.on = False
        self.firstRound = True
        self.firstPlay = True
        self.firstGo = True
        self.firstCount = True

    def intro(self):
        time.sleep(PRINT_SPEED)
        print ("\nTo begin the game, we'll deal six cards to each player out of a standard 52 card deck.")
        input("[Enter to proceed] ")

    def crib(self):
        time.sleep(PRINT_SPEED)
        print ("\nNow that you have your hand, you need to choose two cards to set aside into the 'crib', Your opponent will also put two cards into the crib.") 
        time.sleep(PRINT_SPEED)
        print("\nLater in the round, after both players score their own hands, the current dealer will also get to score the crib and gain any points from it.")
        input("[Enter to proceed] ")

    def starter(self):
        time.sleep(PRINT_SPEED)
        print ("\nOnce the crib is made, we flip the top card of the deck to reveal the 'starter'.")
        time.sleep(PRINT_SPEED)
        print("\nThe starter is mostly relevant during the scoring phase, but if it is a Jack, the dealer automatically gets two points (called 'His heels').")
        input("[Enter to proceed] ")

    def play(self):
        time.sleep(PRINT_SPEED)
        print ("\nEach round begins with the 'play' phase wherein players alternate playing a single card from their hands. As they play, they keep a running sun of the cards played thus far (with all face cards valued at 10 and Ace at 1). The sum may not go over 31.")
        time.sleep(PRINT_SPEED)
        print("\nIf a player cannot play without exceeding 31, that person says 'Go,' their opponent gets a point, and we move to the 'go' phase.")
        time.sleep(PRINT_SPEED)
        print("\nDuring the 'play' phase, certain sequences can earn a player points.")
        time.sleep(PRINT_SPEED)
        print("• If a player's card makes the count exactly 15, they get 2 points.")
        time.sleep(PRINT_SPEED)
        print("• Likewise, if their card matched the previously played cards making a pair, they earn 2 points. A triplet earns 6 points.")
        time.sleep(PRINT_SPEED)
        print("• If three, four, or five consequtive cards form a run of adjacently ranked cards (e.g. 10, J, Q), the player who just played gets 3, 4, or 5 points respectively.")
        time.sleep(PRINT_SPEED)
        print("\nNote: For runs, the cards do not have to have been played in sequence - Q, 10, J would still count, for example. If a player gets the count exactly to 31, they get two points and the 'go' phase is skipped.")
        input("[Enter to proceed] ")

    def go(self):
        time.sleep(PRINT_SPEED)
        print ("\nWhen a player says 'Go,' their opponent plays as many cards as they are able without going over 31.")
        time.sleep(PRINT_SPEED)
        print("\nScoring opportunities (15, pairs, and runs) are the same as in the 'play' phase. If a player hits exactly 31 in the 'go' phase, they get an additional point, on top of the point for gaining the 'Go.'")
        input("[Enter to proceed] ")

    def skipGo(self):
        time.sleep(PRINT_SPEED)
        print ("\nBecause we hit exactly 31 in the 'play' phase, the 'go' phase will be skipped this round and we begin a new 'play' phase.")

    def repeatPlayGo(self):
        time.sleep(PRINT_SPEED)
        print ("\nThe 'play' and 'go' phases repeat until both players have played all their cards.")
        input("[Enter to proceed] ")

    def combos(self):
        time.sleep(PRINT_SPEED)
        print ("\nOnce both players have played all their cards, we move to counting combinations.")
        time.sleep(PRINT_SPEED)
        print("\nBoth players receive the four cards they've just played back into their hands to count combinations. At this stage, the starter card that was drawn earlier in the game becomes like a fifth card in each player's hand.")
        time.sleep(PRINT_SPEED)
        print("\nThe non-dealer scores their hand first, then the dealer, and then the dealer scores the crib as well.")
        time.sleep(PRINT_SPEED)
        print("\nPoints are earned as follows:")
        time.sleep(PRINT_SPEED)
        print("• Any set of cards totaling 15 (with face cards as 10) earns 2 points.")
        time.sleep(PRINT_SPEED)
        print("• Each pair of the same rank earns 2 points.")
        time.sleep(PRINT_SPEED)
        print("• Each run of three or more cards earns 1 point per card in the run.")
        time.sleep(PRINT_SPEED)
        print("• A flush of four cards of the same suit (not including the starter and not applicable for the crib) earns 4 points, and a five card flush including the starter earns 5 points.")
        time.sleep(PRINT_SPEED)
        print("• Finally, a Jack of the same suit as the starter earns 1 point.")
        time.sleep(PRINT_SPEED)
        print("\nA card may be used as part of multiple combinations.")
        input("[Enter to proceed] ")

    def repeatRound(self):
        time.sleep(PRINT_SPEED)
        print ("\nOnce the combinations have been counted, all cards are shuffled back into the deck and a new round is dealt.")
        time.sleep(PRINT_SPEED)
        print("\nThe game continues until one player reaches the winning score (which may happen in the middle of a round).")
        input("[Enter to proceed] ")

    def wantTeacher(self):
        while True:
            wantTeacher = input("\nWould you like to see instructions as you play? (y/n) ")
            if wantTeacher == "y" or wantTeacher == "Y" or wantTeacher == "yes" or wantTeacher == "Yes":
                self.on = True
                print ("Sounds good! First, we need to select a winning score and a first dealer...\n")
                return
            elif wantTeacher == "n" or wantTeacher == "N" or wantTeacher == "no" or wantTeacher == "No":
                self.on = False
                print ("Ok, you've got this!\n")
                return
            else:
                print("Invalid selection. Please try again.")