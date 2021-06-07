bninchain = 0
num = 0

def chainlen(n):
    ninchain = 1
    while n > 1:
        if n % 2 == 0:
            n = n/2
        else:
            n = 3 * n + 1
        ninchain += 1
    return ninchain

for n in range(1000000):
    ninchain = chainlen(n)
    if ninchain > bninchain:
        bninchain = ninchain
        num = n
    print(f"{n}: {ninchain}")

print(f"{num}: {bninchain}")
