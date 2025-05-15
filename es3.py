tot=0
totkg=tot/1000
def menu():
    print("inserisci 0 per terminare il programma")
    print("inserisci 1 per aggiungere vestiti in grammi al totale (massimo 9kg)")
    print("inserisci 2 per convertire da kg a libbre")
    print("inserisci 3 per calcolare il costo")
while True:
    menu()
    a=int(input())
    if a==0:
        break
    elif a==1:
        x=int(input("inserisci il peso dei vestiti in grammi"))
        if tot+x<9000:
            tot += x
            print("aggiunto con successo")
        elif tot+x>=9000:
            print("non puoi aggiungerlo pesa troppo")
    elif a==2:
        k=int(input("inserire peso in kg"))
        print(f"libbra {k/2}")
    elif a==3:
        t=int(input("a quanti gradi è la temperatura"))
        if totkg>5:
            if t==40:
                print(f"il costo è {totkg*0.50} euro")
            elif t==60:
                print(f"il costo è {totkg*0.75} euro")
            elif t==90:
                print(f"il costo è {totkg} euro")
        elif totkg>=5:
            if t==40:
                print(f"il costo è {totkg*0.75} euro")
            elif t==60:
                print(f"il costo è {totkg} euro")
            elif t==90:
                print(f"il costo è {totkg*1.50} euro")
print(f"i tuoi capi in totale pesano {tot}")