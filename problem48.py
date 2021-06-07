sum = 0

for n in range(1, 1001):
    sum += n**n
sum = str(sum)
print(sum[len(sum)-10:len(sum)])