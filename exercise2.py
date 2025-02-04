string = "hello world"
array = ["hi", "hello", "python", "rahaf"]
print(len(string))
print(len(array))

def elementlength(element):
    length = 0
    for i in element:
        length+= 1
        
    return length
    
print(elementlength(string))
print(elementlength(array))