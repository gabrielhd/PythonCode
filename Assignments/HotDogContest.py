import MyModule
import random
import time

def people():
    tom = 0
    sally = 0
    fred = 0
    winner = ""
    
    keepGoing = True
    
    while keepGoing:
        person1 = random.randrange(1, 8)
        person2 = random.randrange(1, 8)
        person3 = random.randrange(1, 8)
        
        tom += person1
        sally += person2
        fred += person3
        
        print "\nnom... nom... nom..."
        time.sleep(1)
        print "\nTom has eaten %s hot dogs!" % tom
        print "Sally has eaten %s hot dogs!" % sally
        print "Fred has eaten %s hot dogs!" % fred
        
        if tom >= 49:
            winner = "Tom"
            keepGoing = False
        if sally >= 49:
            winner = "Sally"
            keepGoing = False
        if fred >= 49:
            winner = "Fred"
            keepGoing = False    
        
    return winner

def guess():
    
    pick = MyModule.userString("Pick a winner (Tom, Sally, Fred)")
    print "Ready, set, eat!"
    w = people()
    
    if pick == w:
        print "\nYou guessed right, %s wins!" % w
    else:
        print "\nYou guessed wrong, %s is the winner." % w
    
    
        
        
def main():
    guess()
    
main()        
        
        
    
    
    