class Person():
    def __init__(self,imie,nazwisko):
        self.imie = imie
        self.nazwisko = nazwisko
    def przedstawSie(self):
        print(f"nazywam sie {self.imie} {self.nazwisko}")

person1 = Person("Bartek","Kot")
person1.przedstawSie()

class Rectangle():
    def __init__(self, h, w):
        self.h = h
        self.w = w
    def area(self):
        print(f"obowd {self.h * self.w}")
rec = Rectangle(2,"3")
rec.area()