import MyModule

# word = MyModule.userString("Please Enter a Word:")
#
# for letter in word:
#    letter = letter + " "
#    print letter,
    
    
words = ['Cat','Dog','Apple', 'House', 'Chicken']

lengths = []

for word in words:
    l = len(word)
    lengths.append(l)
    
    
print "Here are the lengths %s" % lengths   