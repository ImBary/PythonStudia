def prime_selector(numbers):
    newList = []
    for i in numbers:
        if(isPrime(i)):
            newList.append(i)
    print(newList)

def isPrime(number):
    if(number < 2 and number > -2):
        return False
    for i in range(2,number):
        if(number%i == 0 and number != i):
            return False
    return True
        
lista = [3,2,-3,5,6,7,19,18,14]
prime_selector(lista)