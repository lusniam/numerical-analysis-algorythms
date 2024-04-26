from math import sqrt
sign = lambda x: x/abs(x) if x!=0 else 0
A=[]
while A==[]:
    try:
        A=[int(a) for a in input("Podaj wspolczynniki wektora A oddzielone spacjami: ").split()]
    except:
        print("Błędny wektor, spróbuj jeszcze raz")
        A=[]
norma=sqrt(sum([a*a for a in A]))
t=(-1)*sign(A[0])*norma
Pa=[t if i==0 else 0 for i in range(len(A))]
print(f"||a|| = {norma}\nt = {t}\nWektor Pa po przekształceniach Householdera: {Pa}")