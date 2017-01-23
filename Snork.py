print "Please enter a sentence:",
s1 = raw_input()

s2 = s1.replace("a" , str(len(s1)))
s3 = s2.replace("e" , str(len(s1)+1))
s4 = s3.replace("i" , str(len(s1)+2))
s5 = s4.replace("o" , str(len(s1)+3))
s6 = s5.replace("u" , str(len(s1)+4))

a2 = s1.replace(str(len(s1)), "a" )
a3 = a2.replace(str(len(s1)), "e" )
a4 = a3.replace(str(len(s1)), "i" )
a5 = a4.replace(str(len(s1)), "o" )
a6 = a5.replace(str(len(s1)), "u" )

print "The encrypted sentence is: %s" % s6
print "The decrypted sentence is: %s" % a6

