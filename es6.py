while True:
    l=[]
    f=0
    print("inserisci 0 per terminare in quanto devi pagare")
    x=float(input("inserisci quanto devi pagare"))
    if x==0:
        break
    y=float(input("inserisci con quanto paghi"))
    if y<x:
        print("non è abbastanza")
    elif y>=x:
        g=y-x
        c=g*100
        while True:
            if c>100:
                c-=100
                f+=1
            else:
                break
        n2=g-f
        l.append(f)
        l.append(n2)
        tuple(l)
        print(l)

