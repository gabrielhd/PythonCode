import MyModule

def countPeople(filename):
    stage1 = []
    stage2 = []
    stage3 = []
    stage4 = []
    stage5 = []
    stage6 = []
    
    for line in open(filename):
        line = line.split(',')
        name = line[0].strip()
        time = float(line[1])
    
        if time > 0 and time <= 9.99:
            stage1.append(name)
            
        if time > 10 and time <= 19.99:
            stage2.append(name)
            
        if time > 20 and time <= 29.99:
            stage3.append(name)
            
        if time > 30 and time <= 39.99:
            stage4.append(name)
            
        if time > 40 and time <= 59.99:
            stage5.append(name)
            
        if time > 60:
            stage6.append(name)    
        
    return stage1, stage2, stage3, stage4, stage5, stage6

def rankings(d):
    
    
    print "Cube Head (0-99):"
    for rank in d[0]:
        print rank
    print "\nSquare Master (10-19.99)"
    for rank in d[1]:
        print rank
    print "\nAdvanced Master (20-29.99)"
    for rank in d[2]:
        print rank
    print "\nIntermediate Turner (30-39.99)"
    for rank in d[3]:
        print rank
    print "\nAverage Mover (40-59.99)"
    for rank in d[4]:
        print rank
    print "\nPathetic (60 and beyond)"
    for rank in d[5]:
        print rank
    

def main():
  a =  countPeople("timings.txt")
  rankings(a)
  
  
  
main()