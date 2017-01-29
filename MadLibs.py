import MyModule

sentence = ("In the shadowy world of spies, a/an test organization like the US "
"Government uses spies to infiltrate ADJ groups for the purpose of "
"obtaining top secret PNOUN. A teacher, CELEB, or even a little "
"old NOUN with a cane and fifteen pet NOUNP could be a spy. ")

adj1 = MyModule.userString("Enter an adjective:")
adj2 = MyModule.userString("Enter another adjective:")
nounP1 = MyModule.userString("Enter a plural noun:")
nounP2 = MyModule.userString("Enter another plural noun:")
celeb = MyModule.userString("Enter a celebrity:")
noun = MyModule.userString("Enter a noun:")

print

sentence = sentence.replace("test",adj1)
sentence = sentence.replace("ADJ",adj2)
sentence = sentence.replace("PNOUN",nounP1)
sentence = sentence.replace("NOUNP",nounP2)
sentence = sentence.replace("CELEB",celeb)
sentence = sentence.replace("NOUN",noun)

print sentence