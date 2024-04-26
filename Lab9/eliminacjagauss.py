from fractions import Fraction

print("Wpisz 'dane', aby wprowadzić własną macierz, lub 'test'/'test2'/'test3' aby użyć przykładowych danych")
A=[]
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
                    A.append(line)
                    
            break
        elif choice == 'test':
            A=[[14,-13,3,-16,-42,-37],[3.5,-18,13,-23.75,-21,-5.5],[3.5,3,-5.25,9.25,10.5,12.5],[2,14.5,-10.5,18.5,21,23.5],[1.5,6.75,-9.25,17,-10.5,-45.25]]
            break
        elif choice == 'test2':
            A=[[1,2,3,0],[4,5,6,0],[7,8,9,0]]
            break
        elif choice == 'test3':
            A = [[1,-2,0,3,1,1],[2,-3,1,8,2,3],[1,-2,1,3,-1,1],[0,1,0,3,5,0],[1,-2,0,5,8,-1]]
            break
        else:
            print("Nieprawidłowy wybór")
    except ValueError:
        print("Nieprawidłowe dane")

print("Wybierz metodę eliminacji:")
print("1. Eliminacja Gaussa (podstawowa)")
print("2. Eliminacja Gaussa (z pełnym wyborem elementu maksymalnego)")
choice = 0
while choice == 0:
    try:
        choice = int(input())
        if choice != 1 and choice != 2:
            print("Nieprawidłowy wybór")
            choice = 0
    except ValueError:
        print("Nieprawidłowy wybór")
        choice = 0

def wyswietlMacierz(A,fractions=0):
    for w in A:
        for i,l in enumerate(w):
            if i == len(w)-1:
                print("|\t",Fraction(l).limit_denominator() if fractions else l)
            else:
                print(Fraction(l).limit_denominator() if fractions else l,end="\t")

def gauss_podst(A): 
    for i in range(len(A)):
        if A[i][i] == 0:
            print("Nie da się wykonać eliminacji Gaussa metodą podstawową")
            exit()
        for j in range(i+1,len(A)):
            m = A[j][i]/A[i][i]
            for k in range(len(A[j])):
                A[j][k] -= m*A[i][k]
        print(f'Krok {i+1}:')
        if i+1!=len(A):
            wyswietlMacierz(A,1)
    return A,[]

def gauss_pelny(A):
    zamiany=[]
    for i in range(len(A)):
        max = 0
        index = (0,0)
        for j in range(i,len(A)):
            for k in range(i,len(A)):
                if abs(A[j][k]) > max:
                    max = abs(A[j][k])
                    index = (j,k)
        if max == 0:
            for j in range(i,len(A)):
                if A[j][-1] != 0:
                    print("Podany układ równań jest sprzeczny!")
                    exit()
                else:
                    print("Podany układ równań jest nieoznaczony!")
                    exit()
        if index[0] != i:
            A[i],A[index[0]] = A[index[0]],A[i]
        if index[1] != i:
            for j in range(len(A)):
                A[j][i],A[j][index[1]] = A[j][index[1]],A[j][i]
            zamiany.append((i,index[1]))
        if i+1!=len(A):
            print(f'Krok {i+1}, wyznaczenie wartości maksymalnej:')
            wyswietlMacierz(A,1)
        for j in range(i+1,len(A)):
            m = A[j][i]/A[i][i]
            for k in range(len(A[j])):
                A[j][k] -= m*A[i][k]
        if i+1!=len(A):
            print(f'Krok {i+1}:')
            wyswietlMacierz(A,1)
    return A,zamiany

print("Macierz A:")
wyswietlMacierz(A)

A,zamiany=gauss_podst(A) if choice == 1 else gauss_pelny(A)

print("Macierz A po eliminacji Gaussa "+("(podstawowej):" if choice == 1 else "(z pełnym wyborem elementu maksymalnego):"))
wyswietlMacierz(A,1)

def wartosci(A,zamiany):
    x = [0]*len(A)
    for i in range(len(A)-1,-1,-1):
        x[i] = A[i][-1]
        for j in range(i+1,len(A)):
            x[i] -= A[i][j]*x[j]
        x[i] /= A[i][i]
    if zamiany != []:
        for i in range(len(zamiany)-1,-1,-1):
            x[zamiany[i][0]],x[zamiany[i][1]] = x[zamiany[i][1]],x[zamiany[i][0]]
    return x

print("Wartości x:")
for i,x in enumerate(wartosci(A,zamiany)):
    print("x"+str(i+1)+" = "+str(round(x,5)))