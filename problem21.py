def d(x):
    sum = 0
    for i in range(1, x):
        if x % i == 0:
            sum += i
    return sum

sum = 0
for a in range(1, 10001):
    b = d(a)
    if a != b and d(b) == a:
        print(a)
        print(b)
        sum += a + b

sum = sum/2
print(sum)