import math

def roundNumers(list,threshold):
    newList =[]
    for i in list:
        if(i<threshold):
           newList.append(math.floor(i/10) * 10)
        else:
            newList.append(math.ceil(i/10)*10)
    print(newList)

print(roundNumers([2.3,6.5,0.2,-1.2,20.3,25.1,-20.1],10))