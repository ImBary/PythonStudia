from math import sqrt


def odleglosc(p1,p2):
    x = (p1[0] - p2[0])**2
    y = (p1[1] - p2[1])**2
    return(sqrt(x+y))



def obwodTrojkata(p1,p2,p3):
    return odleglosc(p1,p2) + odleglosc(p1,p3)+odleglosc(p2,p3)
print(obwodTrojkata([0,0],[0,4],[4,4]))

def czyWspolniniowe(p1,p2,p3):
    mAB = (p2[1]-p1[1])/(p2[0]-p1[0]) 
    mBC = (p3[1]-p2[1])/(p3[0]-p2[0])
    if(mAB==mBC):
        return True
    return False

#if (not czyWspolniniowe([0,0],[0,0],[0,0])):
   #obwodTrojkata([])