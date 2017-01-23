print "How many malcorps did you find on planet Exflon?", 
planet1 = raw_input()

print "How many malcorps did you find on planet Mobiles?", 
planet2 = raw_input()

print "How many malcorps did you find on planet Monsantoes?", 
planet3 = raw_input()

total = int(planet1)+ int(planet2)+ int(planet3)

print "You found %s malcorps!" % total 
print "The average malcorps per planet is %.2f" % (total/3.0) 
