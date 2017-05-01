import MyModule

weapons = ['Candlestick','Wrench','Pipe']
suspects = ['Miss Scarlet','Col Mustard','Mr Green']

def count():
    
    c = []
    
    for weapon in weapons:
        for suspect in suspects:
            c.append("%s with a %s" % (suspect, weapon))
            
    return c        
    
def ask(c):
    
    print "%s possibilites." % len(c)
    
    game = MyModule.userString("Is the clue about a weapon or a suspect (w or s)?")
    
    if game == "w":
        
        w = MyModule.userString("Enter the weapon not used %s" % weapons).title()
        
        if any(w in x for x in c):
            
            weps = [x for x in c if w in x]
            
            for item in weps:
                
                c.remove(item)
                
    if game == "s":
    
        s = MyModule.userString("Enter the innocent suspect %s" % suspects).title()
        
        if any(s in x for x in c):
            
            susp = [x for x in c if s in x]
            
            for item in susp:
                
                c.remove(item)           
                
                
def main():
    
    start = count()
    
    while len(start) != 1:
        ask(start)
    
    print "The killer was %s" % start
        
                
main()            