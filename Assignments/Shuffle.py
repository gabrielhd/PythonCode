import MyModule

rank = ['Ace', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King']
suit = ['Clubs', 'Hearts', 'Diamonds', 'Spades']

def buildDeck(rank, suit):
    deck = []
    num = 0
    a = -1
    
    while num != 13:
        a = -1
        for i in suit:
            a += 1
            deck.append(("%s of %s") % (rank[num], suit[a]))
            
            if a == 3:
                num += 1
                
    return deck
    
    
def shuffle(deck):
    i = 0
    newDeck = []
    deck1 = deck[:26]
    deck2 = deck[26:]
    
    while i < len(deck1):
        newDeck.append(deck1[i])
        newDeck.append(deck2[i])
        i += 1
        
    return newDeck    
    
    
def deal(deck):
    five = deck[:5]
    
    return five

def main():
    i = 0
    mainDeck = buildDeck(rank, suit)
    userShuffle = MyModule.userInt("How many times do you want me to shuffle?")
    
    while i < userShuffle:
        mainDeck = shuffle(mainDeck)
        i += 1
    print deal(mainDeck)
    
main()    