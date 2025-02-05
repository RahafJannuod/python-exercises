string ="hello world"

def upperlower(text):
    counter = 0
    mystr = ""
    for i in text:
        
        if counter %2 == 0:
            mystr+=i.upper()
        else:
            mystr+=i.lower()
        counter +=1
    return mystr
    
print(upperlower(string))


def upperlower2(text):
    isupperiteration = True
    mystr = ""
    for i in text:
        
        if isupperiteration:
            isupperiteration = False
            mystr+=i.upper()
        else:
            isupperiteration = True
            mystr+=i.lower()
        
    return mystr
    
print(upperlower2(string))

def upperlower3(text):
    isupperiteration = True
    mystr = ""
    for i in text:
        
        if isupperiteration:
            mystr+=i.upper()
        else:
            mystr+=i.lower()
        isupperiteration= not isupperiteration
    return mystr
    
print(upperlower3(string))