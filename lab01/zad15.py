x = input("Podaj wartość: ")

try:
    val = eval(x) 
    
    if isinstance(val, bool):  
        print("boolean")
    elif isinstance(val, int):  
        print("int")
    elif isinstance(val, float):  
        print("float")
    else:
        print("string")
except:
    print("string") 