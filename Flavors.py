import MyModule

ratings = []
flavors = ['vanilla','chocolate','strawberry','bacon']

for flavor in flavors:
    rating = MyModule.userString("Rate %s from 1 to 5:" % flavor)
    #ratings = ratings + ["%s as a %s" % (flavor, rating)]
    ratings.append("%s as a %s" % (flavor, rating))
    

 
print ratings    