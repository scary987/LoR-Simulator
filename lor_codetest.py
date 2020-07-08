from twisted_fate import Deck,Card

draven_deck = Deck.decode("CEBAGAIDCQRSOCQBAQAQYDISDQTCOKBNGQAACAIBAMFQ")
chase_deck = Deck.decode("CEAAABAUAEAAOCIKBMGA6FIWDIOSCJJGE4VS2MRTGQ3AYAIDB4IRGFAYDYQSMKBPGA3QMAQAAEBQOCAJBIBAEAYEAU")
# results
print(draven_deck,type(draven_deck))
print(chase_deck)
card = chase_deck.cards[5]
print(card,"\n", card.count, card.cost,"\n", card.health,card.attack)
#[
#    Card(01NX020, Name: Draven, Cost: 3), 
#    Card(01NX035, Name: Draven's Biggest Fan, Cost: 1), 
#    Card(01NX039, Name: Vision, Cost: 3), 
#    Card(01PZ001, Name: Rummage, Cost: 1), 
#    Card(01PZ012, Name: Flame Chompers!, Cost: 2), 
#    Card(01PZ013, Name: Augmented Experimenter, Cost: 6), #    Card(01PZ018, Name: Academy Prodigy, Cost: 2), 
#    Card(01PZ028, Name: Jury-Rig, Cost: 1), 
#    Card(01PZ038, Name: Sump Dredger, Cost: 2), 
#    Card(01PZ039, Name: Get Excited!, Cost: 3), 
#    Card(01PZ040, Name: Jinx, Cost: 4), 
#    Card(01PZ045, Name: Zaunite Urchin, Cost: 1), 
#    Card(01PZ052, Name: Mystic Shot, Cost: 2), 
#    Card(01NX011, Name: Whirling Death, Cost: 3)
# ]
