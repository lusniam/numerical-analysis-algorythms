n=int(input("Podaj ilość węzłów: "))
if n<2:
    print("Za mało węzłów!")
    exit()
x=[]
y=[]
for i in range(n):
    x.append(float(input(f"Podaj x{i}: ")))
    if x[i] in x[:i:]:
        print("Węzły nie są różne!")
        exit()
    y.append(float(input(f"Podaj y{i}: ")))

p=float(input("Podaj punkt: "))
if(min(x)>p or max(x)<p):
    print("Punkt nie należy do przedziału!")
    exit()

def neville(x,y,n,p):
    w=[0 for i in range(n)]
    tab=[[0 for i in range(n)] for j in range(n)]
    for k in range(n):
        w[k]=y[k]
        for j in range(k-1,-1,-1):
            w[j]=w[j+1]+(w[j+1]-w[j])*(p-x[k])/(x[k]-x[j])
        for j in range(n):
            tab[j][k-j]=w[j]
    print('\nTabelka:')
    for i in range(n):
        print(f'i = {i}: [',end='')
        for j in range(n-i):
            print(f'{tab[i][j]:>10.4f}',end=', ')
        print(f']')
    return w[0]

print(f"Wartość f({p}) w przybliżeniu wynosi: {neville(x,y,n,p)}")