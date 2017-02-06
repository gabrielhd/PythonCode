# reads the temps from the file
# and returns them in a list
def readTemps():
   data = []
   file = open('temps.txt')
   for line in file:
      numbers = line.split(" ")
      data = data + [float(line)]
   return data
   


# calculates the average of a range of numbers
# as specified by start (inclusive) and stop (inclusive)
def calculateAve(data, start, stop): # 0-80 temps
    totals = 0
    randomS = 81
    for num in range(start, stop):
      totals = totals + data[num]
      
      if stop > 81:
         randomS = 35
    avg = totals / randomS
    return avg
          
       
# counts all values that have a positive deviation
# in the range as specified by start (inclusive) 
# and stop (inclusive)
def count(data, start, stop):
    count = 0   
    for pos in range(start, stop):
       
       if data[pos] > 0:
          count+=1
    return count
      
# main function
# the data represent the deviation in global surface
# temperature relative to 1951-1980 average temperatures.
def main():
   
   temps = readTemps()
   then = calculateAve(temps,0,81)
   now = calculateAve(temps,81,116)
   posThen = count(temps,0,81)
   posNow = count(temps,81,116)
   print "During the first 81 years, the average deviation from the temperature anomaly is %s" % then
   print "During the first 81 years, %s had a positive temperature anomaly" % posThen
   print "During the first 35 years, the average deviation from the temperature anomaly is %s" % now
   print "During the first 35 years, %s had a positive temperature anomaly" % posNow
main()    
    
    
    