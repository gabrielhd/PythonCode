import json
import MyModule



def readFile(file):
    jsonTxt = ""
    f = open('myClasses.json')

    for line in f:
        line = line.strip()
        jsonTxt = jsonTxt + line
    
    return jsonTxt

def Search(jsonTxt):
    classes = json.loads(jsonTxt)
    name = MyModule.userString("Enter a class:")
    for classs in classes:
        if classs["Name"] == name:
            print "\n%s" % classs["Professor"]
        
    for time in classs["Time"]:
        print time
            
def main():
  data = readFile(file)
  Search(data)


main()
    
    