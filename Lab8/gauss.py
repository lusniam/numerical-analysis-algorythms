from math import sin, cos, pi, e, log, sqrt, factorial
from numpy import roots, round

print("Wybierz calke: ")
print("1. -1,1 x^2/sqrt(1-x^2) dx Gauss-Chebyshev dla n=3")
print("2. -1,1 1/sqrt(1+x^2) dx Gauss-Legendre dla n=4")
print("3. 0,inf e^(-2x) * sin(x)/x dx Gauss-Laguerre dla n=3")
print("4. -inf,inf e^(-x^2) cos(x) dx Gauss-Hermite dla n=4")
print("5. Wlasna calka")
wybor=0
while(wybor < 1 or wybor > 5):
    try:
        wybor = int(input("Wybor: "))
        if wybor < 1 or wybor > 5:
            print("Niepoprawny wybor, podaj jeszcze raz")
    except ValueError:
        print("Niepoprawny wybor, podaj jeszcze raz")
f,t,n='',0,0
match wybor:
    case 1:
        f='(x)**2/sqrt(1-x**2)'
        n=3
        t='Chebyshev'
    case 2:
        f='1/sqrt(1+x**2)'
        n=4
        t='Legendre'
    case 3:
        f='(e**(-2*x))*sin(x)/x'
        n=3
        t='Laguerre'
    case 4:
        f='e**(-(x**2))*cos(x)'
        n=4
        t='Hermite'
    case 5:
        while(f==''):
            f=input("Podaj funkcje: ").replace(" ","").replace(",",".").replace("^","**").replace("E","e").replace("ln","log")
            try:
                eval(f.replace("x","0"))
            except:
                try:
                    eval(f.replace("x","1"))
                except:
                    print("Niepoprawna funkcja, podaj jeszcze raz")
                    f=''
        while(t < 1 or t > 4):
            try:
                print("Wybierz rodzaj kwadratury: ")
                print("1. Gauss-Chebyshev")
                print("2. Gauss-Legendre")
                print("3. Gauss-Laguerre")
                print("4. Gauss-Hermite")
                t = int(input("Wybor: "))
                if t < 1 or t > 4:
                    print("Niepoprawny wybor, podaj jeszcze raz")
            except ValueError:
                print("Niepoprawny wybor, podaj jeszcze raz")
        match t:
            case 1:
                t='Chebyshev'
            case 2:
                t='Legendre'
            case 3:
                t='Laguerre'
            case 4:
                t='Hermite'
        while(n < 1):
            try:
                n = int(input("Podaj n: "))
                if n < 1:
                    print("Niepoprawne n, podaj jeszcze raz")
                    n=0
            except ValueError:
                print("Niepoprawne n, podaj jeszcze raz")
                n=0

def addLists(a,b):
    for i in range(len(a)):
        try:
            t=b[i]
        except:
            b.insert(0,0)
    for i in range(len(b)):
        try:
            t=a[i]
        except:
            a.insert(0,0)
    return [a[i]+b[i] for i in range(len(a))]

def addToList(l,num):
    l.append(num)
    return l

def multiplyList(l,num):
    return [x * num for x in l]

def pochodna(w):
    return [w[i]*(len(w)-i-1) for i in range(len(w)-1)]

def wartosc(w,x):
    return sum([w[i]*x**(len(w)-i-1) for i in range(len(w))])

def legendre(n):
    if n==0:
        return [1]
    elif n==1:
        return [1,0]
    else:
        return addLists(multiplyList(addToList(legendre(n-1),0),2-1/n),multiplyList(legendre(n-2),-(1-1/n)))

def chebyshev(n):
    if n==0:
        return [1]
    elif n==1:
        return [1,0]
    else:
        return addLists(multiplyList(addToList(chebyshev(n-1),0),2),multiplyList(chebyshev(n-2),-1))

def laguerre(n):
    if n==0:
        return [1]
    elif n==1:
        return [-1,1]
    else:
        return multiplyList(addLists(addLists(multiplyList(addToList(laguerre(n-1),0),-1),multiplyList(laguerre(n-1),2*n-1)),multiplyList(laguerre(n-2),1-n)),1/n)        

def hermite(n):
        if n==0:
            return [1]
        elif n==1:
            return [2,0]
        else:
            return addLists(multiplyList(addToList(hermite(n-1),0),2),multiplyList(hermite(n-2),-2*(n-1)))

def gauss(f,n,rodzaj):
    match rodzaj:
        case 'Chebyshev':
            wielomian=lambda n: chebyshev(n)
            norma = pi if n==0 else pi/2
            waga = lambda x: 1/sqrt(1-x**2)
        case 'Legendre':
            wielomian=lambda n: legendre(n)
            norma = 2/(2*n+1)
            waga = lambda x: 1
        case 'Laguerre':
            wielomian=lambda n: laguerre(n)
            norma = 1
            waga = lambda x: e**(-x)
        case 'Hermite':
            wielomian=lambda n: hermite(n)
            norma = 2**n * factorial(n) * sqrt(pi)
            waga = lambda x: e**(-x**2)
        case _:
            print("Nie ma takiego wielomianu")
            return None
    func = lambda x: eval(f.replace("x",str(x) if x>=0 else "("+str(x)+")"))/waga(x)
    wn=wielomian(n)
    wn1=wielomian(n+1)
    wezly=sorted(roots(wn1))
    wspolczynniki=[(wn1[0]/wn[0])*(norma/(wartosc(pochodna(wn1),x)*wartosc(wn,x))) for x in wezly]
    wynik=0
    print("j\txj\tHj\tf(xj)")
    for i in range(n+1):
        print(i,end="\t")
        print("{:.4f}".format(wezly[i]),end="\t")
        print("{:.4f}".format(wspolczynniki[i]),end="\t")
        print("{:.4f}".format(fx:=func(wezly[i])))
        wynik+=wspolczynniki[i]*fx
    return wynik
print("Wynik:",round(gauss(f, n, t),6)) # type: ignore