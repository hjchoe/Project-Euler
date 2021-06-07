def numfactors(x):
    nfactors = 0
    for i in range(1, int(x**0.5) + 1):
        if x % i == 0:
           nfactors += 2
    return nfactors

def trianglenum(x):
    i = 1
    num = 0
    while i <= x:
        num += i
        i += 1
    return num

def nexttri(n, x):
    n = n + x
    return n

i = 1
n = 0
while True:
    #n = trianglenum(i)
    n = nexttri(n, i)
    nof = numfactors(n)
    print(f"{n}: {nof} factors")
    if nof > 500:
        break
    i += 1

print(n)