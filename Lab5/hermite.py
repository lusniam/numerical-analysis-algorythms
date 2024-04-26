n=int(input("Podaj ilość węzłów: "))
if n<2:
    print("Za mało węzłów!")
    exit()
x=[]
f=[]
k=[]
for i in range(n):
    x.append(float(input(f"Podaj x{i}: ")))
    if x[i] in x[:i:]:
        print("Węzły nie są różne!")
        exit()
    k.append(int(input(f"Podaj k{i}: ")))
    if(k[i]<1):
        print("Za mała krotność!")
        exit()
    ftemp=[]
    for j in range(k[i]):
        ftemp.append(float(input("Podaj f"+"'"*j+f"({x[i]}): ")))
    f.append(ftemp)

p=float(input("Podaj punkt: "))
if(min(x)>p or max(x)<p):
    print("Punkt nie należy do przedziału!")
    exit()

print('\nTabelka:')

def silnia(x):
    if(x==0):
        return 1
    else:
        return x*silnia(x-1)

def dodajWspolczynniki(w_a, w_b):
    return [a + b for (a, b) in zip(w_a, w_b)]

def hermite(x,f,k,n,p):
    tab=[[float(0) for i in range(sum(k)+1)] for j in range(sum(k))]
    t=0
    for i in range(len(k)):
        for j in range(t,t+k[i]):
            tab[j][0]=x[i]
            tab[j][1]=f[i][0]
        t+=k[i]
    
    for i in range(2,sum(k)+2):
        for j in range(i-1,sum(k)):
            if(tab[j][0]==tab[j-i+1][0]):
                tab[j][i]=f[x.index(tab[j][0])][i-1]/silnia(i-1)
            else:
                tab[j][i]=(tab[j][i-1]-tab[j-1][i-1])/(tab[j][0]-tab[j-i+1][0])

    for i in range(sum(k)):
        print(f'[',end='')
        for j in range(i+2):
            print(f'{tab[i][j]:>10.4f}',end=', ')
        print(f']')

    wspolczynniki = [float(0) for i in range(sum(k))]
    for i in range(sum(k)):
        w=[1.0]
        for j in range(i):
            w=dodajWspolczynniki(w+[0],[0]+[-tab[j][0]*v for v in w])
        while(len(w)<sum(k)):
            w=[0]+w
        wspolczynniki=dodajWspolczynniki(wspolczynniki,[tab[i][i+1]*c for c in w])
    
    wynik=""
    wartosc=0
    for i,w in enumerate(wspolczynniki):
        wartosc+=w*p**(sum(k)-i-1)
        if w!=0:
            wynik+=('- ' if w<0 else '+ ' if wynik!='' else '')+str(abs(w))+f" {f'* x^{sum(k)-i-1}' if sum(k)-i-1>=1 else ''} "
    print("Wielomian w(x) ma postać:",wynik)
    return wartosc

print(f"Wartość f({p}) w przybliżeniu wynosi: {hermite(x,f,k,n,p)}")