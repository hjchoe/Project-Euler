fsum = 0
ssum = 0

for n in range(1, 101):
    fsum += n * n
    ssum += n
ssum = ssum * ssum
sum = ssum - fsum
print(sum)
