"""
Cribbage2
Erica Chesley
Winter/Spring 2020

Cribbage game program written for Hackbright Academy Phenomenal Women Scholarship application.
Run from main.py; see README.txt for more information.
"""

import random
import time

from player import *
from deck import *
from round import *
from teacher import *

from constants import PRINT_SPEED

#play a full series of rounds until the winning score is reached
def fullGame(p,c):
    
    t = Teacher()
    t.wantTeacher()
    time.sleep(PRINT_SPEED)

    winningScore = pickWinningScore()
    dealer = pickFirstDealer(p,c)
    
    while True:
        #loop full rounds until there is a winner
        fullRound(p, c, t, winningScore, dealer)
            
        #check for a winner
        if p.score >= winningScore:
            time.sleep(PRINT_SPEED)
            print ("\n----------", p.name, "wins!----------")
            time.sleep(PRINT_SPEED)
            print (p.name, "'s score:", p.score, " ~  Computer 's score:", c.score)
            break
        elif c.score >= winningScore:
            time.sleep(PRINT_SPEED)
            print ("\n----------", c.name, "wins!----------")
            time.sleep(PRINT_SPEED)
            print (p.name, "'s score:", p.score, " ~  Computer 's score:", c.score)
            break

        #swap dealer before next game
        if dealer == c:
            dealer = p
        else:
            dealer = c

#full round = deal, play, go, [play, go, ...], count
def fullRound(p, c, t, winningScore, dealer):

    if t.on and t.firstRound:
        t.intro()
    
    time.sleep(PRINT_SPEED)
    print("\n---------- New round ( playing to", winningScore,") ----------\n")
    
    #create a new Game class (aka round)
    r = Round(dealer, p, c, winningScore)
    time.sleep(PRINT_SPEED)
    r.printScores()

    #clear hands from previous round
    p.hand = []
    p.played = []
    c.hand = []
    c.played = []

    #deal
    print (dealer.name, "'s deal.")
    d = Deck()
    d.deal(p)
    d.deal(c)
    time.sleep(PRINT_SPEED)
    print("Deal finished.")
    time.sleep(PRINT_SPEED)
    print("\nYour hand: ", end="")
    p.printHand()

    input("[Enter to proceed] ")

    if t.on and t.firstRound:
        t.crib()

    #make the crib
    r.makeCrib(p,c,t.firstRound)

    input("[Enter to proceed] ")

    if t.on and t.firstRound:
        t.starter()

    #draw the starter
    r.drawStarter(d)
    if r.starter.rank == "J":
        dealer.score += 2
        time.sleep(PRINT_SPEED)
        print ("**His heels (starter is a Jack)! Dealer (", dealer.name, ") gets two points.**\n")
        r.printScores()

    input("[Enter to proceed] ")

    #loop between play and go as long as any player has cards in hand
    while len(p.hand) > 0 or len(c.hand) > 0:

        if t.on and t.firstPlay:
            t.play()

        r.play(p,c,d,t)
        if r.gameOver:
            return

        if t.on and t.firstGo and not r.thirtyone and len(p.hand)+len(c.hand) > 0:
            t.go()
            t.firstGo = False

        if t.on and t.firstGo and r.thirtyone:
            t.skipGo()

        r.go(p,c,d)
        if r.gameOver:
            return

        if t.on and t.firstPlay:
            t.repeatPlayGo()
            t.firstPlay = False

    if t.on and t.firstCount:
        t.combos()
        t.firstCount = False

    #once hands are empty, pick cards back up and count/score combinations
    time.sleep(PRINT_SPEED)
    print("\n---- Counting Combinations -----")

    input("[Enter to proceed] ")

    if dealer == c:
        p.countCombinations(r, d, False)
        if r.gameOver:
            return
        c.countCombinations(r, d, True)
    else:
        c.countCombinations(r, d, False)
        if r.gameOver:
            return
        p.countCombinations(r, d, True)
    
    if r.gameOver:
        return

    if t.on and t.firstRound:
        t.repeatRound()
    
    t.firstRound = False

#set up - play to 61 or 121        
def pickWinningScore():
    while True:
        winningScore = input("Would you like to play to (a) 61 or (b) 121? ")
        if winningScore == "a" or winningScore == "A" or winningScore == "61":
            return 61
        elif winningScore == "b" or winningScore == "B" or winningScore == "121":
            return 121
        else:
            print("Invalid selection. Please try again.\n")
    
#set up - who deals first
def pickFirstDealer(person, computer):
    while True:
        dealer = input("Who should deal first? (a) You or (b) Computer? ")
        if dealer == "a" or dealer == "A" or dealer == "Me" or dealer == "me":
            return person
        elif dealer == "b" or dealer == "B" or dealer == "Computer" or dealer == "computer":
            return computer
        else:
            print("Invalid selection. Please try again.\n")
            
#offer another game when game ends
def playAgain():
    while True:
        choice = input("\nWould you like to play again? (y/n) ")
        if choice == "y" or choice == "Y" or choice == "yes" or choice == "Yes":
            return True
        elif choice == "n" or choice == "N" or choice == "no" or choice == "No":
            time.sleep(PRINT_SPEED)
            print("Goodbye!\n")
            return False
        else:
            print("Invalid selection. Please try again.\n")
    
def main():
    
    print("\nWelcome.")
    while True:
        p = Player(input("What's your name? "))
        if p.name == "Computer":
            print ("That name is taken. Please select a different name.\n")
        else:
            break

    c = Player("Computer")
    
    while True:
        fullGame(p,c)
        
        if playAgain():
            p = Player(p.name)
            c = Player("Computer")
        else:
            return
    
main()