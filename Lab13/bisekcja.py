from math import sin, cos, pi, e, log, sqrt
from fractions import Fraction
from sys import setrecursionlimit

setrecursionlimit(10**8)
print("Wybierz calke: ")
print("1. 0,1 sqrt(1+x) dx")
print("2. 0,2pi sin(x)^2 + 2 dx")
print("3. Wlasne dane")
wybor=0
while(wybor < 1 or wybor > 3):
    try:
        wybor = int(input("Wybor: "))
        if wybor < 1 or wybor > 3:
            print("Niepoprawny wybor, podaj jeszcze raz")
    except ValueError:
        print("Niepoprawny wybor, podaj jeszcze raz")
a,b,f,eps='','','',''
match wybor:
    case 1:
        a='0'
        b='2'
        f='(x)**4+5*((x)**2)-3*x-15'
        eps='0.05'  
    case 2:
        a='1'
        b='2'
        f='sin(x)-(x/2)'
        eps='0.001'
    case 3:
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
            f=input("Podaj funkcje: ").replace(" ","").replace(",",".").replace("^","**").replace("E","e").replace("ln","log").replace('x','(x)')
            try:
                eval(f.replace("x","1"))
            except:
                print("Niepoprawna funkcja, podaj jeszcze raz")
                f=''
        while(eps==''):
            eps=input("Podaj epsilon: ").replace(" ","").replace(",",".").replace("^","**").replace("E","e").replace("ln","log")
            try:
                eval(eps)
            except:
                print("Niepoprawne epsilon, podaj jeszcze raz")
                eps=''

if eval(f.replace('x',a))*eval(f.replace('x',b))>1:
    print("W podanym przedziale nie ma pierwiastkow")
    exit()
elif eval(f.replace('x',a))==0:
    print("Punkt a jest pierwiastkiem")
    exit()
elif eval(f.replace('x',b))==0:
    print("Punkt b jest pierwiastkiem")
    exit()

def bisekcja(f,a,b,eps,krok=0):
    s=str((eval(a)+eval(b))/2)
    krok+=1
    if abs(eval(f.replace('x',s)))<eval(eps):
        return s,krok
    elif eval(f.replace('x',a))*eval(f.replace('x',str(s)))<1:
        return bisekcja(f,a,s,eps,krok)
    else:
        return bisekcja(f,s,b,eps,krok)
    
s,krok=bisekcja(f,a,b,eps)

print(f"Pierwiastkiem funkcji jest punkt {s} osiagniety po {krok} krokach")