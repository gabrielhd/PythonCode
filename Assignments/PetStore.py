import json
import MyModule



def readFile(file):
    jsonTxt = ""
    f = open('PetStore.json')

    for line in f:
        line = line.strip()
        jsonTxt = jsonTxt + line
    return jsonTxt

def Search(jsonTxt):
    store = json.loads(jsonTxt)
    choice = MyModule.userString("Search by category (c) or keyword (k)").lower()
    
    if choice == "c":
        catg = MyModule.userString("\nEnter a Category:").title()
        
        for c in store:
            if c["Category"] == catg:
                print "%s - $%s" % (c["Product"], c["Price"])
   
    if choice == "k":
        key = MyModule.userString("\nEnter a Keyword:").title()
        
        for c in store:
            if key in c["Product"]:
                print "%s - $%s" % (c["Product"], c["Price"])        
            
            
def main():
  data = readFile(file)
  Search(data)


main()
    
    