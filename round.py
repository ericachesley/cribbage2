"""
Cribbage2
Erica Chesley
https://github.com/ericachesley/cribbage2

Cribbage game program written for Hackbright Academy Phenomenal Women Scholarship application.
Run from main.py; see README.txt for more information.
"""

import random
import time

from constants import PRINT_SPEED

class Round:
    def __init__(self, dealer, person, computer, winningScore):
        self.count = 0
        self.crib = []
        self.starter = None
        self.players = [person, computer]
        self.up = self.players[abs(self.players.index(dealer)-1)]
        self.winningScore = winningScore
        self.gameOver = False
        self.thirtyone = False
        
    #prompt player to add two cards from hand to crib, then randomly select two cards from computer hand as well
    def makeCrib(self, person, computer, firstCrib):
        print("\n--------------- Make the crib ---------------")
        while (len(self.crib) < 2):
            time.sleep(PRINT_SPEED*.5)
            print("\nYour hand: ", end="")
            person.printHand()
            if firstCrib:
                cardPosition = input("Which card position (counting from 1) in your hand would you like to put in the crib? ")
            else:
                cardPosition = input("Which card position in your hand would you like to put in the crib? ")
            try:
                card = person.hand.pop(int(cardPosition)-1)
            except ValueError:
                print("\nPlease choose an integer value.")
                continue
            except IndexError:
                print("\nYour choice is out of range. Please try again.")
                continue
            self.crib.append(card)

        print("\nComputer adding to crib.")
        while (len(self.crib) < 4):
            card = computer.hand.pop(random.randint(0, len(computer.hand)-1))
            self.crib.append(card)

        time.sleep(PRINT_SPEED)
        print("Crib complete.")

    #draw the starter and display it
    def drawStarter(self, deck):
        self.starter = deck.draw()
        time.sleep(PRINT_SPEED)
        print("\nStarter: |",self.starter.rank,self.starter.suit,"| ")
    
    #play phase - alternate player turns until one player can no longer make a legal move
    def play(self, person, computer, deck, teacher):
        self.thirtyone = False
        time.sleep(PRINT_SPEED)
        print("\n----------- Play -----------")
        go = False
        deck.setLength = 1
        deck.played = []
        self.count = 0
        while not go:
            if self.up.checkHand(self, deck):       #current player is able to play
                self.turn(self.up, deck)
                if self.gameOver:
                    return
                time.sleep(PRINT_SPEED)
                print ("Total count:", self.count)
                if self.count == 31:
                    self.up.score += 2
                    time.sleep(PRINT_SPEED)
                    print(self.up.name, "made 31!\n")
                    self.thirtyone = True
                self.printScores()
                self.up.checkWin(self)
                if self.gameOver:
                    return
            else:                                   #current player is not able to play
                go = True
                if not self.thirtyone:
                    print("\n", self.up.name, "says 'Go' (can't play).")
                input("[Enter to proceed.] ")
            self.turnSwitch()
    
    #go phase - player who did not call 'go' gets unlimited turns as long as they are able to play
    def go(self, person, computer, deck):
        if self.thirtyone:
            self.turnSwitch()
            return
        self.up.score += 1
        self.up.checkWin(self)
        if self.gameOver:
            return
        print("\n------------ Go ------------\n")
        time.sleep(PRINT_SPEED)
        print ("Total count:", self.count)
        time.sleep(PRINT_SPEED)
        self.printScores()
        while self.up.checkHand(self, deck):
            self.turn(self.up, deck)
            time.sleep(PRINT_SPEED)
            print ("Total count:", self.count)
            time.sleep(PRINT_SPEED)
            if self.count == 31:
                self.up.score += 1
                time.sleep(PRINT_SPEED)
                print(self.up.name, "made 31!\n")
                self.up.checkWin(self)
                if self.gameOver:
                    return
            self.printScores()
        if self.count < 31:
            print("\n", self.up.name, "can't play.")
        self.turnSwitch()
        input("[Enter to proceed.] ")
            
    #single turn - helper for play() and go() functions
    def turn(self, player, deck):
        while True:
            #pick a card to play
            if player.name != "Computer":
                print("")
                time.sleep(PRINT_SPEED)
                print("Your hand: ", end="")
                player.printHand()
                index = input("Which card position in your hand would you like to play? ")
                try:
                    index = int(index)-1
                except ValueError:
                    print("\nPlease choose an integer value.")
                    continue
            else:
                index = random.randint(0, len(player.hand)-1)
                
            #check if card is playable
            if index not in range(0, len(player.hand)):
                print("\nInvalid selection. Please try again. Count begins with 1.")
            elif self.count + player.hand[index].value <= 31:
                card = player.hand.pop(index)
                print("\n", player.name, "played |",card.rank,card.suit,"| ")
                self.count += card.value
                player.played.append(card)
                deck.played.append(card)
                player.updateScorePlay(self, deck)      #check for any scoring opportunties (15s, pairs, runs, etc.)
                return
            elif player.name != "Computer":
                print ("\nThat card is not playable at this time. Please try again.")
              
    #change which player's turn it is  
    def turnSwitch(self):
        self.up = self.players[abs(self.players.index(self.up)-1)]

    #print the current scores for both players
    def printScores(self):
        print (self.players[0].name, "'s score:", self.players[0].score, " ~  Computer 's score:", self.players[1].score)
        time.sleep(PRINT_SPEED)



    