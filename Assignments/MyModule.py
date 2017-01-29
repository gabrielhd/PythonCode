def userInt(prompt):
    print prompt,
    num = int(raw_input())
    return num
    

def kmtoMi(km):
    return 0.62 * km
    
def userString(prompt):
    print prompt,
    s = raw_input()
    return s
    
def userList(prompt):
    print prompt,
    l = list(raw_input())
    return l