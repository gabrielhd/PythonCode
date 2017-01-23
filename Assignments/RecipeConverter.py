#######################
# Recipe Converter    #
#                     #
# Gabriel H           #
#                     #
# 1/22/17             #
#######################

print "--Original Recipe--"

print "Enter the amount of flour (cups):",
flour = raw_input()

print "Enter the amount of water (cups):",
water = raw_input()

print "Enter the amount of salt (teaspoons):",
salt = raw_input()

print "Enter the amount of yeast (teaspoons):",
yeast = raw_input()

print "Enter the loaf adjustment factor (eg. 2.0 double the size):",
tweak = raw_input()
print ""
print "--Modified Recipe--"

print "Flour: %.2f cups." % (float(flour) * float(tweak)) 
print "Water: %.2f cups." % (float(water) * float(tweak)) 
print "Salt: %.2f teaspoons." % (float(salt) * float(tweak))
print "Yeast: %.2f teaspoons." % (float(yeast) * float(tweak))
print ""

print "--Modified Recipe (in Grams)--";

print "Flour: %.2f grams." % ((float(flour) * float(tweak)) * 120)
print "Water: %.2f grams." % ((float(water) * float(tweak)) * 237)
print "Salt: %.2f grams." % ((float(salt) * float(tweak)) * 5)
print "Yeast: %.2f grams." % ((float(yeast) * float(tweak)) * 3)