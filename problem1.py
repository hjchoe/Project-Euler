n = 1000
i = 0
sum = 0
while i < 1000:
    if i % 3 == 0:
        sum += i
    elif i % 5 == 0:
        sum += i
    i += 1
print(sum)