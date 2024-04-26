from math import sqrt,log,exp,e,ceil
#import matplotlib.pyplot as plt
import numpy as np

try:
    n = int(input("Podaj liczbe węzłów: "))
except:
    print("Błąd w podanych danych")
    exit()
if(n < 2):
    print("Za mała liczba węzłów")
    exit()

x = []
xi = []
y = []
yi = []

for i in range(n):
    xi.append(eval(str(input(f"Podaj x{i}: ")).replace(" ","").replace(",",".").replace("^","**").replace("E","e").replace("ln","log")))
    yi.append(eval(str(input(f"Podaj y{i}: ")).replace(" ","").replace(",",".").replace("^","**").replace("E","e").replace("ln","log")))
    if(xi[i] in xi[:i]):
        print("Węzeł o takiej wartości x już istnieje")
        exit()

while True:
    print("Funkcja 1: f(x) = a*x+b")
    print("Funkcja 2: f(x) = a*x^2+b")
    print("Funkcja 3: f(x) = a*x^3+b")
    print("Funkcja 4: f(x) = a/x+b")
    print("Funkcja 5: f(x) = a*√x+b")
    print("Funkcja 6: f(x) = a^x*b")
    print("Funkcja 7: f(x) = x^a+b")

    try:
        match index := int(input("Podaj numer funkcji: ")):
            case 1:
                x = [x for x in xi]
                y = [y for y in yi]
            case 2:
                x = [x**2 for x in xi]
                y = [y for y in yi]
            case 3:
                x = [x**3 for x in xi]
                y = [y for y in yi]
            case 4:
                x = [1/x for x in xi]
                y = [y for y in yi]
            case 5:
                x = [sqrt(x) for x in xi]
                y = [y for y in yi]
            case 6:
                x = [x for x in xi]
                y = [log(y) for y in yi]
            case 7:
                x = [log(x) for x in xi]
                y = [log(y) for y in yi]
            case _:
                print("Nie ma takiej funkcji")
                exit()
    except:
        print("Błąd w podanych danych")
        exit()

    sum_x = sum(x)
    print("Suma x =",sum_x)
    sum_x2 = sum([x**2 for x in x])
    print("Suma x^2 =",sum_x2)
    sum_y = sum(y)
    print("Suma y =",sum_y)
    sum_xy = sum([x*y for x,y in zip(x,y)])
    print("Suma x*y =",sum_xy)
    wyzn=(n*sum_x2)-(sum_x**2)
    print("Wyznacznik =",wyzn)
    wyzn_a=((n*sum_xy)-(sum_x*sum_y))
    print("Wyznacznik a =",wyzn_a)
    wyzn_b=(sum_x2*sum_y)-(sum_xy*sum_x)
    print("Wyznacznik b =",wyzn_b)
    a=wyzn_a/wyzn
    b=wyzn_b/wyzn

    print(f"Funkcja aproksymująca ma postać f(x) =", end=" ")

    match index:
        case 1:
            label=str(('x' if a == 1 else '' if a == 0 else f'{a}*x')+(f'+{b}' if b > 0 else '' if b == 0 else f'{b}'))
            func = lambda x: a*x+b
        case 2:
            label=str(('x^2' if a == 1 else '' if a == 0 else f'{a}*x^2')+(f'+{b}' if b > 0 else '' if b == 0 else f'{b}'))
            func = lambda x: a*x**2+b
        case 3:
            label=str(('x^3' if a == 1 else '' if a == 0 else f'{a}*x^3')+(f'+{b}' if b > 0 else '' if b == 0 else f'{b}'))
            func = lambda x: a*x**2+b
        case 4:
            label=str(('' if a == 0 else f'{a}/x')+(f'+{b}' if b > 0 else '' if b == 0 else f'{b}'))
            func = lambda x: a/x+b if x != 0 else 0
        case 5:
            label=str(('√x' if a == 1 else '' if a == 0 else f'{a}*√x')+(f'+{b}' if b > 0 else '' if b == 0 else f'{b}'))
            func = lambda x: a*sqrt(x)+b
        case 6:
            label=str(f'e^({a}*x)*e^{b}' if a !=1 and b!=1 else '0')
            func = lambda x: exp(a*x)*exp(b)
        case 7:
            label=str((f'x^{a}' if a != 1 and a != 0 else 'x' if a == 1 else '1')+(f'+{b}' if b > 0 else '' if b == 0 else f'{b}'))
            func = lambda x: x**a+b

    print(label)
    if input("Czy chcesz zobaczyc wykres funkcji? (Y/n): ") != "n":
        try:
            user_input = float(input("Podaj minimalne x na wykresie (lub enter aby wykorzystać wartości węzłów): "))
            x_min = user_input if user_input < min(xi) else min(xi)
        except:
            x_min = min(xi)
        try:
            user_input = float(input("Podaj maksymalne x na wykresie (lub enter aby wykorzystać wartości węzłów): "))
            x_max = user_input if user_input > max(xi) else max(xi)
        except:
            x_max = max(xi)
        w_x=np.linspace(x_min,x_max,ceil(x_max-x_min)*100)
        w_y = [func(x) for x in w_x]
        plt.title("Wykres funkcji aproksymującej")
        plt.xlabel("x")
        plt.ylabel("g(x)")
        plt.ticklabel_format(axis='both', style='plain')
        plt.plot(w_x,w_y, label=f"Funkcja aproksymująca ( g(x)={label} )")
        plt.scatter(xi,yi, label="Węzły")
        plt.legend()
        plt.show()
    if input("Czy chcesz spróbować z innym wzorem funkcji? (y/N): ") != "y":
        exit()