from math import sin, cos, pi, e, log, sqrt
from fractions import Fraction

print("Wybierz zadanie: ")
print("1. y'=y^2/(x+1), y(0)=3, n=5, b=1, metoda Euler'a")
print("2. y'=y/(x^2), y(1)=2, n=2, b=1.5, metoda Heuna")
print("3. y'=2*x*y, y(0)=1, n=2, b=0,5, metoda zmodyfikowana Eulera")
print("4. Wlasne")
wybor=0
while(wybor < 1 or wybor > 4):
    try:
        wybor = int(input("Wybor: "))
        if wybor < 1 or wybor > 5:
            print("Niepoprawny wybor, podaj jeszcze raz")
    except ValueError:
        print("Niepoprawny wybor, podaj jeszcze raz")
y,a,ya,b,n,metoda='','','','','',0
match wybor:
    case 1:
        y='y**2/(x+1)'
        a='0'
        ya='3'
        b='1'
        n='5'
        metoda=1
    case 2:
        y='y/(x**2)'
        a='1'
        ya='2'
        n='2'
        b='1.5'
        metoda=2
    case 3:
        y='2*x*y'
        a='0'
        ya='1'
        n='2'
        b='0.5'
        metoda=3
    case 4:
        while(y==''):
            y=input("Podaj pochodna: ").replace(" ","").replace(",",".").replace("^","**").replace("E","e").replace("ln","log")
            try:
                eval(y.replace("x","1").replace("y","1"))
            except:
                print("Niepoprawna pochodna, podaj jeszcze raz")
                y=''
        while(a==''):
            a=input("Podaj a: ").replace(" ","").replace(",",".").replace("^","**").replace("E","e").replace("ln","log")
            try:
                eval(a)
            except:
                print("Niepoprawne a, podaj jeszcze raz")
                a=''
        while(ya==''):
            ya=input("Podaj y(a): ").replace(" ","").replace(",",".").replace("^","**").replace("E","e").replace("ln","log")
            try:
                eval(ya)
            except:
                print("Niepoprawne y(a), podaj jeszcze raz")
                ya=''
        while(n==''):
            n=input("Podaj n: ")
            try:
                int(n)
            except:
                print("Niepoprawne n, podaj jeszcze raz")
                n=''
        while(b==''):
            b=input("Podaj b: ").replace(" ","").replace(",",".").replace("^","**").replace("E","e").replace("ln","log")
            try:
                eval(b)
            except:
                print("Niepoprawne b, podaj jeszcze raz")
                b=''
        while(metoda < 1 or metoda > 3):
            try:
                print("1. Metoda Eulera")
                print("2. Metoda Heuna")
                print("3. Metoda zmodyfikowana Eulera")
                metoda = int(input("Wybierz metode: "))
                if metoda < 1 or metoda > 3:
                    print("Niepoprawny wybor, podaj jeszcze raz")
            except ValueError:
                print("Niepoprawny wybor, podaj jeszcze raz")
                metoda=0

a=float(a)
b=float(b)
n=int(n)
ya=float(ya)

def wartosc(y,a,ya,b,n,metoda):
    h=(b-a)/n
    match metoda:
        case 1:
            skladnik=lambda h,f,xi,yi: h*eval(f.replace("x",str(xi)).replace("y",str(yi)))
        case 2:
            skladnik=lambda h,f,xi,yi: h/2*(eval(f.replace("x",str(xi)).replace("y",str(yi)))+eval(f.replace("x",str(xi+h)).replace("y",str(yi+h*eval(f.replace("x",str(xi)).replace("y",str(yi)))))))
        case 3:
            skladnik=lambda h,f,xi,yi: h*eval(f.replace("x",str(xi+h/2)).replace("y",str(yi+h/2*eval(f.replace("x",str(xi)).replace("y",str(yi))))))
        case _:
            print("Błąd danych")
            exit()
    for i in range(n):
        ya+=skladnik(h,y,a+(i*h),ya)
    return ya
print(f"y({b}) = {round(wartosc(y,a,ya,b,n,metoda),5)}")