from twisted_fate import Deck,Card
import random
from Player import Player
from BoardState import *


def mana_filter(per, mana):
    temp= 0
    for i in per:
        temp+=i.cost
        if temp>mana:
            return False
    return True

def board_filter(per,re_boardsize):
    temp =0
    for i in per:
        #print(i.cardType)
        if i.cardType=="Unit":
            temp+=1
            if temp>re_boardsize:
                return False
    return True
class Client:


    def __init__(self,hand,Board,opBoard,mana):
        '''You should only filter if you have an extremely high of combinations plus low cost cards, good luck tf decks

        2nd step: build a tree out of possible permutations and simulate changes
        


        '''




        temp=[]
        for i in range(len(hand)):
            temp.extend(list(permutations(hand,i)))
        print('All Permutations:',len(temp))
        temp = list(filter(lambda per: mana_filter(per,mana),temp))
        print('Filtered Permutations ',len(temp))
        re_boardsize=7-len(Board)
        if re_boardsize<4:
            temp = list(filter(lambda per: board_filter(per,re_boardsize),temp))
        print('Filtered yet again ',len(temp))