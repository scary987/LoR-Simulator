from twisted_fate import Deck,Card
import random

class Player:
    attack_token = False
    def __init__(self,name,deckcode):
        self.name=name
        self.deckcode=deckcode
        self.deck = Deck.decode(deckcode).cards
        self.health=20
        self.hand=[]
        self.board=[]
        random.shuffle(self.deck)
        self.draw(9)
        self.mana=0
        self.spellmana=0
        

        print(self)

    '''
    Example Usage of **kwargs will be:
    target as []




    '''

    def summon(self,card,**kwargs):
        self.board.append(card)
        #here should be a dict of functions or something


    def play(self,card,**kwargs):
            if card.Type== "Unit":
                self.mana-=card.cost
                self.hand.remove(card)
                if "Play" in card.keywords:
                    Play(card)
                summon(card)
                
            if card.Type== "Spell":
                self.hand.remove(card)
                #self.fast.append(card)
                pass # query card effect






        

    def __str__(self):
        temp = ""
        for i in self.hand:
            temp+=str(i.cost)+": "+i.name+" "+i.cardType+" "+i.subType+i.spellSpeedRef+ str(i.keywords) +"\n"
        return str(self.name)+str(self.health)+"\n"+temp+"\n"

    def draw(self,amount):
        for i in range(amount):
            self.hand.append(self.deck.pop(0)) #takes first and adds to hand
         