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

def dodajWspolczynniki(w_a, w_b):
    return [a + b for (a, b) in zip(w_a, w_b)]

def obliczLj(x, i):
    wspolczynniki, mianownik = [1.0], 1.0
    for j in range(len(x)):
        if j != i:
            wspolczynniki = dodajWspolczynniki(wspolczynniki+[0],[0]+[-x[j]*v for v in wspolczynniki])
            mianownik *= x[i]-x[j]
    return [l / mianownik for l in wspolczynniki]

def obliczWielomian(xs, ys):
    wspolczynniki = [0 for x in xs]
    for i in range(len(xs)):
        l = obliczLj(xs, i)
        print(f'l{i}=',[ys[i]*c for c in l])
        wspolczynniki = dodajWspolczynniki(wspolczynniki, [ys[i]*c for c in l])
    return wspolczynniki

wynik=""
for i,w in enumerate(obliczWielomian(x,y)):
    if w!=0:
        wynik+=('-' if w<0 else '+' if i>0 else '')+str(abs(w))+f"*x^{n-i-1}"
print("Wielomian w(x) ma postać:",wynik)

p=float(input("Podaj punkt: "))

def lagrange(x,y,n,p):
    wynik=0
    for i in range(n):
        iloczyn=y[i]
        for j in range(n):
            if i!=j:
                iloczyn*=(p-x[j])/(x[i]-x[j])
        wynik+=iloczyn
    return wynik

if p<x[0] or p>x[n-1]:
    print("Punkt nie należy do przedziału!")
    exit()
print(f"Wartość f({p}) w przybliżeniu wynosi: {lagrange(x,y,n,p)}")