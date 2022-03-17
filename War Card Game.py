#!/usr/bin/env python
# coding: utf-8

# In[7]:


#####################################
### WELCOME TO YOUR OOP PROJECT #####
#####################################

# For this project you will be using OOP to create a card game. This card game will
# be the card game "War" for two players, you an the computer. If you don't know
# how to play "War" here are the basic rules:
#
# The deck is divided evenly, with each player receiving 26 cards, dealt one at a time,
# face down. Anyone may deal first. Each player places his stack of cards face down,
# in front of him.
#
# The Play:
#
# Each player turns up a card at the same time and the player with the higher card
# takes both cards and puts them, face down, on the bottom of his stack.
#
# If the cards are the same rank, it is War. Each player turns up three cards face
# down and one card face up. The player with the higher cards takes both piles
# (six cards). If the turned-up cards are again the same rank, each player places
# another card face down and turns another card face up. The player with the
# higher card takes all 10 cards, and so on.
#
# There are some more variations on this but we will keep it simple for now.
# Ignore "double" wars
#
# https://en.wikipedia.org/wiki/War_(card_game)

from random import shuffle

# Two useful variables for creating Cards.
SUITE = 'H D S C'.split()
RANKS = '2 3 4 5 6 7 8 9 10 J Q K A'.split()

class Deck:     
    """
    This is the Deck Class. This object will create a deck of cards to initiate
    play. You can then use this Deck list of cards to split in half and give to
    the players. It will use SUITE and RANKS to create the deck. It should also
    have a method for splitting/cutting the deck in half and Shuffling the deck.
    """
    def __init__(self):
        self.deck=[]
        for rank in RANKS:
            for suite in SUITE:
                self.deck.append({'suite':suite,'rank':rank})
    def split(self):
        """This splits the deck in 2."""
        self.deck = (self.deck[0:26], self.deck[26:])
    def mix(self):
        shuffle(self.deck)
    

class Hand:
    '''
    This is the Hand class. Each player has a Hand, and can add or remove
    cards from that hand. There should be an add and remove card method here.
    '''
    def __init__(self, hand):
        self.hand=hand
        
    def add(self, card):
        '''Adds card to the bottom of the hand when the player wins a round.'''
        self.hand.insert(0,card)
        
    def remove(self):
        '''Removes the last card of the hand.'''
        if len(self.hand) > 0:
            return self.hand.pop(-1)
        
    

class Player:
    """
    This is the Player class, which takes in a name and an instance of a Hand
    class object. The Payer can then play cards and check if they still have cards.
    """
    def __init__(self, name, hand):
        self.name = name
        self.hand = hand
    


######################
#### GAME PLAY #######
######################


"""Get Player Names"""
player1Name = input('Enter Player 1 Name:')
player2Name = input('Enter Player 2 Name:')

"""Initialise Objects"""
deck = Deck()
deck.mix()
deck.split()
player1 = Player(player1Name, Hand(deck.deck[0]))
player2 = Player(player2Name, Hand(deck.deck[1]))
tieDeck = []


"""Start and loop through game until there is a winner"""
print("Welcome to War, let's begin...")
"""Take one card from each player and see which is highest. 
Player with the highest card takes both cards and adds it to the bottom of their deck."""

def cardPlay():
#     print("player 1 has "+ str(len(player1.hand.hand)) + " cards.")
#     print("player 2 has "+ str(len(player2.hand.hand)) + " cards.")
#     print("tieDeck has "+ str(len(tieDeck)) + " cards.")
    card1 = player1.hand.remove()
    card2 = player2.hand.remove()

        
    
#     print(player1.name + "'s card is: " + card1['suite'] + str(card1['rank']))
#     print(player2.name + "'s card is: " + card2['suite'] + str(card2['rank']))

    for card in [card1, card2]:
        if card['rank'] in ['J','Q', 'K', 'A']:
            for letter in [['J', 11], ['Q', 12],['K', 13],['A', 14]]:
                if card['rank'] == letter[0]:
                    card['rank'] = letter[1]
  
    if int(card1['rank']) == int(card2['rank']):
#         print("It's a tie!")
        tieDeck.append(card1)
        tieDeck.append(card2)
        for x in range(3):
            tieDeck.append(player1.hand.remove())
            tieDeck.append(player2.hand.remove())
        
        if len(player1.hand.hand) != 0 and len(player2.hand.hand) !=0 :
            cardPlay()
            
    elif int(card1['rank']) > int(card2['rank']):
        player1.hand.add(card1)
        player1.hand.add(card2)
        if len(tieDeck) > 0:
            for card in tieDeck:
                player1.hand.add(card)
            tieDeck.clear()
                
#         print("player 1 won round.")
#         print("player 1 has "+ str(len(player1.hand.hand)) + " cards.")
#         print("player 2 has "+ str(len(player2.hand.hand)) + " cards.")
    else:
        player2.hand.add(card1)
        player2.hand.add(card2)
        if len(tieDeck) > 0:
            for card in tieDeck:
                player2.hand.add(card)
            tieDeck.clear()
       
#         print("player 2 won round.")
#         print("player 1 has "+ str(len(player1.hand.hand)) + " cards.")
#         print("player 2 has "+ str(len(player2.hand.hand)) + " cards.")
        
while len(player1.hand.hand) > 0 and len(player2.hand.hand) > 0:
#     print('NEW ROUND')
    cardPlay()   
    
    if len(player1.hand.hand) == 0:
        winner = player1
    
    if len(player2.hand.hand) == 0:
        winner = player2
        
print(winner.name + " has won the game!")



# Use the 3 classes along with some logic to play a game of war!


# In[ ]:




