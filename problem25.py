F = [1, 1]

curF = 1
n = 3

while len(str(curF)) != 1000:
    curF = F[n-2] + F[n-3]
    F.append(F[n-2] + F[n-3])
    n += 1

print(n-1)