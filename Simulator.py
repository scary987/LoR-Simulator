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
        self.draw(5)
        self.mana=0
        self.spellmana=0
    
        self.options=["pass","play"]

        print(self)

    '''
    Example Usage of **kwargs will be:
    target as []




    '''



    def play(self,card,**kwargs):
            if card.Type== "Unit":
                self.mana-=card.cost
                self.hand.remove(card)
                self.board.append(card)
                
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
            
class board:
    side1={}
    side2={}


    def __init__(self):
        self.side1={}
        self.side2={}


class State:
    seed= 0
    eos=False
    Burst=[]
    Fast=[]
    player1=None
    player2=None
    board=board() # 
    history=[]
    graveyard=[]
    turn=0
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
        if kwargs["Turn"]%2==0:
            self.player2.attack_token=True
        else:
            self.player2.attack_token=True

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
simulator= State("CEAAABAUAEAAOCIKBMGA6FIWDIOSCJJGE4VS2MRTGQ3AYAIDB4IRGFAYDYQSMKBPGA3QMAQAAEBQOCAJBIBAEAYEAU","CEBAGAIDCQRSOCQBAQAQYDISDQTCOKBNGQAACAIBAMFQ",seed)


        

