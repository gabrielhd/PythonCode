import MyModule
import random

choices = ['bird','dog','snake','fish','cat','mouse','starfish','woodchuck','crab']
deck = [0,1,2,3,4,5,6,7,8,5]

def cards():
    random.shuffle(choices)
    random.shuffle(deck)
    
    return choices, deck
    
def user(a):
    counter = 0
    match = False
    
    while match == False:
        choice1 = MyModule.userInt("Pick the first card to turn over (0-9)")
        choice2 = MyModule.userInt("Pick the second card to turn over (0-9)")
        print "Card %s is a %s" % (choice1, choices[deck[choice1]])
        print "Card %s is a %s" % (choice2, choices[deck[choice2]])
        counter+= 1
        
        if choice1 == choice2 or choice1 < 0 or choice2 < 0:
            print "Invalid choice. You must pick a card 0-9"

        
        elif choices[deck[choice1]] == choices[deck[choice2]]:
            print "You win! It took you %s tries" % counter
            match = True
        
def main():
    user(cards()) 
    
main()    
    
    
    