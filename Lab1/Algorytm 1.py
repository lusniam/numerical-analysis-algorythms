from math import trunc
def koduj(n,p):
    return koduj(n//p,p)+[n%p] if n>0 else []

a=float(input("Podaj liczbę: "))
n=int(input("Podaj dokładność, z jaką przedstawić liczbę A: "))
b=int(input("Podaj podstawę systemu liczbowego: "))
if(b<2):
    print("Podstawa systemu liczbowego musi być większa od 1!")
else:
    if(a==0):
        A="0"
    A=koduj(trunc(a*(b**n)),b)
    A.insert(len(A)-n,".")
    A.extend([0]*(n-len(A)+A.index(".")))
    if(b>=2 and b<=36):
        for i in range(len(A)):
            if(A[i]=='.'):
                continue
            A[i]='0123456789ABCDEFGHIJKLMNOPQRSTUWXYZ'[int(A[i])]
        A="".join(A)
    print("Liczba A w systemie o podstawie",b,"z dokładnością",n,"wynosi:",A)