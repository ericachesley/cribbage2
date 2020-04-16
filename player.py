"""
Cribbage2
Erica Chesley
https://github.com/ericachesley/cribbage2

Cribbage game program written for Hackbright Academy Phenomenal Women Scholarship application.
Run from main.py; see README.txt for more information.
"""

import time
from constants import PRINT_SPEED

class Player:
    def __init__(self, name):
        self.hand = []
        self.played = []
        self.score = 0
        self.name = name
        self.pairs = []

    #check if hand has anything that can be played
    def checkHand(self, rnd, deck):
        for card in self.hand:
            if rnd.count + card.value <= 31:
                return True
        return False
    
    #print cards with proper formatting
    def printCards(self, cards):
        for card in cards:
            if card == cards[-1]:
                print ("|",card.rank,card.suit,"| ")
            else:
                print ("|",card.rank,card.suit, end=" ")

    #print hand - no arguments needed
    def printHand(self):
        self.printCards(self.hand)
        
    #check if player has won to interrupt game flow
    def checkWin(self, rnd):
        if self.score >= rnd.winningScore:
            rnd.gameOver = True
        
    #scoring during play phase & go phase
    def updateScorePlay(self, rnd, deck):
        #count 15
        if rnd.count == 15:
            self.score += 2
            time.sleep(PRINT_SPEED)
            print("**15!**")
        #2-3-4 of a kind
        if deck.checkPair():
            deck.setLength += 1
            if deck.setLength >= 4:        #set of 4
                self.score += 12
                time.sleep(PRINT_SPEED)
                print("**Four of a Kind!**")
            elif deck.setLength >= 3:      #set of 3
                self.score += 6
                time.sleep(PRINT_SPEED)
                print("**Three of a Kind!**")
            else:                          #pair
                self.score += 2
                time.sleep(PRINT_SPEED)
                print("**Pair!**")
        else:
            deck.setLength = 1             #if doesn't match previous card, reset setLength
        #run
        for i in range(5, 2, -1):
            if deck.checkRunLastN(i):
                self.score += i
                time.sleep(PRINT_SPEED)
                print("**Run of ", i, "!**")
                break
        self.checkWin(rnd)

    #scoring during count phase - score player hand, then crib if player is dealer
    def countCombinations(self, rnd, deck, isDealer):
        #score player
        time.sleep(PRINT_SPEED)
        print("\nStarter: |",rnd.starter.rank,rnd.starter.suit,"| ")
        print(self.name, "'s hand: ", end="")
        self.printCards(self.played)
        print("\n", self.name, "'s combinations")
        self.updateScoreCount(rnd, deck, False)
        time.sleep(PRINT_SPEED)
        rnd.printScores()
        if rnd.gameOver:
            return
        input("[Enter to proceed] ")
        print ("\n-----------")
        #score crib
        if isDealer:
            time.sleep(PRINT_SPEED)
            print("\nStarter: |",rnd.starter.rank,rnd.starter.suit,"| ")
            print ("Crib: ", end="")
            self.printCards(rnd.crib)
            time.sleep(PRINT_SPEED)
            print ("\nCrib combinations")
            self.updateScoreCount(rnd, deck, True)
            time.sleep(PRINT_SPEED)
            rnd.printScores()
            input("[Enter to proceed] ")
    
    #helper function for combination count scoring
    def updateScoreCount(self, rnd, deck, isCrib):
        if isCrib:
            cards = rnd.crib
        else:
            cards = self.played
        
        count = 0
        starter = rnd.starter

        cards.append(starter)
        #15s
        count = self.count15s(cards, count)
        #pairs
        count = self.countPairs(cards, count)
        #runs
        count = self.countRuns(cards, count, deck)

        cards.remove(starter)
        #flush
        count = self.countFlush(cards, count, starter, isCrib)
        #his nobs
        count = self.checkHisNobs(cards, count, starter)
                
        self.score += count
        self.checkWin(rnd)
        print("")

    """
    Helper functions for updateScoreCount()
    Each function below prints combinations as they are found and returns updated score count.
    """

    def count15s(self, cards, count):
        cards = sorted(cards, key=lambda x:x.value)
        #from 2 cards
        for i in range(0, len(cards)-1):
            for j in range(i+1, len(cards)):
                if cards[i].value+cards[j].value==15:
                    count += 2
                    time.sleep(PRINT_SPEED)
                    print ("Fifteen for",count, "- ",end="")
                    self.printCards([cards[i], cards[j]])
        #from 3 cards
        for i in range(0, len(cards)-2):
            for j in range(i+1, len(cards)-1):
                for k in range(j+1, len(cards)):
                    if cards[i].value+cards[j].value+cards[k].value==15:
                        count += 2
                        time.sleep(PRINT_SPEED)
                        print ("Fifteen for",count, "- ",end="")
                        self.printCards([cards[i], cards[j], cards[k]])
        #from 4 cards
        for i in range(0, len(cards)-3):
            for j in range(i+1, len(cards)-2):
                for k in range(j+1, len(cards)-1):
                    for l in range(k+1, len(cards)):
                        if cards[i].value+cards[j].value+cards[k].value+cards[l].value==15:
                            count += 2
                            time.sleep(PRINT_SPEED)
                            print ("Fifteen for",count, "- ",end="")
                            self.printCards([cards[i], cards[j], cards[k], cards[l]])
        #from 5 cards
        for i in range(0, len(cards)-4):
            for j in range(i+1, len(cards)-3):
                for k in range(j+1, len(cards)-2):
                    for l in range(k+1, len(cards)-1):
                        for m in range(l+1, len(cards)):
                            if cards[i].value+cards[j].value+cards[k].value+cards[l].value+cards[m].value==15:
                                count += 2
                                time.sleep(PRINT_SPEED)
                                print ("Fifteen for",count, "- ",end="")
                                self.printCards([cards[i], cards[j], cards[k], cards[l], cards[m]])
        return count

    def countPairs(self, cards, count):
        cards = sorted(cards, key=lambda x:x.equiv)
        self.pairs = []
        for i in range(0,len(cards)-1):
            for j in range(i+1, len(cards)):
                if cards[i].rank == cards[j].rank:
                    count += 2
                    time.sleep(PRINT_SPEED)
                    print ("Pair for",count, "- ",end="")
                    self.printCards([cards[i], cards[j]])
                    self.pairs.append(cards[j])
        return count

    def countRuns(self, cards, count, deck):
        cards = sorted(cards, key=lambda x:x.equiv)
        found = False
        #of 5
        if deck.checkRun(cards):
            count = self.printRun(cards, count, 5)
            found = True
        #of 4
        if found == False:
            if len(self.pairs) == 0:
                for i in range(2):
                    if deck.checkRun(cards[i:i+4]):
                        count = self.printRun(cards[i:i+4], count, 4)
                        found = True
            elif len(self.pairs) == 1:
                #remove duplicate
                index = cards.index(self.pairs[0])
                cards.pop(index)
                if deck.checkRun(cards):
                    count = self.printRun(cards, count, 4)
                    #swap duplicate
                    cards.insert(index, self.pairs[0])
                    held = cards.pop(index-1)
                    count = self.printRun(cards, count, 4)
                    #return duplicate
                    cards.insert(index-1, held)
                    found = True
                else:
                    #return duplicate
                    cards.insert(index, self.pairs[0])
        #of 3
        if found == False:
            if len(self.pairs) == 0:
                for i in range(3):
                    if deck.checkRun(cards[i:i+3]):
                        count = self.printRun(cards[i:i+3], count, 3) 
            elif len(self.pairs) == 1:
                #remove duplicate
                index = cards.index(self.pairs[0])
                cards.pop(index)
                for i in range(2):
                    if deck.checkRun(cards[i:i+3]):
                        count = self.printRun(cards[i:i+3], count, 3)
                        #check if pair is part of run
                        for j in range(3):
                            if cards[i+j].rank == self.pairs[0].rank:
                                #swap out match and print 2nd run
                                held = cards.pop(i+j)
                                cards.insert(i+j, self.pairs[0])
                                count = self.printRun(cards[i:i+3], count, 3)
                                #swap pair back
                                cards.remove(self.pairs[0])
                                cards.insert(i+j, held)
                #return duplicate
                cards.insert(index, self.pairs[0])
            elif len(self.pairs) == 2:
                #remove duplicates
                index0 = cards.index(self.pairs[0])
                index1 = cards.index(self.pairs[1])
                cards.pop(index1)
                cards.pop(index0)
                if deck.checkRun(cards):
                    #run w/triple
                    if self.pairs[0].rank == self.pairs[1].rank:
                        count = self.printRun(cards, count, 3) 
                        #swap out matching cards
                        cards.insert(index0, self.pairs[0])
                        held = cards.pop(index0-1)
                        count = self.printRun(cards, count, 3) 
                        #swap out matching cards
                        cards.insert(index0, self.pairs[1])
                        cards.pop(index0-1)
                        count = self.printRun(cards, count, 3) 
                        #put back duplicates
                        cards.insert(index0-1, held)
                        cards.insert(index0, self.pairs[0])
                    #run w/two different pairs
                    else:
                        count = self.printRun(cards, count, 3) 
                        #swap first pair
                        cards.insert(index0, self.pairs[0])
                        held0 = cards.pop(index0-1)
                        count = self.printRun(cards, count, 3) 
                        #swap second pair
                        cards.insert(index1-1, self.pairs[1])
                        held1 = cards.pop(index1-2)
                        count = self.printRun(cards, count, 3) 
                        #swap first pair back
                        cards.insert(index0-1, held0)
                        cards.pop(index0)
                        count = self.printRun(cards, count, 3) 
                        #put back duplicates
                        cards.insert(index0, self.pairs[0])
                        cards.insert(index1-1, held1)
        return count

    #helper for countRuns() function
    def printRun(self, cards, count, n):
        count += n
        time.sleep(PRINT_SPEED)
        print ("Run of", n, "for", count, "- ", end="")
        self.printCards(cards)
        return count

    def countFlush(self, cards, count, starter, isCrib):
        cards = sorted(cards, key=lambda x:x.suit)
        if cards[0].suit == cards[-1].suit:
            if cards[0].suit == starter.suit:
                count += 5
                time.sleep(PRINT_SPEED)
                print ("Five card flush for", count, "- ", end="")
                self.printCards(cards + [starter])
            #four card flush does not count for crib, or with starter
            elif not isCrib:
                count += 4
                time.sleep(PRINT_SPEED)
                print ("Four card flush for", count, "- ", end="")
                self.printCards(cards)
        return count

    #His nobs = Jack of same suit as starter in hand
    def checkHisNobs(self, cards, count, starter):
        for i in range(len(cards)):
            if cards[i].rank == "J" and cards[i].suit == starter.suit:
                count += 1
                time.sleep(PRINT_SPEED)
                print ("His nobs (Jack of same suit as starter) for", count)
        return count
        

            