tot=0
while True:
    print("inserisci 0 per terminare il programma")
    x=int(input("inserisci il peso dei vestiti in grammi"))
    if x==0:
        break
    elif tot+x<9000:
        tot += x
        print("aggiunto con successo")
    elif tot+x>=9000:
        print("non puoi aggiungerlo pesa troppo")
    
print(f"i tuoi capi in totale pesano {tot}")