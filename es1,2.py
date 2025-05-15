while True:
    x=input("inserisci il codice")
    y="123456"
    if len(x) == 6:
        if x == y:
            print("Porta aperta")
            break
        else:
            print("codice errato")
    else:
        print("il codice deve essere composto da 6 cifre")