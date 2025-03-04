def czy_zbalansowane(napis: str) -> bool:
    stos = []
    pary = {')': '(', ']': '[', '}': '{'}
    
    for znak in napis:
        if znak in pary.values(): 
            stos.append(znak)
        elif znak in pary.keys():
            if not stos or stos.pop() != pary[znak]:
                return False
    
    return not stos 
print(czy_zbalansowane("()(){}"))