# ------------------------------------------------------
# reads the speeds in the specified file (filename)
# and returns them as a list of integers
# ------------------------------------------------------
def readData(filename):
   data = []
   file = open(filename)
   for num in file:
       data.append(int(num))
   return data
   
    
# ------------------------------------------------------    
# calculates and returns the average of the numbers
# in the the specified list (l)
# ------------------------------------------------------
def getAverage(l):
    total = float(sum(l))
    avg = total / len(l)
    return avg
# ------------------------------------------------------
# counts and returns the number of values in the 
# specified list (l) that are greater than or 
# equal to maxSpeed
# ------------------------------------------------------
def countSpeeders(l, maxSpeed):
    count = 0
    for speed in l:
        if speed > 69:
            count+=1
    return count        
    
# ------------------------------------------------------
# Determines the number of people speeding during 
# rush hour and not during rush hour.  Also determines
# the total fines during rush hour and not during 
# rush hour.  A person is considered speeding if they
# are traveling faster than 69 MPH.  The fine for 
# speeding during rush hour is $150.  The fine for 
# speeding not during rush hour is $100.
#
# THE CORRECT OUTPUT IS:
#
# The average speed during rush hour was 63.47.
# The average speed not during rush hour was 64.07.
# There were 4 speeders during rush hour.  Total fine = $600
# There were 6 speeders not during rush hour.  Total fine = $600
# ------------------------------------------------------
def main():
    
    a = readData("data-rush.txt")
    ticketA = countSpeeders(a ,69)
    avgSpeed1 = getAverage(a)
    fine1 = 150 * ticketA
    
    b = readData("data-not-rush.txt")
    ticketB = countSpeeders(b ,69)
    avgSpeed2 = getAverage(b)
    fine2 = 100 * ticketB
    
    
    print "The average speed during rush hour was %.2f MPH" % avgSpeed1
    print "The average speed not during rush hour was %.2f MPH" % avgSpeed2
    print "There were %s speeders during rush hour. Total fine = $%s" % (ticketA, fine1)
    print "There were %s speeders not during rush hour. Total fine = $%s" % (ticketB, fine2) 

# ------------------------------------------------------
# kick off the program by calling main
# ------------------------------------------------------
main()