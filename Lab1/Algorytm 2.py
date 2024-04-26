def silnia(n):
    if n == 0:
        return 1
    else:
        return n * silnia(n-1)
    
def wersTabelki(wspolczynniki, x, stopien):
    wynik=[wspolczynniki[0]]
    for i in range(1, stopien+1):
        wynik.append(wynik[i-1]*x+wspolczynniki[i])
    return wynik


stopien=int(input("Podaj stopień wielomianu: "))
wspolczynniki=[[]]
for i in range(stopien,-1,-1):
    wspolczynniki[0].append(int(input(f"Podaj współczynnik przy x^{i}: ")))
x=int(input("Podaj x: "))
for i in range(stopien+1):
    wspolczynniki.append(wersTabelki(wspolczynniki[i], x, stopien-i))



print("Tabelka:")
for i in wspolczynniki:
    wers=" "*len(str(x)) if wspolczynniki.index(i)==0 else str(x)
    for j in i:
        wers+="|"+str(j).rjust(max([len(str(a)) for a in [b for b in wspolczynniki]]))
    print(wers)

print("Pochodne:")
for i in range(1,stopien+1):
    nrPoch="'"*(i)
    print(f'w{nrPoch}({x}) = {wspolczynniki[i+1][-1]*silnia(i)}')