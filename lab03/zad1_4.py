def dach(znak):
    base = 10
    height = (base + 1) // 2  # Obliczamy wysokość trójkąta
    for i in range(1, height + 1):
        stars = znak * (2 * i - 1)  # Liczba gwiazdek w danym wierszu
        spaces = " " * ((base - len(stars)) // 2)  # Liczba spacji po bokach
        print(spaces + stars + spaces)


def pietro(znak):
    print(4*znak+"OO"+4*znak)




def rysuj_dom(znak_dach, znak_pietro, pietra):
    dach(znak_dach)
    x=0
    while(x<pietra):
        pietro(znak_pietro)
        x+=1
rysuj_dom("*","#",3)