from math import sin, cos, pi, e, log, sqrt
from fractions import Fraction

def metoda_trapezow(f, a, b, n):
    h = (b - a) / n
    fi = [eval(f.replace('x', str(a + i * h))) for i in range(0, n+1)]
    return h * (fi[0] + 2 * sum(fi[1:n]) + fi[n]) / 2

def metoda_simpsona(f, a, b, n):
    h = (b - a) / n
    fi = [eval(f.replace('x', str(a + i * h))) for i in range(0, n+1)]
    return h * (fi[0] + 4 * sum(fi[1:n:2]) + 2*sum(fi[2:n:2]) + fi[n]) / 3

def metoda_simpsona_3_8(f, a, b, n):
    h = (b - a) / n
    fi = [eval(f.replace('x', str(a + i * h))) for i in range(0, n+1)]
    return 3 * h * (fi[0] + 3 * sum(fi[1:n:3]) + 3 * sum(fi[2:n:3]) + 2 * sum(fi[3:n:3]) + fi[n]) / 8

print("Wybierz calke: ")
print("1. 0,1 sqrt(1+x) dx")
print("2. 0,2pi sin(x)^2 + 2 dx")
print("3. 0,2 e^x + 2*x^3 dx")
print("4. 0,4 x*e^(2*x) dx")
print("5. Wlasna calka")
wybor=0
while(wybor < 1 or wybor > 5):
    try:
        wybor = int(input("Wybor: "))
        if wybor < 1 or wybor > 5:
            print("Niepoprawny wybor, podaj jeszcze raz")
    except ValueError:
        print("Niepoprawny wybor, podaj jeszcze raz")
a,b,f='','',''
match wybor:
    case 1:
        a='0'
        b='1'
        f='sqrt(x+1)'
    case 2:
        a='0'
        b='2*pi'
        f='sin(x)**2 + 2'
    case 3:
        a='0'
        b='2'
        f='e**x + 2*(x**3)'
    case 4:
        a='0'
        b='4'
        f='x*e**(2*x)'
    case 5:
        while(a==''):
            a=input("Podaj a: ").replace(" ","").replace(",",".").replace("^","**").replace("E","e").replace("ln","log")
            try:
                eval(a)
            except:
                print("Niepoprawne a, podaj jeszcze raz")
                a=''
        while(b==''):
            b=input("Podaj b: ").replace(" ","").replace(",",".").replace("^","**").replace("E","e").replace("ln","log")
            try:
                eval(b)
            except:
                print("Niepoprawne b, podaj jeszcze raz")
                b=''
        while(f==''):
            f=input("Podaj funkcje: ").replace(" ","").replace(",",".").replace("^","**").replace("E","e").replace("ln","log")
            try:
                eval(f.replace("x","1"))
            except:
                print("Niepoprawna funkcja, podaj jeszcze raz")
                f=''    
wybor=0
while(wybor < 1 or wybor > 3):
    try:
        print("1. Metoda trapezow")
        print("2. Metoda Simpsona")
        print("3. Metoda Simpsona 3/8")
        wybor = int(input("Wybierz metode: "))
        if wybor < 1 or wybor > 3:
            print("Niepoprawny wybor, podaj jeszcze raz")
    except ValueError:
        print("Niepoprawny wybor, podaj jeszcze raz")
if wybor==1:
    wartosc=lambda f,a,b,n: metoda_trapezow(f,a,b,m)
elif wybor==2:
    wartosc=lambda f,a,b,n: metoda_simpsona(f,a,b,m)
else:
    wartosc=lambda f,a,b,n: metoda_simpsona_3_8(f,a,b,m)
m=0
while(m < 1):
    try:
        m = int(input("Podaj m: "))
        if m < 1 or (m % 2 == 1 and wybor==2):
            print("Niepoprawny m, podaj jeszcze raz")
    except ValueError:
        print("Niepoprawny m, podaj jeszcze raz")
if a.find("pi")>-1 or b.find("pi")>-1:
    wartosc=str(Fraction(wartosc(f,eval(a),eval(b),m)/pi).limit_denominator(10))+'*pi'
elif a.find("e")>-1 or b.find("e")>-1:
    if log(wartosc(f,eval(a),eval(b),m))==int(log(wartosc(f,eval(a),eval(b),m))):
        wartosc='e^'+str(Fraction(log(wartosc(f,eval(a),eval(b),m))).limit_denominator(10))
    else:
        wartosc=str(Fraction(wartosc(f,eval(a),eval(b),m)/e).limit_denominator(10))+'*e'
else:
    wartosc=str(wartosc(f,eval(a),eval(b),m))
print(f"Wartosc podanej calki obliczonej metoda {'trapezow' if wybor==1 else 'Simpsona' if wybor==2 else 'Simpsona 3/8'}: {wartosc}")