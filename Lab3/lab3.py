n=int(input("Podaj ilość węzłów: "))
if n<2:
    print("Za mało węzłów!")
    exit()
x=[]
y=[]
for i in range(n):
    x.append(float(input(f"Podaj x{i}: ")))
    if i>0:
        if x[i-1]>=x[i]:
            print("Węzły nie są posortowane!")
            exit()
    y.append(float(input(f"Podaj y{i}: ")))

p=float(input("Podaj punkt: "))

def dodajWspolczynniki(w_a, w_b):
    return [a + b for (a, b) in zip(w_a, w_b)]

def obliczFx(x, y, i, k):
    if k==0:
        return y[i]
    return (obliczFx(x,y,i+1,k-1)-obliczFx(x,y,i,k-1))/(x[i+k]-x[i])
    
def obliczWielomian(xs, ys, n):
    wspolczynniki = [0 for x in xs]
    for i in range(n):
        l = obliczFx(xs, ys, 0, i)
        w=[1.0]
        for k in range(i):
            w=dodajWspolczynniki(w+[0],[0]+[-xs[k]*v for v in w])
        while(len(w)<n):
            w=[0]+w
        print('f['+','.join([f'x{i}' for i in range(i+1)])+'] =',l)
        wspolczynniki=dodajWspolczynniki(wspolczynniki,[l*c for c in w])
    return wspolczynniki

wynik=""
wartosc=0
for i,w in enumerate(obliczWielomian(x,y,n)):
    wartosc+=w*p**(n-i-1)
    if w!=0:
        wynik+=('- ' if w<0 else '+ ' if wynik!='' else '')+str(abs(w))+f" {f'* x^{n-i-1}' if n-i-1>=1 else ''} "
print("Wielomian w(x) ma postać:",wynik)
print(f"Wartość f({p}) w przybliżeniu wynosi: {wartosc}")