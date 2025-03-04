def cypel(text, key):
    if len(text) < key:
        return text
    lista = list(text)  
    for i in range(key, len(lista), key):  
        lista[i], lista[i - key] = lista[i - key], lista[i]  
    return "".join(lista)

print(cypel("123456789AB", 5))
