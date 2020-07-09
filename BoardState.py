from twisted_fate import Deck,Card
import random
from Player import Player
from itertools import permutations
from Client import *
   






class State:
    seed= 0
    eos=False
    Burst=[]
    Fast=[]
    player1=None
    player2=None
    history=[]
    graveyard=[]
    Turn=0
    

    def init_turn(self,Turn):
        self.player1.mana=Turn
        self.player2.mana=Turn
        self.player1.draw(1)
        self.player2.draw(1)
        self.player1.hand.sort(key=lambda card: card.cost)
        self.player2.hand.sort(key=lambda card: card.cost)
        player1 = self.player1
        self.Client = Client(player1.hand,player1.board,self.player2.board,10)

    def printboard(self): #prints current state of minions of a player
        for i in range (max(len(self.player1.board),len(self.player2.board))):
            print("-----")
            temp = ""
        for i in self.player1.board:
            temp+="| ",i.health," ",i.attack ," |"
            print(temp)
            temp =""
        for i in self.player2.board:
            temp+="| ",i.health," ",i.attack ," |"
            print(temp)
        for i in range (max(len(self.player1.board),len(self.player2.board))):
            print("-----")
    def is_eos(self):
        self.eos =True 

    def __init__(self,deckcode1,deckcode2,seed,**kwargs):
        random.seed(5)
        self.player1=Player("Nodbody",deckcode1)
        self.player2=Player("Nodbody2",deckcode2)
        if 'Turn' in kwargs.keys():

            if kwargs['Turn']%2==1:
                self.player2.attack_token=True
            else:
                self.player1.attack_token=True
            self.Turn=1+kwargs['Turn']
        else:
            self.player1.attack_token=True
            self.Turn = 0
        self.init_turn(self.Turn)
        
    def trigger_lw(self,*args): #trigger dying effect
        pass
    def damage_calc(self,index,**kwargs):
        for i in range(7):
            self.strike_each_other(self.board.side1[i],self.board.side2[i])
            if self.board.side1[i].health<=0:
                self.graveyard.append(self.board.side1[i])
                self.trigger_lw(self.board.side1[i])
                del(self.board.side1[i])
            if self.board.side2[i].health<=0:
                self.graveyard.append(self.board.side2[i])
                self.trigger_lw(self.board.side2[i])
                del(self.board.side2[i])


    def strike(self,unit,target):
        self.dd_to(target,unit.attack)
    def strike_each_other(self,unit1,unit2):
        self.strike(unit1,unit2)
        self.strike(unit2,unit1)

    def dd_to(self,target,amount):
        target.health-=amount
        if type(self.player1)==type(target) and target.health<=0: #if target is a player end the game
            self.is_eos()
 
seed =28
simulator= State("CEAAABAUAEAAOCIKBMGA6FIWDIOSCJJGE4VS2MRTGQ3AYAIDB4IRGFAYDYQSMKBPGA3QMAQAAEBQOCAJBIBAEAYEAU","CEBAGAIDCQRSOCQBAQAQYDISDQTCOKBNGQAACAIBAMFQ",seed,Turn=3)


        

