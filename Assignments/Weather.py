import MyModule
import json
import urllib2

def weatherAPI():

    city = MyModule.userString("\nPlease enter a zipcode or city name:")
    url = 'https://api.apixu.com/v1/current.json?key=0acf9807210e4f2eb6211338172304&q=' + city
    jsonTxt = urllib2.urlopen(url).read()
    weather = json.loads(jsonTxt)
    
    return weather

def data(weather):

        print "\nCurrent weather for %s, %s" % (weather['location']['name'], weather['location']['region'])
        print "%s and %s degrees (F)" % (weather['current']['condition']['text'], weather['current']['temp_f'])
        print "It actually feels like %s degrees (F)" % (weather['current']['feelslike_f'])
        
        repeat = MyModule.userString("\nWant to check another location? (y/n):")
        
        return repeat

def main():
   again = True
   
   while again:
       a = weatherAPI()
       b = data(a)
       
       if b == "y":
           again = True
        
       else:
           again = False
   
main()    