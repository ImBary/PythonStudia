a = input("a: ")
b= input("b: ")
if(int(a)!=0 ):
    print(-1*(b/a))
elif(int(a)==0 and int(b)!=0):
    print("brak")
elif(int(a)==0 and int(b)==0):
    print("nieskonczonosc miejsc")