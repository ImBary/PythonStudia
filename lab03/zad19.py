import math

def rysuj_i_oblicz(typ, *args):
    if typ == "kwadrat":
        bok = args[0]
        for _ in range(bok):
            print("* " * bok)
        pole = bok ** 2
    
    elif typ == "prostokat":
        szerokosc, wysokosc = args
        for _ in range(wysokosc):
            print("* " * szerokosc)
        pole = szerokosc * wysokosc

    elif typ == "kolo":
        promien = args[0]
        for y in range(-promien, promien + 1):
            for x in range(-promien, promien + 1):
                if x**2 + y**2 <= promien**2:
                    print("*", end=" ")
                else:
                    print(" ", end=" ")
            print()
        pole = math.pi * promien**2

    else:
        return "Nieznana figura"

    print(f"\nPole {typ}: {pole:.2f}")
    return pole



rysuj_i_oblicz("kwadrat", 5)
rysuj_i_oblicz("prostokat", 6, 3)
rysuj_i_oblicz("kolo", 5)
