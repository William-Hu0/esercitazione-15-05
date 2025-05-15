for i in range(3):
    x=int(input("inserisci il codice"))
    v=str(x)
    y="123456"
    if len(v) == 6:
        if v == y:
            print("Porta aperta")
            break
        else:
            print("codice errato")
    else:
        print("il codice deve essere composto da 6 cifre")
print("ERRORE")
while True:
    x=int(input("inserisci il codice"))
    print("ERRORE")