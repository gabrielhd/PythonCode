import MyModule
    

kmWeekday = MyModule.userInt("How many km did you travel on a weekday?")
kmWeekend = MyModule.userInt("How many km did you travel on a weekend?")
miWeekday = MyModule.kmtoMi(kmWeekday)
miWeekend = MyModule.kmtoMi(kmWeekend)

dollarsWeekday = miWeekday * 0.13
dollarsWeekend = miWeekend * 0.24

print "Weekday $%.2f" % dollarsWeekday
print "Weekend $%.2f" % dollarsWeekend
print "Total $%.2f" % (dollarsWeekday + dollarsWeekend)
