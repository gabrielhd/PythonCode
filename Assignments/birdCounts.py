# ------------------------------------------------------------
# For a badge do the following:
#
# After each user query print out the bird that has been seen 
# most often.  If there is a tie, print all of birds that are 
# tied for most sightings.
#
# Allow the user to enter a bird name as often as they like.
# When they want to stop entering bird names they can type 
# 'Exit'.
#
# Make the lookup case insensitive.  In other words, I should
# be able to type ROBIN or RoBiN and get the count for Robin.
# ------------------------------------------------------------

# ------------------------------------------------------------
# Reads the specified file (filename) and returns a dictionary 
# whose keys are bird names and whose values are the number of 
# times the bird has been seen.
# ------------------------------------------------------------
import MyModule

def countBirds(filename):
    birds = {}
    for line in open(filename):
        line = line.split(', ')
        name = line[0]
        seen = int(line[1])
        
        if name not in birds:
            birds[name] = seen
        else:
            birds[name] += seen
    return birds
# ------------------------------------------------------------
# Asks the user to enter a bird name and then looks up 
# the sighting count for that bird in the specified 
# dictionary (d).
# ------------------------------------------------------------
def askUser(d):
    user = MyModule.userString("Enter a bird name:",)
     
    if user in d:
        num = d[user]
        
    elif user not in d:
        num = 0
    
    print "\nI have seen that bird %s time(s)" % num

def main():
   data = countBirds("Birds.txt")
   askUser(data)
    
main()