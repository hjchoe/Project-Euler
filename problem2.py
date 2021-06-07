nterm = 0
fterm = 1
sterm = 2
sum = 0 + sterm

while nterm <= 4000000:
    nterm = fterm + sterm
    if nterm % 2 == 0:
        sum += nterm
    fterm = sterm
    sterm = nterm

print(sum)
