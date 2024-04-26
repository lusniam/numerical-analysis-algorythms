from fractions import Fraction

print("Wpisz 'dane', aby wprowadzić własną macierz, lub 'test'/'test2'/'test3' aby użyć przykładowych danych")
A=[]
B=[]
while True:
    try:
        choice = input()
        if choice == 'dane':
            print("Wprowadź macierz:")
            print("Wprowadź wierszami, oddzielając elementy spacjami")
            print("Ostani element oddziel znakiem |")
            print("Wpisz 'koniec', aby zakończyć wprowadzanie")
            while True:
                line = input()
                if line == 'koniec':
                    break
                else:
                    line=line.split()
                    line.remove('|')
                    line=[float(i) for i in line]
                    A.append(line[:-1])
                    B.append(line[-1])
                    
            break
        elif choice == 'test':
            A=[[1,2,3],[2,8,10],[3,10,22]]
            B=[1,3,7]
            break
        elif choice == 'test2':
            A=[[4,6,-4,-6],[6,25,6,-17],[-4,6,14,1],[-6,-17,1,23]]
            B=[2,-13,-14,5]
            break
        elif choice == 'test3':
            A=[[1,-2,3],[-2,5,-8],[3,-8,17]]
            B=[1,-1,3]
            break
        else:
            print("Nieprawidłowy wybór")
    except ValueError:
        print("Nieprawidłowe dane")

def wyswietlMacierz(A,fractions=0):
    for w in A:
        for l in w:
            print(Fraction(l).limit_denominator() if fractions else l,end="\t")
        print()

def transpozycja(A):
    return [[A[j][i] for j in range(len(A))] for i in range(len(A[0]))]

print("Macierz A:")
wyswietlMacierz(A)

def choleski(A):
    n = len(A)
    M = [[0]*n for i in range(n)]
    D = [0]*n
    for s in range(n):
        for i in range(s,n):
            if i == s:
                M[s][s] = 1
                D[s] = A[s][s]-sum([D[k]*(M[s][k]**2) for k in range(s)])
            else:
                M[i][s] = (A[i][s]-sum([D[k]*M[i][k]*M[s][k] for k in range(s)]))/D[s]
    return M,D

M,D = choleski(A)
MT=transpozycja(M)
print("Macierz M:")
wyswietlMacierz(M,1)
print("Wektor D:")
print(D)

def wartosci(A,B,odwrotnie=0):
    x = [0]*len(A)
    if odwrotnie:
        for i in range(len(A)):
            A[i].reverse()
    for i in range(len(A)):
        A[i].append(B[i])
    if odwrotnie:
        A.reverse()
    for i in range(len(A)-1,-1,-1):
        x[i] = A[i][-1]
        for j in range(i+1,len(A)):
            x[i] -= A[i][j]*x[j]
        x[i] /= A[i][i]
    if odwrotnie:
        x.reverse()
    return x

Y=wartosci(M,B,1)
print("Wartości y:")
for i,y in enumerate(Y):
    print("y"+str(i+1)+" = "+str(Fraction(y).limit_denominator()))

X=wartosci(MT,[Y[i]/D[i] for i in range(len(Y))])
print("Wartości x:")
for i,x in enumerate(X):
    print("x"+str(i+1)+" = "+str(Fraction(x).limit_denominator()))