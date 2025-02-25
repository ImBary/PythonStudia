x = input("zmienna liczbowa: ")
liczba = int(x)
jednostki = liczba % 10
dziesiątki = (liczba // 10) % 10
setki = (liczba // 100) % 10

print(f"Jednostki: {jednostki}")
print(f"Dziesiątki: {dziesiątki}")
print(f"Setki: {setki}")