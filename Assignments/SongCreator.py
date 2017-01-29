import MyModule

songs = []
verses = ['first','second','third','fourth']

for verse in verses:
    song = MyModule.userString("Enter the %s verse:" % verse)
    songs = songs + ["%s" % (song)] 
    
chorus = MyModule.userString("Enter the chorus:") + " "
chorusNum = MyModule.userInt("Enter the chorus repeat:")
 
 
songs.insert(1, chorus * chorusNum) 
songs.insert(3, chorus * chorusNum)
songs.insert(5, chorus * chorusNum)
songs.insert(7, chorus * chorusNum + chorus)
songs = songs * 2
songs.insert(8, "...One more time...") 
 
print songs

print ""

for lines in songs:
    print lines
