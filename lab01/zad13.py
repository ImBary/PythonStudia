class IsEqual():
    def __init__(self,x,y):
        self.x = x
        self.y = y
    def isEqual(self):
        if(self.x == self.y):
            print("TAK")
        else:
            print("NIE")

x = input("pierwsza zmienna: ")
y = input("drua zmienna: ")
result = IsEqual(x,y)
result.isEqual()